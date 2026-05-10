
## [LRN-20260510-001] best_practice

**Logged**: 2026-05-10T21:08:00+08:00
**Priority**: medium
**Status**: pending
**Area**: docs

### Summary
subagent 派发时优先使用最小必要参数，避免混入 ACP 专用字段导致失败。

### Details
本次为日报补采 AI 新闻时，重复携带了 ACP 线程相关字段，触发 subagent 参数报错。对于日常 Spy/Ops 子任务，直接沿用最简可运行参数更稳。

### Suggested Action
后续 native subagent 默认只传 agentId、task、runtime、mode、必要 cwd/context；非 ACP 不带 streamTo/thread 等字段。

### Metadata
- Source: simplify-and-harden
- Related Files: AGENTS.md
- Tags: subagent, openclaw, reliability
- Pattern-Key: harden.subagent_minimal_params

---
