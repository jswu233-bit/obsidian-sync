## [LRN-20260614-001] browser_x_snapshot_recovery

**Logged**: 2026-06-14T16:20:00+08:00
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
X 主页快照比网页搜索更稳，能直接读到可验证的 profile header 和近期帖子；浏览器里拿到的临时 tab id 不能复用，需立刻 snapshot 同一 tab 或重新 open。

### Details
本次日报采集里，X 搜索页多次触发挑战页或可抓取性不稳定，但直接打开公开 profile 后，`browser snapshot` 可以稳定读到主页信息和最近几条帖子。通过 `targetId` 复用旧标签时，一旦页面重载或标签切换，旧 id 会失效。

### Suggested Action
以后采 X 时优先：公开 profile -> 立即 snapshot -> 记录稳定事实；不要依赖搜索结果页的临时 tab id。

### Metadata
- Source: conversation
- Tags: x, browser, snapshot, recovery
- Pattern-Key: harden.browser_tab_reuse
- Recurrence-Count: 1

---
