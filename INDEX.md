# Miraiji INDEX — まず「探す」前にここを見る

> 「どこに何があるか」の単一の地図。grep で探す前にここを見ること。確認順: **INDEX.md → README.md → docs/**。
> 最終更新: 2026-06-18 (oreInc-governance#247 Code-First Defense ガード横展開で新設)。
> トップレベル dir を増やしたら**本書を同時更新**する(pre-commit `index-coverage` が物理担保)。

## 役割
スキルパック **Miraiji**(旧 bizstack) — Claude Code 向けビジネススキルパック。
「gstack はコードを出荷する、Miraiji はそれをユーザーに届ける」。gstack を**拡張**する位置づけ。各トップ dir が 1 つのスキル。

## 本物(canonical)
- **SSOT = GitHub `Yosei-Lab-ai/Miraiji`**(repo 改名済・ローカル dir 名は旧 `bizstack`)。default branch=`main`。
- モノレポへの実体焼き込み(二重管理)は禁止。GitHub を唯一の真実とする。

## トップレベル dir の所在地図(各 dir = スキル)
| dir | スキル/中身 |
|---|---|
| `market-scan/` | 市場スキャン・競合調査 |
| `persona/` | ペルソナ設計 |
| `pricing/` | 価格設計 |
| `bizplan/` | 事業計画 |
| `gtm/` | Go-To-Market 戦略 |
| `launch/` | ローンチ実行 |
| `outreach/` | アウトリーチ/獲得 |
| `content/` | コンテンツ施策 |
| `grow/` | グロース |
| `measure/` | 計測・KPI |
| `feedback/` | 顧客フィードバック |
| `biz-retro/` | 事業振り返り |
| `templates/` | スキル共通テンプレート |
| `docs/` | スキルパック設計・仕様 |
| `scripts/` | 補助スクリプト + `pre-commit/`(構造ガード4種) |

(`.github/` `.claude/` 等の dotdir は地図対象外)

## Pre-commit セットアップ (clone 後・マシンごとに 1 回)
```bash
pip install pre-commit
pre-commit install            # git hook 登録 (以後 commit 時に自動実行)
pre-commit run --all-files    # 単発フルスキャン
```
稼働ガード(正典 = `oreInc-governance` / 本 repo `scripts/pre-commit/` は vendor):
- **structure-guard** — `/Users/<user>/` 絶対パス・`OreInc/<事業部>` 停滞コピー参照を block(例外は行末 `allow-structure-guard`)
- **no-nested-git** — repo 内 repo(野良 nested `.git`)を block
- **index-exists** — ルートに `INDEX.md`(本書)必須
- **index-coverage** — 新トップレベル dir を本書に追記しないと block(地図ドリフト防止)

ローカル install を省いても CI(`.github/workflows/pre-commit.yml`)が PR で同ガードを走らせる。

## 成果物を作ったら(再発防止)
新しくトップレベル dir / 生成物を作ったら、**本書の地図表に1行追記**してから commit する。
ブランチに置き去りにせず、どこに置いたかを必ず明示する。
