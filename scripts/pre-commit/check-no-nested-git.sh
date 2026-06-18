#!/usr/bin/env bash
# Code-First Defense (全社リストラ Phase2 S5): nested .git = repo 内 repo の禁忌を block。
# feedback_nested_repo_taboo / claude-config 事故の再発防止。
#
# 許可するもの:
#   - 登録済み submodule (.gitmodules に path 登録) — 正規の参照
#   - git worktree (.claude/worktrees/ 配下)
#   - 暫定 allowlist (処分予定の既知 nested。解消後にここから外す)
# それ以外の野良 nested .git は block。
set -uo pipefail

root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$root" || exit 0

# 暫定 allowlist: Phase で処分予定の既知 nested repo (解消後に削除)
ALLOWLIST="claude-config"

# 登録済み submodule パス
subs=""
if [ -f .gitmodules ]; then
  subs=$(git config -f .gitmodules --get-regexp '^submodule\..*\.path$' 2>/dev/null | awk '{print $2}')
fi

is_allowed() {
  local d="$1" s
  for s in $subs;      do [ "$d" = "$s" ] && return 0; done
  for s in $ALLOWLIST; do [ "$d" = "$s" ] && return 0; done
  return 1
}

bad=""
while IFS= read -r g; do
  [ -z "$g" ] && continue
  d="${g%/.git}"; d="${d#./}"
  is_allowed "$d" || bad="${bad}${d}"$'\n'
done < <(find . -name .git -not -path './.git' -not -path './.git/*' \
              -not -path '*/.claude/worktrees/*' -not -path '*/node_modules/*' 2>/dev/null)

if [ -n "$bad" ]; then
  echo "nested .git 検出 (repo 内 repo 禁忌・feedback_nested_repo_taboo):" >&2
  printf '%s' "$bad" | sed '/^$/d; s/^/  - /' >&2
  echo "→ submodule 化 (.gitmodules 登録) するか、隣 dir へ mv + .gitignore せよ" >&2
  exit 1
fi
exit 0
