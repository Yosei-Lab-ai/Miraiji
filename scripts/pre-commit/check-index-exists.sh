#!/usr/bin/env bash
# Code-First Defense (全社リストラ Phase2 S5-d): repo ルートに INDEX.md(所在地図) を必須化。
# CLAUDE.md 規定の確認チェーン「INDEX.md → scripts/README.md → docs/」の先頭を物理担保。
# 「探す→見る」恒久転換のため、地図不在の repo を commit させない。
set -uo pipefail

root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
if [ ! -f "$root/INDEX.md" ]; then
  echo "INDEX.md がリポジトリルートに存在しません (Phase2 S5-d):" >&2
  echo "  → この repo の所在地図 INDEX.md を新設せよ(本物の所在/主要dir/成果物置き場)。" >&2
  echo "  「探す→見る」の物理担保。CLAUDE.md 確認チェーンの先頭。" >&2
  exit 1
fi
exit 0
