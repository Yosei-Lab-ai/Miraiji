#!/usr/bin/env python3
"""Build self-contained Phase 1 ZIPs from a public file allowlist."""

import argparse
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {'persona': 'persona.md', 'pricing': 'pricing.md', 'gtm': 'gtm-strategy.md'}


def read(path):
    return (ROOT / path).read_bytes()


def skill_text(skill):
    text = read(f'{skill}/SKILL.md').decode('utf-8')
    source_reference = '../docs/hypothesis-contract.md'
    if source_reference not in text:
        raise ValueError(f'{skill}: shared contract reference is missing')
    return text.replace(source_reference, 'references/hypothesis-contract.md').encode('utf-8')


def write_zip(path, entries):
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (0o100755 if name == 'setup' else 0o100644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, content)


def build(output_dir):
    output_dir = Path(output_dir).resolve()
    if output_dir == ROOT or ROOT in output_dir.parents:
        raise ValueError('Use a temporary output directory outside the repository')
    output_dir.mkdir(parents=True, exist_ok=True)
    shared = read('docs/hypothesis-contract.md')
    bundle = {name: read(name) for name in ('README.md', 'LICENSE', 'VERSION', 'setup')}
    bundle['docs/hypothesis-contract.md'] = shared
    archives = []
    for skill, template in SKILLS.items():
        entries = {
            'SKILL.md': skill_text(skill),
            'references/hypothesis-contract.md': shared,
            f'templates/{template}': read(f'templates/{template}'),
            'LICENSE': read('LICENSE'),
            'VERSION': read('VERSION'),
        }
        entries['README.md'] = f'''# Miraiji /{skill}

This self-contained skill is part of Miraiji's implemented three-skill edition.
It has the same functionality and MIT rights as the free source at
https://github.com/Yosei-Lab-ai/Miraiji . No model subscription, API credits,
paid support, future skills or business outcomes are included or guaranteed.
Agent/model provider access, costs and data handling still apply.

For an authorized local copy, keep SKILL.md and references/ together in
~/.claude/skills/{skill}/ . Preserve any existing installation and saved files.
For Agensi delivery, follow Agensi's agent-connection instructions.
The three-skill local bundle includes a Bash installer for first install,
non-destructive legacy migration and repeat installation.

Outputs are local under ~/.miraiji/; state/current.md records the unfinished
step and output paths. Before questions, read that state and its outputs.
Your agent may process prompts/files through its provider. Miraiji adds no
telemetry. External actions require the user's separate authorization.

See LICENSE for the MIT notice and warranty disclaimer; retain it on redistribution.
'''.encode('utf-8')
        destination = output_dir / f'miraiji-{skill}.zip'
        write_zip(destination, entries)
        archives.append(destination)
        for name in ('SKILL.md', 'references/hypothesis-contract.md'):
            bundle[f'{skill}/{name}'] = entries[name]
        bundle[f'templates/{template}'] = entries[f'templates/{template}']
    destination = output_dir / 'miraiji-phase1.zip'
    write_zip(destination, bundle)
    archives.append(destination)
    return archives


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    for archive in build(args.output_dir):
        print(archive)


if __name__ == '__main__':
    main()
