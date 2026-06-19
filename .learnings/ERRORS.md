# ERRORS.md

## [ERR-20260618-001] git_add_pathspec_missing

**Logged**: 2026-06-18T23:30:00+08:00
**Priority**: medium
**Status**: pending
**Area**: docs

### Summary
`git add memory MEMORY.md .learnings || true && git commit ... || true` 首次执行失败，因为工作区中不存在 `.learnings/` 目录，导致 `git add` 报 pathspec 错误且未把 `memory/2026-06-18.md` 加入暂存区。

### Error
```
fatal: pathspec '.learnings' did not match any files
```

### Context
- 操作：执行每日记忆维护任务要求的固定 git 提交命令
- 结果：`git add` 因 `.learnings` 缺失失败，后续 commit 因无已暂存变更未生成提交

### Suggested Fix
先创建 `.learnings/` 并记录错误，再重新执行固定 git 提交命令。

### Metadata
- Reproducible: yes
- Related Files: .learnings/ERRORS.md, memory/2026-06-18.md

---

## [ERR-20260619-002] agent_reach_exa_not_configured

**Logged**: 2026-06-19T21:05:00+08:00
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
按 search-sop 优先尝试使用 agent-reach 的 Exa 全网搜索时失败，原因是本机 mcporter 未配置 exa MCP server，导致 `exa.web_search_exa` 无法调用。

### Error
```
[mcporter] Unknown MCP server 'exa'.
Error: Unknown MCP server 'exa'.
```

### Context
- 操作：执行 AI 新闻采集任务，优先使用 agent-reach 搜索今日 AI 新闻
- 命令：`mcporter call 'exa.web_search_exa(query: "AI artificial intelligence news June 19 2026", numResults: 8)'`
- 结果：命令直接失败，随后退回 Google News RSS + 网页抓取链路完成任务

### Suggested Fix
按 `agent-reach doctor` 提示执行：`mcporter config add exa https://mcp.exa.ai/mcp`，恢复 Exa 搜索能力。

### Metadata
- Reproducible: yes
- Related Files: .learnings/ERRORS.md

---

