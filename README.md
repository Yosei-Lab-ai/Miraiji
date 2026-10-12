# Miraiji

Business design skills for Claude Code: define a target user, design pricing,
and plan how to reach users. Outputs are decision inputs and hypotheses;
they do not guarantee business outcomes.

## Available skills

| Command | Output |
| --- | --- |
| `/persona` | Target-user persona, evidence status and bounded validation test |
| `/pricing` | Pricing design, break-even assumptions and billing/limit requirements |
| `/gtm` | Positioning, channel priorities and first-100-users strategy |

Only these three skills are implemented, installed and packaged. Other skill
directories in the source repository are Coming soon and are excluded from the
distribution. Launch planning does not execute publication or outreach.

## Requirements and costs

Use an existing Claude Code environment that can read and write local files.
The installer requires Bash and symbolic links on macOS/Linux; on Windows use
Git Bash with `cmd.exe`, `powershell.exe` and `cygpath` for directory junctions.
The source installer and local distribution need no additional Python or npm
packages. Building and testing ZIPs requires Python 3.9+ (standard library only).
gstack and Miragoe are optional integrations, not prerequisites for these skills.

Miraiji includes no model, agent subscription or API credits. Your chosen agent
and model provider's access requirements, limits, fees and data handling still
apply. No paid model call is needed for the local packaging/setup tests.

## Local installation

For an authorized local distribution, extract `miraiji-phase1.zip` to a permanent
folder, open Bash there, and run:

```bash
bash setup
```

Keep that folder in place: installed commands link to it. Do not copy only the
SKILL.md files; their `references/` folders must stay with them. If a command
directory already belongs to another installation, setup stops without replacing
it. Resolve that collision explicitly; do not delete another user's skills.
Rerunning setup from the same folder preserves saved data and resume state.

The free source installation uses the same command:

```bash
git clone https://github.com/Yosei-Lab-ai/Miraiji.git
cd Miraiji
bash setup
```

Source skills reference `../docs/hypothesis-contract.md` relative to their physical
repository directory. Packaged skills carry that contract in `references/`.
If Agensi delivers a skill through its agent connection, follow Agensi's delivery
instructions; the local ZIP workflow is for authorized local copies.

## Saved work and resume

Outputs live in `~/.miraiji/personas/`, `pricing/`, `gtm/` and `experiments/`.
The current pointer is `~/.miraiji/state/current.md`. To continue, invoke the
recorded skill and ask it to resume the saved project. Each skill instructs the agent to read that
pointer and the referenced files before asking questions, then continue the
unfinished step. Missing or ambiguous records trigger a specific question rather
than invented answers. A new project or fresh interview requires your request.

On first install, if `~/.bizstack/` exists and `~/.miraiji/` does not, setup copies
the old data and preserves the original. If both exist, it reports the conflict
without merging. Existing files and saved resume pointers are not overwritten.
Saved plans or approval flags do not authorize posting, messages, purchases,
account changes or customer-facing price changes.

## Privacy

Miraiji saves outputs locally and adds no telemetry or separate network service.
Your chosen agent may send prompts or file contents to its model provider under
that provider's settings and terms. Review those before using confidential data.
User outputs, credentials and internal repository tooling are excluded from the
distribution by an explicit file allowlist.

## Free MIT source and packaged edition

The free source and packaged edition contain the same three implemented skills.
The packaged edition adds installation/packaging documentation and bundled
references; it does not add exclusive functionality or revoke MIT rights.
The source remains available at [Yosei-Lab-ai/Miraiji](https://github.com/Yosei-Lab-ai/Miraiji).
Any listing fee or separately stated support service does not change the MIT
permission to use, copy, modify and redistribute the included software.
No paid support or future skill delivery is promised by this repository.

## License

MIT. Copyright (c) 2026 Yosei Lab. See `LICENSE` for the complete permissions
and warranty disclaimer. Include that notice when redistributing copies.
