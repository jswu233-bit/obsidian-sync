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
