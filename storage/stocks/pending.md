# 受け渡しキュー（Threads / image2生成済み画像 / 定期投稿）

このファイルは **image2で生成したPNG + 投稿文 → GitHub Actions の受け渡し場所**。
`storage/images/{投稿ID}.png` に画像を置き、このファイルに同じ投稿IDの画像付き投稿を積む。
GitHub Actions（送信専用）が該当スロットで Threads へ投稿して posted.md に移すと、ここは再び空になる。

- GitHub Actions は画像を生成しない。画像は必ず ChatGPT image2 で作成してから置く。
- ここに長く残る投稿があれば「送信ワークフローが動いていない」または「該当スロット待ち」のサイン。
- 旧来の事前ストックは `archive/pending-pre-directpost-2026-06-03.md` に退避済み。
- フォーマットは `skill/agents/writer.md` と `storage/analytics/image-requests.md` 準拠。

---
## 2026-06-23-703
- 種類: 画像付き
- 投稿想定時刻: 夜（image2生成済み・GitHub Actions配信）
- 想定日: 2026-06-23（火）
- 軸: AI自動化メタ #監視と代替経路
- ソース: Claude Status: Elevated errors for Claude Opus 4.8 (Jun 23, 2026) https://status.claude.com/
- 画像プロンプト: Create a polished square social media summary card for Threads, 1024x1024. This must summarize the post, not be an atmospheric image. Theme: AI tools can have elevated errors, so creators need monitoring and fallback paths. Main Japanese headline, exact and large: AIは止まる。だから備える. Use three large blocks connected by arrows: 1) 気づく 2) 切り替える 3) 戻す. Include short supporting labels only: エラー検出, フォールバックに切り替え, 正常化を確認. Small top label: Claude Opus 4.8 / 6/23. Visual style: clean operations board, red alert card, teal fallback path, green recovery check. Avoid generic AI atmosphere, random laptop, tiny text, long Japanese sentences, decorative-only scene. Reject if date, product name, headline, or major labels are wrong or garbled.
- 画像ファイル: storage/images/2026-06-23-703.png
- 文面:

今日、Claudeのステータスを見ていて、Opus 4.8 の elevated errors が出ているのを確認しました。

こういう時に思うのは、AI運用は「止まらない前提」で組むほど危ないということです。

私も自動投稿を見直していて、生成側が止まると配信側だけ成功扱いになる怖さを痛感しました。

大事なのは、気づく、切り替える、戻す。この3つを最初から仕込むことですね。

皆さんはAIが止まった時の代替手段、用意していますか？

- ステータス: pending

---
