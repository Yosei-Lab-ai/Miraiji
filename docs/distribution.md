# Phase 1 distribution

Build with Python 3.9+ and no additional packages:

```bash
python scripts/build-distribution.py --output-dir /absolute/temporary/output
python scripts/test-distribution.py --output-dir /absolute/temporary/buyer-check --bash /path/to/bash
```

Use an isolated temporary output directory. The buyer check retains its evidence
and writes only its own fixture HOME; it never uses the real user's data directories.

The builder creates `miraiji-phase1.zip` and three individually self-contained
submission ZIPs (`miraiji-persona.zip`, `miraiji-pricing.zip`, `miraiji-gtm.zip`).
Each individual ZIP has a root `SKILL.md`, valid name/description frontmatter,
its shared contract under `references/`, a template, README, VERSION and LICENSE.
The bundle includes setup and only the three implemented skill directories.
It replaces the source-relative contract link with the packaged relative link.

The allowlist excludes Git history, internal settings/hooks, roadmap stubs,
test fixtures, user outputs, credentials and all unlisted files. Do not submit a
raw repository archive. Review the final ZIPs and listing before any upload.

The buyer check builds and extracts those ZIPs, checks their exact entries and
references, then exercises first install, legacy migration, repeat install,
collision protection and saved-state preservation. It also checks the explicit
resume instructions. These checks do not prove that an LLM agent follows those
instructions in a live conversation. A live agent test must be recorded separately
and must not introduce unapproved fees or transmit private user data.

The reviewed ZIPs are retained under `assets/distribution/` for PR inspection.
Submit an individual skill ZIP where Agensi requires one root SKILL.md.
The three-skill `miraiji-phase1.zip` is the authorized local installation bundle,
not a fourth skill or a single-skill marketplace submission.
See `distribution-test-results.md` for the checked ZIP hashes and test limits.
