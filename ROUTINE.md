# ROUTINE — Threads（@atelierbase_own / ひろ｜AI実業家）ストック自動補充

> **Claude Code の Routines（クラウド・スケジュール実行）が無人で実行する標準指示書。**
> 必要な知識はすべて repo 内（`skill/` 配下）に同梱。grok・ローカルスキルには依存しない。

## 役割

**「ストック補充マシン」**。Researcher → Writer を回し `storage/stocks/pending.md` を補充して push。
**配信は GitHub Actions（毎日 JST 07:20 / 12:20 / 19:20）が担当**。このルーティンは投稿しない。
分析＝Analyst は別立て・ローカル（`ANALYSIS.md`）。

## 設定

| キー | 値 | 意味 |
|---|---|---|
| `TARGET_BUFFER` | **9** | pending がこの本数以上なら今回はスキップ |
| `MAX_PER_RUN` | **6** | 1回の生成上限 |
| `CHAR_RANGE` | **200-400字** | Threads 最適 |

## 手順

### Step 1. 残量チェック
`storage/stocks/pending.md` の `## ID` 見出し数を数える。9以上ならスキップ（routine.log 追記 → commit & push → 終了）。9未満なら不足分を生成。

### Step 2. Researcher（ネタ仕入れ）
`skill/agents/researcher.md` に従う。WebSearch のみ。直近1週間の Claude Code / Codex 情報を **Threads特性で選別**（共感・気づき・失敗成功に接続できるもの）。

### Step 3. Writer（投稿生成）
`skill/agents/writer.md` に従う。書く前に必ず：
- `skill/references/00-context.md` / `skill/templates/voice-guide.md` / `skill/references/02-generate.md`（6カテゴリ）
- **`storage/analytics/learnings.md`**（効くルールを毎回反映）

**Threads鉄則**：必ず問いかけで締める／「私の体験」主役＋最新情報セット／絵文字1個・多様化／200-400字／同カテゴリ3連続NG。
**投稿タイプは3種を均等に（各1/3）**：`単発` / `コメント仕込み` / `画像付き`。1回の生成でも全体でも、なるべく各1/3になるよう配分する（例：3本なら各1本。`画像付き`は Step 5 の画像指示を出す）。
時間帯：朝（07-09）/ 昼（11-15）/ 夜（15-23）、足りない枠を優先。

### Step 4. pending.md へ追記
`skill/agents/writer.md` のフォーマットで末尾に追記。キー（`## ID` / `投稿想定時刻` / `ステータス: pending`）は崩さない。

### Step 5. 画像付きを生成した場合
オーナーが ChatGPT(image) で手動生成（Path B）。`storage/analytics/image-requests.md` に指示を追記：
```
## [投稿ID] 画像リクエスト（YYYY-MM-DD）
- 投稿プレビュー: [冒頭]
- GPTに投げるプロンプト: [全文]
- 保存先: storage/images/[投稿ID].png   ← この名前で保存してコミット（Threadsは公開URLで添付するため必須）
```
未配置でも本文のみでフォールバック配信。

### Step 6. ログ → commit & push
`storage/analytics/routine.log` に1行 → `git add -A && git commit -m "routine: stock +N (auto-refill)" && git push`

## 完全無人の原則
- 承認を求めない／生成0でも log を残し push／エラー時は log に残して pending を壊さない

## チェックリスト（push 前）
- [ ] 全投稿が問いかけで締め・一人称「私」・絵文字0〜1個・200-400字
- [ ] 同カテゴリ3連続なし／時間帯の偏りなし
- [ ] learnings.md を反映した
- [ ] 画像付きは image-requests.md に指示を追記した
- [ ] routine.log を更新した
