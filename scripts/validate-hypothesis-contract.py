#!/usr/bin/env python3
"""Validate Miraiji's bounded hypothesis and external-action contract."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: list[str]) -> list[str]:
    text = (ROOT / path).read_text(encoding="utf-8")
    return [f"{path}: missing {needle!r}" for needle in needles if needle not in text]


def main() -> int:
    errors: list[str] = []
    errors += require("setup", ["SKILLS=(persona pricing gtm", "LEGACY_DATA_DIR", ".miraiji", "state/current.md", "internal_autorun", "do not authorize launch"])
    errors += require("scripts/test-setup.sh", ["persona-001.md", "legacy-data-migration", "internal_autorun"])
    contract_fields = [
        "Specific situation",
        "Problem",
        "Promise",
        "Proof status",
        "Riskiest assumption",
        "Timebox",
        "Budget",
        "Pass",
        "Fail",
        "Inconclusive",
        "Stop condition",
        "internal_autorun",
        "external_approval_required",
        "measurement_repair",
        "Experiment record",
        "external_action_authorized: false",
    ]
    errors += require("docs/hypothesis-contract.md", contract_fields)
    for skill in ("persona", "pricing", "gtm"):
        errors += require(f"{skill}/skill.md", ["hypothesis-contract.md", "## Bounded Hypothesis", "## Minimal Test", "internal_autorun", "measurement_repair", "External action authorized:** false"])
    for template in ("persona.md", "pricing.md", "gtm-strategy.md"):
        errors += require(f"templates/{template}", ["## Bounded Hypothesis", "## Minimal Test", "**Execution mode:**", "**Experiment record:**", "**Pass:**", "**Fail:**", "**Inconclusive:**", "**Inconclusive next action:**", "**Stop condition:**"])
    errors += require("ARCHITECTURE.md", ["~/.miraiji/state/current.md", "Evidence-gated decisions"])

    tracked = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in ROOT.rglob("*.md"))
    personal_prefix = "/Users/" + "nakahara" + "shogo/"
    if personal_prefix in tracked:
        errors.append("public Markdown contains a personal absolute path")
    setup_text = (ROOT / "setup").read_text(encoding="utf-8")
    if any(line.strip() == 'DATA_DIR="${HOME}/.bizstack"' for line in setup_text.splitlines()):
        errors.append("legacy data root remains the canonical write target")

    if errors:
        print("[FAIL] Miraiji hypothesis contract")
        for error in errors:
            print(f"- {error}")
        return 2
    print("[OK] Miraiji hypothesis contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
