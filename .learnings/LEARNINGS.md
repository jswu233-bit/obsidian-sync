# LEARNINGS

## [LRN-20260314-001] correction

**Logged**: 2026-03-14T02:55:00+08:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
Jamie明确指出：记忆维护不能断档，必须每日记录并把长期结论归档到 MEMORY.md。

### Details
在 #repair 线程中，Jamie反馈“你为何每天都不写你的记忆，你也不总结你的记忆到大的记忆库”。这属于对执行纪律的直接纠偏：
1) daily memory 必须持续、可追踪；
2) 长期规则与关键决策必须及时提升到 MEMORY.md；
3) 不能只写零散日志而缺乏归档机制。

### Suggested Action
- 每日收尾前检查并补齐 `memory/YYYY-MM-DD.md`
- 每次出现“长期有效规则/流程变更”时，同步更新 `MEMORY.md`
- 建立固定提醒，避免再次漏记

### Metadata
- Source: user_feedback
- Related Files: memory/2026-03-14.md, MEMORY.md, AGENTS.md
- Tags: memory, correction, discipline, workflow

---

## [LRN-20260321-002] correction

**Logged**: 2026-03-21T13:57:00+08:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
在 Discord 线程中出现同一请求重复回复（双发），用户明确要求记录为教训并修正。

### Details
Jamie 反馈“你为啥每次回复我2次？”并要求“这个写到你的教训里去”。问题表现为：同一条请求被连续发送两次（正常回复 + 补发），影响群聊体验。

### Suggested Action
- 对同一 inbound message_id 只允许一次用户可见回复。
- 有 queued messages / 系统 completion 事件时，发送前先做去重检查（最近一条回复内容与 message_id 绑定校验）。
- 若已发送成功，不再发送补发文案。

### Metadata
- Source: user_feedback
- Related Files: AGENTS.md, SOUL.md
- Tags: correction, messaging, dedup, discord, ux

---
