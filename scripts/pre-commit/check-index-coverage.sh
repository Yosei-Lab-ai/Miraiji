#!/usr/bin/env bash
# Code-First Defense (全社リストラ Phase2 S5): 地図ドリフト防止。
# トップレベルの tracked/staged dir が INDEX.md に記載されているかを物理担保。
# 新しい dir をルートに追加したのに INDEX 未記載 → commit を block。
# 「地図を更新し忘れて腐る」(今回の散乱の根本原因)を構造的に封じる。
set -uo pipefail

root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$root" || exit 0
[ -f INDEX.md ] || exit 0   # INDEX 不在は check-index-exists が担当

# トップレベルの dir 名(staged 含む・dotfile 除外)。CJK/特殊文字 path の quote を抑止
dirs=$(git -c core.quotepath=false ls-files | awk -F/ 'NF>1 {print $1}' | sort -u | grep -v '^\.')

missing=""
while IFS= read -r d; do
  [ -z "$d" ] && continue
  # 末尾スラッシュ付きで照合(security/ が security-reports/ に誤マッチしない)
  grep -qF "$d/" INDEX.md || missing="${missing}${d}"$'\n'
done <<< "$dirs"

if [ -n "$missing" ]; then
  echo "INDEX.md にトップレベル dir の記載が不足 (地図ドリフト防止 S5):" >&2
  printf '%s' "$missing" | sed '/^$/d; s/^/  - /' >&2
  echo "→ INDEX.md「本店ルート直下の主要物の所在」表に追記してから commit せよ。" >&2
  echo "  地図(INDEX)は構造変更と同時に更新する=「探す→見る」の恒久担保。" >&2
  exit 1
fi
exit 0
