## [ERR-20260614-001] sessions_send 参数冲突

**Logged**: 2026-06-14T16:20:00+08:00
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
`sessions_send` 在当前环境下对 `sessionKey` / `label` 的校验表现不一致，反复报“Provide either sessionKey or label (not both)”。

### Error
```
Provide either sessionKey or label (not both).
```

### Context
- 尝试向 `agent:spy:subagent:69a16d53-1456-4ba2-8906-d254c21805a2` 发送补采任务
- 传入了 `agentId`、`sessionKey`，并在不同重试中同时/分别携带 `label`
- 任务目标：继续补齐 X 与微信公众号采集

### Suggested Fix
统一明确 `sessions_send` 的调用约束：要么只允许 `sessionKey`，要么只允许 `label`，并给出可复用示例。

### Metadata
- Reproducible: yes
- Tags: sessions_send, subagent, orchestration

---
