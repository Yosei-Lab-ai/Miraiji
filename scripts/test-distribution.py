#!/usr/bin/env python3
"""Check the delivered ZIP with isolated buyer HOME fixtures; keep evidence."""

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('persona', 'pricing', 'gtm')
TEMPLATES = ('persona.md', 'pricing.md', 'gtm-strategy.md')


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def bash_path(bash, path):
    if os.name == 'nt':
        return subprocess.check_output([bash, '-c', 'cygpath -u "$1"', '--', str(path)], text=True).strip()
    return str(path)


def install(bash, distribution, home, log, expected=0):
    home.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env['HOME'] = bash_path(bash, home)
    env['MSYS_NO_PATHCONV'] = '1'
    process = subprocess.run(
        [bash, '-c', 'export PATH=/usr/bin:/bin:$PATH; exec "$BASH" ./setup'],
        cwd=distribution, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    log.write_text(process.stdout, encoding='utf-8')
    check(process.returncode == expected, f'{log.name}: expected {expected}, got {process.returncode}; see log')


def snapshot(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}


def validate_skill(text, name, archive):
    check(re.match(r'---\r?\nname: ' + name + r'\r?\ndescription: .+\r?\nuser-invocable: true', text), f'{name}: frontmatter')
    check('references/hypothesis-contract.md' in text, f'{name}: packaged reference')
    check('../docs/' not in text, f'{name}: repository-only reference')
    check('references/hypothesis-contract.md' in archive, f'{name}: missing shared document')
    check('## Resume before asking questions' in text and 'Before introducing yourself' in text, f'{name}: early resume')
    check('resume_from' in text and 'output_refs' in text and 'existing answers' in text, f'{name}: resume pointer')
    check('next unused' in text and 'Preserve existing files' in text, f'{name}: save safety')
    check(not re.search(r'(?<![A-Za-z])/(' + '|'.join(('market-scan','bizplan','launch','content','outreach','measure','grow','feedback','biz-retro')) + r')\b', text), f'{name}: unavailable command')
    check(set(re.findall(r'`/([a-z]+(?:-[a-z]+)*)`', text)) <= set(SKILLS), f'{name}: only shipped skill commands')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--bash', required=True, help='Existing Bash executable; no installation or model calls')
    args = parser.parse_args()
    work = Path(args.output_dir).resolve()
    check(not work.exists(), 'Choose a new, dedicated buyer-test directory')
    work.mkdir(parents=True)
    spec = importlib.util.spec_from_file_location('miraiji_distribution', ROOT / 'scripts/build-distribution.py')
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    archives = builder.build(work / 'zips')
    expected_bundle = {'README.md','LICENSE','VERSION','setup','docs/hypothesis-contract.md'}
    for skill, template in zip(SKILLS, TEMPLATES):
        expected_bundle.update({f'{skill}/SKILL.md',f'{skill}/references/hypothesis-contract.md',f'templates/{template}'})
        with zipfile.ZipFile(work / 'zips' / f'miraiji-{skill}.zip') as archive:
            expected = {'SKILL.md','README.md','LICENSE','VERSION','references/hypothesis-contract.md',f'templates/{template}'}
            check(set(archive.namelist()) == expected, f'{skill}: submission allowlist')
            validate_skill(archive.read('SKILL.md').decode('utf-8'), skill, archive.namelist())
            check(archive.read('LICENSE') == (ROOT/'LICENSE').read_bytes(), f'{skill}: MIT notice')
            check(archive.read('references/hypothesis-contract.md') == (ROOT/'docs/hypothesis-contract.md').read_bytes(), f'{skill}: complete common contract')
    distribution = work / 'extracted'
    with zipfile.ZipFile(work / 'zips/miraiji-phase1.zip') as archive:
        check(set(archive.namelist()) == expected_bundle, 'bundle allowlist')
        archive.extractall(distribution)
    check((distribution/'LICENSE').read_bytes() == (ROOT/'LICENSE').read_bytes(), 'bundle MIT rights')
    fresh = work/'fresh-home'
    install(args.bash, distribution, fresh, work/'fresh.log')
    installed = fresh/'.claude/skills'
    check(set(p.name for p in installed.iterdir()) == set(SKILLS), 'only three commands installed')
    for skill in SKILLS:
        text = (installed/skill/'SKILL.md').read_text(encoding='utf-8')
        validate_skill(text, skill, ('references/hypothesis-contract.md',))
        check((installed/skill/'references/hypothesis-contract.md').is_file(), f'{skill}: installed contract')
    check('resume_from:' in (fresh/'.miraiji/state/current.md').read_text(), 'fresh resume pointer')
    legacy = work/'legacy-home'
    old = legacy/'.bizstack'
    (old/'personas').mkdir(parents=True)
    (old/'state').mkdir()
    (old/'personas/persona-004.md').write_text('# Existing test fixture\nNo personal profile data.\n', encoding='utf-8')
    (old/'state/current.md').write_text('---\nproject: fixture\nnext_skill: pricing\nresume_from: pricing step 3 remaining input\noutput_refs: [~/.miraiji/personas/persona-004.md]\nexternal_action_authorized: false\n---\n', encoding='utf-8')
    original = snapshot(old)
    install(args.bash, distribution, legacy, work/'migration.log')
    new = legacy/'.miraiji'
    check(snapshot(old) == original, 'legacy original preserved')
    for path, digest in original.items():
        check(snapshot(new).get(path) == digest, f'migrated {path} preserved')
    before = snapshot(new)
    install(args.bash, distribution, legacy, work/'repeat.log')
    check(snapshot(new) == before, 'all existing outputs and resume state preserved')
    resumed = (new/'state/current.md').read_text(encoding='utf-8')
    check('pricing step 3' in resumed and (new/'personas/persona-004.md').is_file(), 'resume pointer and referenced output readable')
    # Both roots present: do not merge a legacy record into the established root.
    (old/'personas/persona-099.md').write_text('# Unmerged fixture\n', encoding='utf-8')
    install(args.bash, distribution, legacy, work/'both-roots.log')
    check(not (new/'personas/persona-099.md').exists(), 'both roots are not merged')
    collision = work/'collision-home'
    conflict = collision/'.claude/skills/persona'
    conflict.mkdir(parents=True)
    sentinel = conflict/'keep.txt'
    sentinel.write_text('existing independent installation', encoding='utf-8')
    install(args.bash, distribution, collision, work/'collision.log', expected=2)
    check(sentinel.read_text() == 'existing independent installation', 'collision preserved')
    result = {'zip_format':'PASS','allowlist_and_mit':'PASS','installed_skills_and_references':'PASS',
              'first_install':'PASS','legacy_migration':'PASS','repeat_and_both_roots_preserved':'PASS',
              'collision_protection':'PASS','resume_state_readable_and_instructions':'PASS',
              'actual_agent_conversation':'NOT RUN; these are filesystem and instruction checks',
              'artifacts':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in archives}}
    (work/'results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
