# 03-stock: ストック管理（Threads）

このフェーズの目的は、生成 → 承認された投稿を**配信タイミングまで安全に保管**し、**配信状況を追跡可能**にすること。

## ファイル構造とデータの真実のソース

**重要**: 現運用（GitHub Actions）では、**真実のソースは GitHub 上**にある。

| 場所 | パス | 役割 |
|---|---|---|
| **GitHub（真実のソース）** | `atelierbase/threads-workflow-atelier/storage/stocks/` | GitHub Actions が直接読む |
| ローカル（作業バッファ） | `~/atlier-base-v1/threads-workflow-repo/storage/stocks/` | 私が生成 → push する場所 |
| スキル内（参考） | `~/.claude/skills/threads-workflow/storage/stocks/` | スキル定義の一部・参考 |

### 各ファイル

```
storage/stocks/
├── pending.md  # 承認済み・未投稿（GitHub Actions が消費）
├── posted.md   # 投稿済み + thread_id ログ
└── drafts.md   # 起案中・没・ネタメモ
```

## pending.md フォーマット（Threads 用）

```markdown
# ストック（Threads / 未投稿）

最終更新: YYYY-MM-DD

---

## 2026-05-27-001
- 種類: 単発
- 投稿想定時刻: 朝（07:00-09:00）
- 想定日: 2026-05-27（火）
- 軸: 海外翻訳 / Claude Code Tips
- ソース: Anthropic 公式ガイド
- 絵文字: 💡（Tips）
- 文面:

[全文・500字以内]

- ステータス: pending

---
```

ID命名規則: `YYYY-MM-DD-NNN`（同日内の通番）

## posted.md フォーマット（Threads 用）

```markdown
# 投稿済みログ（Threads）

---

## 2026-05-27-001（Threads自動配信 / GitHub Actions）
- プラットフォーム: Threads
- 投稿日時: 2026-05-27T07:14:32+09:00
- 配信モード: api（GitHub Actions + Threads API）
- thread_id: 18393912259083839
- URL: https://www.threads.com/@atelierbase_own/post/18393912259083839
- 文面:

[全文]

- ステータス: posted
- 数値（24h時点）: いいね xx / リプ xx / 引用RT xx
- 数値（7d時点）: いいね xx / リプ xx / 引用RT xx
- 所感: [伸びた / 普通 / 不調] - [理由仮説]

---
```

## drafts.md フォーマット

```markdown
# 起案中・没・メモ（Threads）

---

## 起案中（要オーナー承認）

### draft-001
- 種類: 単発
- 文面: ...
- ステータス: 要承認

---

## 没（参考用に残す）

### killed-001
- 没理由: 問いかけが弱い
- 文面（参考）: ...

---

## ネタメモ（未着手）

- [メモ1]
- [メモ2]

---
```

## 操作

### ストック残量確認

`pending.md` のエントリ数をカウント。

- 残10本以上: 余裕
- 残5-9本: 通常
- 残3-4本: 注意。次回ネタ仕入れを推奨
- 残2本以下: ⚠️ 緊急。即ネタ仕入れ＋生成

### ストック追加

新規ストックは `pending.md` の末尾に追加 → git push。
GitHub UI でもオーナーが直接編集可能。

### ストックから取り出し（配信時）

GitHub Actions が `threads_poster.py` で：
1. `pending.md` から該当時間帯の最初のエントリを取り出し
2. Threads API で投稿
3. `posted.md` に追加
4. `pending.md` から削除
5. コミット & プッシュ

### リライト

GitHub UI で編集が最速。私が編集する場合は git pull → 編集 → push。

### 緊急差し込み

トレンド乗りなどで即時投稿したいときは、`pending.md` の先頭に挿入。
スクリプトは ID 順ではなく **時間帯フィルタの先頭から**取るので、ID の数字を当日大番号にする：

```markdown
## 2026-05-26-999
- 投稿想定時刻: 夜（15:00-23:00）
...
```

これを pending.md の先頭エントリの直前に挿入してコミット。

## ストック健全性ルール

1. **同日に種類が偏らない**: 1日3本のうち、主軸1・サブ軸1・サブ軸2 のように
2. **時間帯がバラける**: 朝・昼・夜が混ざるように
3. **絵文字が連続しない**: 同じ絵文字を3投稿連続NG
4. **テーマ配分（主軸60% / サブ25% / サブ15%）を維持**
5. **ストック0は絶対避ける**: 残3本切ったらアラート
6. **古すぎるストックは見直し**: 2週間以上未投稿のものは、文脈ズレで没になる可能性

## storage の初期化

初回利用時は `references/07-setup.md` の手順で初期化する。

## 注意

- GitHub Actions が読むのは GitHub 上のファイル。ローカルだけ更新しても反映されない
- pending.md / posted.md の同期は git pull / push で
- 値そのもの（access_token など）は絶対にここに書かない（credentials.json で管理）
- Threads API の `thread_id` は数字の長い文字列（保存して後で URL 構築）

## 関連

- 配信フロー: `references/04-distribute.md`
- GitHub Actions: `references/09-github-actions.md`

## 履歴

- v1（2026-05-26）: 初版（X 用 03-stock.md を Threads 用に複製・調整）
