# ERRORS.md

## [ERR-20260609-001] git_add_missing_directory

**Logged**: 2026-06-09T23:32:02+0800
**Priority**: medium
**Status**: resolved
**Area**: docs

### Summary
每日记忆维护提交时，固定命令里的 `.learnings` 路径不存在，导致 `git add memory MEMORY.md .learnings` 未把 `memory/2026-06-09.md` stage 进去。

### Error
```
fatal: pathspec '.learnings' did not match any files
no changes added to commit (use "git add" and/or "git commit -a")
```

### Context
- Command attempted: `git add memory MEMORY.md .learnings || true && git commit -m "chore(memory): daily log + memory+feishu index sync" || true`
- Trigger: `daily-memory-log-creator` cron
- Workspace lacked the `.learnings/` directory and baseline files expected by `AGENTS.md`.

### Suggested Fix
预先创建 `.learnings/` 及基础文件 `LEARNINGS.md`、`ERRORS.md`、`FEATURE_REQUESTS.md`，再执行固定提交命令。

### Metadata
- Reproducible: yes
- Related Files: `.learnings/ERRORS.md`, `AGENTS.md`

### Resolution
- **Resolved**: 2026-06-09T23:32:02+0800
- **Commit/PR**: pending
- **Notes**: 已创建 `.learnings/` 骨架文件，准备重跑固定提交命令。

---
