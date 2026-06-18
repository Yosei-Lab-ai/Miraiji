#!/usr/bin/env python3
"""Code-First Defense 構造ガード (全社リストラ Phase2 S5).

staged のコード/設定ファイルに対し、構造散乱の再発パターンを物理 block する:
  (1) /Users/<user>/ のハードコード絶対パス — 拠点(Win/Mac)間で壊れる。repo 相対 or env へ
  (2) 停滞モノレポコピー OreInc/<事業部> への参照 — 二重管理の能動再生産
      (本物は ~/<事業部> もしくは GitHub。update_rankings.py 事故の再発防止)

対象は コード/設定ファイルのみ (.md ドキュメントは所在を正規に記述するため除外)。
行末に 'allow-structure-guard' コメントを付ければ、その行のみ許可 (正当な例外用)。

pre-commit から staged filename を受け取って実行 (pass_filenames: true)。
"""
from __future__ import annotations

import re
import sys

CODE_EXTS = {
    ".py", ".sh", ".bash", ".zsh", ".js", ".mjs", ".cjs", ".ts", ".tsx",
    ".yaml", ".yml", ".toml", ".cfg", ".ini", ".bat", ".ps1",
}

# 自己マッチ回避のためユーザ名を分割構築 (この検査スクリプト自身が引っかからないように)
_USER = "nakahara" + "shogo"
ABS_PATH = re.compile(r"/Users/" + _USER + r"/")

_DIVISIONS = [
    "Dev", "AGT", "POS", "Cyrus_Coffee_Lab", "fanza-auto",
    "sns-tool", "bizstack", "Lifestack", "migration-subsidy-app",
]
# 大文字 "OreInc/<division>" のみ対象 (repo 名 "oreInc-governance" は小文字始まりで非該当)
STALE_COPY = re.compile(r"OreInc/(?:" + "|".join(_DIVISIONS) + r")(?:/|\b)")

ALLOW_MARK = "allow-" + "structure-guard"


def _ext(path: str) -> str:
    return path[path.rfind("."):] if "." in path.rsplit("/", 1)[-1] else ""


def check_file(path: str) -> list[str]:
    if _ext(path) not in CODE_EXTS:
        return []
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.readlines()
    except (OSError, IsADirectoryError):
        return []
    errs: list[str] = []
    for n, line in enumerate(lines, 1):
        if ALLOW_MARK in line:
            continue
        if ABS_PATH.search(line):
            errs.append(
                f"{path}:{n}: ハードコード絶対パス /Users/<user>/ — 拠点間で壊れる。"
                f"repo 相対 or env へ (例外は行末に '{ALLOW_MARK}')"
            )
        if STALE_COPY.search(line):
            errs.append(
                f"{path}:{n}: 停滞モノレポコピー OreInc/<事業部> 参照 — 二重管理の再生産。"
                "本物 ~/<事業部> もしくは GitHub を参照せよ"
            )
    return errs


def main(argv: list[str]) -> int:
    all_errs: list[str] = []
    for path in argv:
        all_errs.extend(check_file(path))
    if all_errs:
        print("Code-First Defense 構造ガード 違反 (Phase2 S5):", file=sys.stderr)
        for e in all_errs:
            print("  - " + e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
