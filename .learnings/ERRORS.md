# ERRORS

## [ERR-20260603-001] protected-sop-missing-during-heartbeat-check

**Logged**: 2026-06-03T23:02:00+08:00
**Priority**: high
**Status**: pending
**Area**: ops

### Summary
Heartbeat 例行检查时发现受保护的 `SOPs/daily-report-sop-v1.md` 缺失，且 `.learnings/ERRORS.md` 目录/文件也不存在，导致保护性校验与经验记录链路一起失效。

### Error
```text
ENOENT: no such file or directory, access '/Users/jamiewu/.openclaw/workspace/SOPs/daily-report-sop-v1.md'
ENOENT: no such file or directory, access '/Users/jamiewu/.openclaw/workspace/.learnings/ERRORS.md'
```

### Context
- 操作：按 AGENTS 规则执行受保护 SOP 存在性检查
- 结果：SOPs 目录整体丢失，只能从 git 历史恢复
- 连带问题：`.learnings` 缺失，无法直接按 self-improvement 规范追加错误记录

### Suggested Fix
1. 恢复 `SOPs/daily-report-sop-v1.md` 与 `SOPs/search-sop.md`
2. 补建 `.learnings/` 基础文件
3. 后续凡执行 sync / 覆盖 / 清理后，显式检查 `SOPs/` 与 `.learnings/` 是否仍存在

### Metadata
- Reproducible: unknown
- Related Files: /Users/jamiewu/.openclaw/workspace/SOPs/daily-report-sop-v1.md, /Users/jamiewu/.openclaw/workspace/.learnings/ERRORS.md

---
