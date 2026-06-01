# 01-neta: ネタ仕入れ（Threads / v2 / 海外バズ翻訳 + バズパターン調査）

このフェーズの目的は、**直近1週間の海外バズ情報 + Threads バズパターン**を組み合わせて、当週分の投稿ネタリスト（21本分）を作ること。

## 重要な前提

このアカウント「ひろ｜AI実業家」（Threads）は **Claude Code / Codex 特化のニッチ専門アカウント**。
ただし、Threads では **「翻訳された情報」が主役だと伸びない**ことが判明（v2 改訂）。

→ ネタは「海外バズ情報」を取りつつ、訴求は **「私の失敗→AI逆転」「等身大」「マイルストーン」**に振り替える必要がある。

## 入力

なし（オーナーから「Threadsストック作って」「次の7日分」など）

## 出力

ネタ候補リスト（次フェーズ「生成」への入力）。
**1週間分なら 20-21本**（朝7・昼7・夜7、消費済み枠は除く）。

## ステップ

### Step 1. 海外ソースを並列で巡回

**X 用 x-workflow と同じソース**を使う：

#### 必須クエリ4本（毎週）

1. `Anthropic Claude announcement news this week [今週の日付範囲]`
2. `Claude Code update feature release past week [今月]`
3. `OpenAI Codex GPT update news this week [今週の日付範囲]`
4. `Hacker News top AI coding agent trending this week [今月]`

### Step 2. Threads バズパターンの再確認

並行で、直近1週間の **Threads バズパターン** も調査する。
詳細は `references/10-research-method.md` を参照。

**主要な調査方法**:

#### A. WebSearch（5-9クエリ並列）
```
"Threads viral posts examples late [month] [year] what went viral"
"Threads algorithm 2026 what type of post wins engagement"
"Threads 日本 バズ投稿 種類 構成 パターン 2026"
"Threads 日本 フォロワー 増やし方 バズる 投稿 [月] [年]"
"Threads top creators Japan viral hook patterns"
```

#### B. grok-search（X 経由）
```
直近2週間（within_time:14d）で、X(Twitter) 上で
『Threads でバズった』『Threads フォロワー急増』と言及されている
日本語投稿を15件、URL付き・いいね数付きで教えて。
AI系に限定せず、マーケ・ライフスタイル・ビジネス・お金・健康など幅広いジャンルから。
```

#### C. Threads 公式 API（権限承認後）
```bash
curl -G "https://graph.threads.net/v1.0/keyword_search" \
  --data-urlencode "q=Claude Code" \
  --data-urlencode "access_token=$TOKEN"
```

（現状はアプリに `threads_keyword_search` 権限がないため使えない。要申請）

### Step 3. ネタ仕入れの選別基準

X 用と同じ「直近1週間」基準に加え、**Threads 特性を考慮**：

✅ **採用しやすい**:
- 「私の体験と接続しやすい」話題（実用Tips・失敗談・気づき）
- 共感を呼びやすいテーマ
- 「A派？B派？」と意見対立を呼びやすい話題
- マイルストーン・数字に変換しやすい話題

❌ **Threads では避けたい**:
- 抽象的すぎる予測・哲学（読者が「で？」となる）
- 単なる速報（X 向け、Threads では深さが求められる）
- 政治・批判系（Threads ユーザーは穏やかな雰囲気を好む）

### Step 4. ネタを 6カテゴリに振り分け

ネタ仕入れの 21 トピックを、以下の **6カテゴリ・バズパターン** に振り分ける（詳細は `references/02-generate.md`）：

| カテゴリ | 配分 | 役割 |
|---|---|---|
| **失敗→AI逆転型** | 4-5本 | 主力・共感最強 |
| **マイルストーン報告型** | 3-4本 | 数字で信頼 |
| **AI自動化メタ型** | 2-3本 | 同業者向け |
| **X vs Threads比較・哲学** | 1-2本 | プラットフォーム哲学 |
| **バズ後課題提起型** | 1-2本 | 上級者向け |
| **等身大・人間味型** | 4-5本 | オーセンティシティ |

