# 09-github-actions: Threads 自動配信運用（GitHub Actions）

このスキルは GitHub Actions で Threads 自動投稿を実行する設計。
PC の起動状態に関係なく、クラウド側で 24 時間動く。

## アーキテクチャ

```
[ローカル: Claude セッション]
   ↓ /threads-workflow ネタ → /threads-workflow 生成
[Claude が pending.md にストック追加]
   ↓ git push（私が代行 or オーナーが実行）
┌────────────────────────────────────────────────┐
│ GitHub: atelierbase/threads-workflow-atelier   │
│  pending.md ← 真実のソース                     │
└────────────────────────────────────────────────┘
   ↓ オーナーが GitHub UI で内容確認・編集（任意）
   ↓ 毎日 JST 07:00 / 12:00 / 19:00
[GitHub Actions ワークフロー実行]
   ↓ scripts/threads_poster.py
[Threads API v1 で投稿（コンテナ作成 → publish）]
   ↓ commit & push
[posted.md 更新、pending.md から削除]
```

## 主要設定値

| 項目 | 値 |
|---|---|
| リポジトリ | https://github.com/atelierbase/threads-workflow-atelier |
| ワークフロー | `.github/workflows/scheduled-post.yml` |
| 投稿スクリプト | `scripts/threads_poster.py` |
| Secrets | `THREADS_ACCESS_TOKEN` / `THREADS_USER_ID` |
| スケジュール | JST 07:00 / 12:00 / 19:00（cron UTC 22:00, 03:00, 10:00） |
| ジッター | ±15分 |
| 文字制限 | 500字 |

## オーナーと秘書（Claude）の役割分担

| ステップ | 秘書（Claude） | オーナー |
|---|---|---|
| 1. ネタ仕入れ | ◯（海外ソース巡回） | 素材提供 |
| 2. 投稿生成 | ◯（21本まとめて・Threads特性） | - |
| 3. ストック追加（pending.md） | ◯（ローカル → git push） | - |
| 4. **内容確認** | （提示） | ◯ **GitHub UI で見る** |
| 5. **編集・微調整** | リライト提案 | ◯ **GitHub UI で直接編集** |
| 6. 配信実行 | - | GitHub Actions が自動 |
| 7. 数値分析 | ◯（週次） | データ提供 |

## 運用サイクル

### 7日ごと（ストック切れ前）

1. 残ストック数を確認（pending.md のエントリ数）
2. オーナーから「最近の活動・気づき」をヒアリング
3. 21本（1日3本 × 7日）を生成
4. ローカルの `~/atlier-base-v1/threads-workflow-repo/storage/stocks/pending.md` に追記
5. `git push` で GitHub に反映
6. オーナーが **GitHub UI で内容確認 → 必要なら直接編集 → commit**

### 毎日（自動）

- JST 07:00 朝枠投稿（±15分のジッター）
- JST 12:00 昼枠投稿
- JST 19:00 夜枠投稿
- 各時間帯ごとに pending.md の該当ストックを1本消費

### 週次（金 or 土）

- posted.md で振り返り
- 伸びた投稿の特徴抽出（問いかけが効いたか・絵文字の効果など）
- 次の生成方針に反映

## 編集フロー

### GitHub UI で確認・編集

🔗 https://github.com/atelierbase/threads-workflow-atelier/blob/main/storage/stocks/pending.md

手順：
1. 上記 URL を開く
2. 右上の **✏️ 鉛筆アイコン** クリック
3. 編集
4. "**Commit changes**" → 確定

→ 次回の自動配信から反映される。

### 編集時の制約

- ストックの ID フォーマット `## YYYY-MM-DD-NNN` は変えない
- `投稿想定時刻: 朝/昼/夜` は保持（スクリプトの判定キー）
- `- ステータス: pending` の行は消さない
- 本文は **500 文字以内**（Threads 仕様）
- 一人称「私」・絵文字 1個・問いかけ必須を維持

## 緊急で投稿を入れたい

ストックは時間帯フィルタの先頭から消費されるので、緊急投稿は ID を当日大番号で：

```markdown
## 2026-05-26-999
- 種類: 単発
- 投稿想定時刻: 夜（15:00-23:00）
- 軸: 緊急
- 文面:

[緊急投稿の本文]

- ステータス: pending

---
```

これを pending.md の先頭付近に挿入してコミットすれば、次の「夜」枠で最優先で投稿される。

## トラブルシューティング

### 投稿されなかった

1. **Actions タブで失敗していないか**
   - https://github.com/atelierbase/threads-workflow-atelier/actions

2. **scheduler.log を確認**
   - https://github.com/atelierbase/threads-workflow-atelier/blob/main/storage/analytics/scheduler.log

3. **よくある原因**
   - 該当時間帯のストックがない
   - 500文字オーバー
   - access_token 期限切れ・revoke

### Threads bio / プロフが反映されない

これは GitHub Actions の管轄外（Threads アプリ側で設定する必要）。

### Free 枠の上限が近い

Threads API は標準で 250 投稿/24時間/ユーザー。1日3投稿だと余裕（上限の1%程度）。

## ワークフロー手動トリガー

緊急で投稿したいときや、テストしたいとき：

```bash
gh workflow run scheduled-post.yml -R atelierbase/threads-workflow-atelier
```

または、Actions タブで「Run workflow」ボタン。

## 関連ファイル

- `references/04-distribute.md` — 配信モード詳細
- `references/02-generate.md` — 生成フロー
- `references/03-stock.md` — ストック管理
- `templates/voice-guide.md` — Threads 用口調ガイド

## 履歴

- 2026-05-26 v1: 初版（X 用 09-github-actions.md を Threads 用に複製・調整）
