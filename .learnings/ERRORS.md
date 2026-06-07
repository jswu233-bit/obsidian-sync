# ERRORS.md

## [ERR-20260607-001] git add .learnings pathspec missing

**Logged**: 2026-06-07T23:31:00+08:00
**Priority**: medium
**Status**: pending
**Area**: docs

### Summary
执行每日记忆维护提交命令时，因工作区缺少 `.learnings/` 目录导致 `git add memory MEMORY.md .learnings` 报 pathspec 错误。

### Error
```text
fatal: pathspec '.learnings' did not match any files
```

### Context
- Command/operation attempted: `git add memory MEMORY.md .learnings || true && git commit -m "chore(memory): daily log + memory+feishu index sync" || true`
- During: daily-memory-log-creator 定时维护
- Environment: OpenClaw workspace

### Suggested Fix
预置 `.learnings/` 目录及基础日志文件，避免后续每日维护命令再次报错。

### Metadata
- Reproducible: yes
- Related Files: .learnings/ERRORS.md

---