### Step 5. 時間帯への配分

**配分目安**:
- 朝（07-09）: 7本 / マイルストーン・失敗開示中心（出勤前の気持ちセット）
- 昼（11-15）: 7本 / AI自動化メタ・バズ後課題（ランチタイムの知的好奇心）
- 夜（15-23）: 7本 / 等身大・哲学（夜の振り返りモード）

### Step 6. 各ネタにメタ情報をつける

各ネタは以下の構造で記録：

```
- トピック: [何の話か]
- 元ソース: [どこから取った情報か：URL/媒体名]
- 直近性: [いつ発表されたか・◯月◯日]
- バズパターン: [失敗→AI逆転 / マイルストーン / AI自動化メタ / X比較 / バズ後課題 / 等身大]
- 想定時間帯: 朝 / 昼 / 夜
- 私の実体験フック: [自分の使用例とどう繋げられるか]
- 想定問いかけ: [意見対立 or 共感誘発の質問]
```

## 主要ソース一覧

| ソース | URL | 特徴 |
|---|---|---|
| **Anthropic News** | https://www.anthropic.com/news | Claude / Claude Code の公式発表 |
| **OpenAI News** | https://openai.com/news/ | GPT / Codex の公式発表 |
| **Claude Code Docs / Changelog** | https://code.claude.com/docs/en/whats-new | Claude Code リリースノート |
| **Codex Changelog** | https://developers.openai.com/codex/changelog | Codex リリースノート |
| **Hacker News** | https://news.ycombinator.com/ | 開発者の議論・バイラル記事 |
| **Reddit r/ClaudeAI** | https://reddit.com/r/ClaudeAI | Claude 周辺コミュニティ |
| **Indie Hackers** | https://www.indiehackers.com/ | 個人開発者の事例 |
| **Threadify バイラル分析** | https://www.threadify.app/blog/viral-threads-analysis | Threads バズ500件分析 |

## X 用ネタとの差分

x-workflow と同じネタを Threads 用に使う場合：

1. **同じネタを使ってOK**（効率的）
2. **訴求文は別途構成**（コピペ NG）
3. Threads では：
   - 「私の体験」を主役に
   - 必ず問いかけで締める（意見対立型）
   - 絵文字1個を内容に合わせて多様化
   - 文字数 280→500 まで活用OK
   - **6カテゴリのいずれかに振り分ける**

## 出力フォーマット

```markdown
# Threads ネタリスト YYYY-MM-DD（直近1週間: YYYY-MM-DD 〜 YYYY-MM-DD）

## A. 失敗→AI逆転型候補（4-5本）

1. **[トピック名]**
   - 元ソース: [URL/媒体]
   - 想定時間帯: 朝
   - 私の失敗エピソード: [具体的に]
   - AI で逆転した瞬間: [具体的に]
   - 想定問いかけ: 「皆さんも、AI に救われた瞬間ってありますか？」

## B. マイルストーン報告型候補（3-4本）
...

## C. AI自動化メタ型候補（2-3本）
...

## D. 等身大・人間味型候補（4-5本）
...

## E. その他（X比較・バズ後課題）
...
```

## 後処理

ネタリストを `~/atlier-base-v1/projects/sns-auto-post/threads/storage/stocks/drafts.md` に追記。
次フェーズ「生成」でこれを元に投稿文を作成。

## 注意

- X 用と同じネタを使うのは効率的だが、**訴求文は別途**書く
- Threads は「対話・共感」が命。情報伝達だけで終わらない
- 21本 = 21トピックで十分。同じトピックで複数本書かない
- 6カテゴリのバランスを必ず確認（同カテゴリ連続NG）

## 履歴

- v1（2026-05-26）: 初版（X 用 01-neta.md をベースに Threads 特性を反映）
- **v2（2026-05-27）**: 6カテゴリ・バズパターン設計を反映、調査方法を強化（**現行版**）
