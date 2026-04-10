## [LRN-20260401-001] correction

**Logged**: 2026-04-01T01:25:00+08:00
**Priority**: high
**Status**: pending
**Area**: config

### Summary
用户明确纠正票务检索时间窗：不要“近一年新票”，应默认“近一个月”。

### Details
在 Discord ticket 线程中，用户指出 Spy_Bot 的新票设定时间范围过长（近一年），导致结果不符合预期。用户要求将默认窗口收敛到近一个月。

### Suggested Action
后续涉及“新票/近期票务”检索时，默认时间窗使用近30天（近一个月）；除非用户明确指定更长区间。

### Metadata
- Source: user_feedback
- Related Files: AGENTS.md
- Tags: ticketing,default-window,correction

---
