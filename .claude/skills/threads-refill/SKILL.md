---
name: threads-refill
description: Threads（@atelierbase_own / ひろ｜AI実業家）のストック自動補充スキル。pending.md が9本未満なら researcher→writer を回して不足分を生成し pending.md へ追記、routine.log を更新して commit & push する。クラウドルーチンが無人実行する用。トリガー：「Threadsストック補充」「threads-refill」または /threads-refill。
---

# threads-refill — Threads ストック自動補充（無人）

このスキルは Threads アカウント @atelierbase_own（「ひろ｜AI実業家」/ 屋号 Atelier Base）の**ストック補充マシン**。
Researcher → Writer を回して `storage/stocks/pending.md` を補充し、commit & push する。
**配信は GitHub Actions（JST 07:20/12:20/19:20）が担当。このスキルは投稿しない。** 分析（Analyst）は別立て・ローカル。

> 詳細仕様はリポジトリの `ROUTINE.md` が正。このスキルはその実行手順をスキルとして発動可能にしたもの。

## 完全無人の原則
- 途中で人間に承認を求めない（クラウド実行なので止まると失敗扱い）
- 生成0でも `storage/analytics/routine.log` を残して push する
- エラー時も `pending.md` は壊さず log に残して終了

## 設定
| キー | 値 | 意味 |
|---|---|---|
| TARGET_BUFFER | 9 | pending がこの本数以上ならスキップ |
| MAX_PER_RUN | 6 | 1回の生成上限 |
| CHAR_RANGE | 200-400字 | Threads 最適 |

## 手順

### Step 1. 残量チェック
`storage/stocks/pending.md` の `## ID` 見出し数を数える。
- **9以上** → 生成不要。`storage/analytics/routine.log` に `skip: pending=N` を追記して **commit & push して終了**。
- **9未満** → 不足分 `(9 - 現在数)`（上限 `MAX_PER_RUN`）を生成。

### Step 2. Researcher（ネタ仕入れ）
**`researcher` サブエージェントが使えるなら Task で委譲**、使えなければメインが直接実行する。
`skill/agents/researcher.md` の定義に従い、**WebSearch のみ**（grok・ローカルスキル不可）で直近1週間の海外 Claude Code / Codex 情報を収集し、**Threads特性（共感・気づき・失敗成功に接続できるもの）で選別** → ネタリスト。

### Step 3. Writer（投稿生成）
**`writer` サブエージェントが使えるなら Task で委譲**、使えなければメインが直接実行する。
書く前に必ず読む：
- `skill/references/00-context.md` / `skill/templates/voice-guide.md` / `skill/references/02-generate.md`
- **`storage/analytics/learnings.md`**（効くルールを毎回反映＝学習の複利）

**Threads鉄則**：必ず問いかけで締める／「私の体験」主役＋最新情報セット／一人称「私」／絵文字1個・多様化／**200-400字**／同カテゴリ3連続NG。
**投稿タイプを混ぜる**：基本=`単発` / `コメント仕込み`を1日1本目安 / `画像付き`を時々。時間帯（朝/昼/夜）の足りない枠を優先。

### Step 4. pending.md へ追記
`skill/agents/writer.md` のフォーマットで末尾に追記（既存は消さない）。
キー `## ID` / `投稿想定時刻` / `- ステータス: pending` は崩さない。
画像付きを作った場合は本文ブロックに `- 画像ファイル: storage/images/<投稿ID>.png` を必ず入れる。

### Step 5. 画像付きを生成した場合
`storage/analytics/image-requests.md` にオーナー向け画像指示を追記（投稿ID・本文プレビュー・GPTプロンプト全文・保存先 `storage/images/<投稿ID>.png`）。
Threads は公開URLで添付するため、画像は commit & push されて初めて添付可能（未配置なら本文のみフォールバック）。

### Step 6. ログ → commit & push
1. `storage/analytics/routine.log` に `YYYY-MM-DD HH:MM JST | generated N | pending 旧→新` を追記
2. `git add -A && git commit -m "routine: stock +N (auto-refill)" && git push`

## チェックリスト（push 前）
- [ ] 全投稿が問いかけで締め・一人称「私」・絵文字0〜1個・200-400字
- [ ] 同カテゴリ3連続なし／時間帯の偏りなし
- [ ] 直近1週間のフレッシュネタ（発表時期を確認）
- [ ] learnings.md を反映した
- [ ] 画像付きがあれば image-requests.md に指示を追記＋本文に画像ファイル行を入れた
- [ ] routine.log を更新した
