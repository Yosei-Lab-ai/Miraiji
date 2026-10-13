# Phase 1 ZIP verification

Base commit: `5755353eb777878cefbc77330b6ea34399c46ea9`.
Verified on Windows using existing Git Bash 5.2.37 and Python 3.10.6.

The buyer check built and extracted the final ZIP, installed only persona/pricing/gtm,
and exercised first install, legacy migration, repeat install, both-root handling,
collision protection and saved resume-state preservation.
All existing fixture outputs and the resume pointer remained byte-for-byte unchanged.
The migrated resume pointer and its referenced persona fixture were readable.

The test fixtures contain no real personal profile or approved business decisions.
There were no paid model calls, new authentication, dependency installations,
marketplace uploads, registration, publication or merge.

Actual agent conversation: **not run**. Existing zero-additional-cost agent access
was not confirmed; the resume result covers instructions and filesystem behavior,
not proof of LLM compliance.

| Check | Result |
| --- | --- |
| zip_format | PASS |
| allowlist_and_mit | PASS |
| installed_skills_and_references | PASS |
| first_install | PASS |
| legacy_migration | PASS |
| repeat_and_both_roots_preserved | PASS |
| collision_protection | PASS |
| resume_state_readable_and_instructions | PASS |

## Reviewed artifacts

| File | SHA-256 |
| --- | --- |
| [`miraiji-persona.zip`](../assets/distribution/miraiji-persona.zip) | `d10ae65b5ebfcf34cfa5cbcee41ca215cc41c2d6df658e790b91f322ed9fbf1c` |
| [`miraiji-pricing.zip`](../assets/distribution/miraiji-pricing.zip) | `f4776422587d66caf4cd519747c38fda441b077cce4424e614e03d82650f8d17` |
| [`miraiji-gtm.zip`](../assets/distribution/miraiji-gtm.zip) | `41ba24aae5d439d1c9443174e0262247b0780403a6d7ba968e4b924b71427781` |
| [`miraiji-phase1.zip`](../assets/distribution/miraiji-phase1.zip) | `3340985813d3f4d5545098163eb5feb784481007886ecbfd6f4c0edbc68abfb1` |

## Reproduce

Run from the repository root with a new isolated directory:

```bash
python -B scripts/test-distribution.py --output-dir <new-temporary-directory> --bash <existing-bash>
python scripts/validate-hypothesis-contract.py
bash -n setup scripts/test-setup.sh
```

The buyer test retains logs and a results JSON inside that dedicated directory.
No real user HOME data is used. Live agent behavior remains a separate verification step.
