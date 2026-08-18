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
    errors += require("setup", ["SKILLS=(persona pricing gtm", ".miraiji", "state/current.md", "do not authorize launch"])
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
        "external_action_authorized: false",
    ]
    errors += require("docs/hypothesis-contract.md", contract_fields)
    for skill in ("persona", "pricing", "gtm"):
        errors += require(f"{skill}/skill.md", ["hypothesis-contract.md", "## Bounded Hypothesis", "## Minimal Test", "External action authorized:** false"])
    for template in ("persona.md", "pricing.md", "gtm-strategy.md"):
        errors += require(f"templates/{template}", ["## Bounded Hypothesis", "## Minimal Test", "**Pass:**", "**Fail:**", "**Inconclusive:**", "**Stop condition:**"])
    errors += require("ARCHITECTURE.md", ["~/.miraiji/state/current.md", "Evidence-gated decisions"])

    tracked = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in ROOT.rglob("*.md"))
    personal_prefix = "/Users/" + "nakahara" + "shogo/"
    if personal_prefix in tracked:
        errors.append("public Markdown contains a personal absolute path")
    if "~/.bizstack" in tracked:
        errors.append("legacy data root remains in public Markdown")

    if errors:
        print("[FAIL] Miraiji hypothesis contract")
        for error in errors:
            print(f"- {error}")
        return 2
    print("[OK] Miraiji hypothesis contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
