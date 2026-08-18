# LEARNINGS.md

## [LRN-20260622-001] best_practice

**Logged**: 2026-06-22T20:45:00+08:00
**Priority**: high
**Status**: pending
**Area**: config

### Summary
升级 OpenClaw 后必须校验当前 PATH 中实际生效的 `openclaw` 二进制版本，避免只更新到另一套全局安装。

### Details
本次 `gateway update.run` 成功把一套全局安装升级到 `2026.6.9`，但当前 shell 实际调用的是 `~/.n/bin/openclaw`，仍停留在 `2026.4.23`。根因是机器上存在多套全局 Node/npm 前缀，`update.run` 更新的 root 与 PATH 中生效的安装不一致。补救方式是直接对活动前缀执行升级，并在之后同时验证：
- `which openclaw`
- `openclaw --version`
- 活动安装目录下 `package.json` 的版本
- `openclaw status` 的 Update / Gateway 状态

### Suggested Action
以后执行 OpenClaw 升级时，把“更新后核验活动二进制路径与版本”作为固定步骤；如存在 `.n` / Homebrew / 其他 prefix 混用，优先升级 PATH 中生效的那套安装。

### Metadata
- Source: conversation
- Related Files: .learnings/LEARNINGS.md
- Tags: openclaw, upgrade, npm, path, prefix
- Pattern-Key: openclaw.upgrade.active-prefix-verification

---

## [LRN-20260818-001] best_practice

**Logged**: 2026-08-18T21:00:00+08:00
**Priority**: high
**Status**: pending
**Area**: tools

### Summary
Daily report workflows should immediately switch to platform-specific fallback tools when `web_search` is broken, instead of waiting on the generic search provider.

### Details
During the 2026-08-18 daily report run, `web_search` failed with both country-filter and API-key errors. The practical path was to continue with xreach, public links, and source-specific pages rather than trying to force the generic search tool to work.

### Suggested Action
Treat `web_search` as optional in the daily-report SOP when the provider is unstable. Prefer direct platform readers and public fallback sources so the report can still ship on time.

### Metadata
- Source: conversation
- Related Files: SOPs/daily-report-sop-v1.md, SOPs/search-sop.md
- Tags: daily-report, search, fallback, reliability
- Pattern-Key: daily_report.search_fallback_first
- Recurrence-Count: 1
- First-Seen: 2026-08-18
- Last-Seen: 2026-08-18

---
