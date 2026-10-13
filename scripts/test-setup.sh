#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEST_ROOT="$(mktemp -d)"
trap 'rm -rf "$TEST_ROOT"' EXIT

TEST_HOME="$TEST_ROOT/home"
mkdir -p "$TEST_HOME/.bizstack/personas"
printf '%s\n' '# Existing persona' > "$TEST_HOME/.bizstack/personas/persona-001.md"

HOME="$TEST_HOME" "$BASH" "$ROOT/setup"

for skill in persona pricing gtm; do
    test -L "$TEST_HOME/.claude/skills/$skill"
    test -f "$TEST_HOME/.claude/skills/$skill/SKILL.md"
done
test -d "$TEST_HOME/.bizstack"
cmp "$TEST_HOME/.bizstack/personas/persona-001.md" "$TEST_HOME/.miraiji/personas/persona-001.md"
grep -Fq 'last_completed: legacy-data-migration' "$TEST_HOME/.miraiji/state/current.md"
grep -Fq 'execution_mode: internal_autorun' "$TEST_HOME/.miraiji/state/current.md"

HOME="$TEST_HOME" "$BASH" "$ROOT/setup"
cmp "$TEST_HOME/.bizstack/personas/persona-001.md" "$TEST_HOME/.miraiji/personas/persona-001.md"

echo '[OK] Miraiji setup exposes all skills and preserves legacy data'
