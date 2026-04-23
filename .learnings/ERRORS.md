# ERRORS


## [ERR-20260423-001] git pull --rebase --autostash blocked by untracked file

**Logged**: 2026-04-23T13:43:53.412333+00:00
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
日报发布时，`git push origin main` 被远端领先拒绝，随后 `git pull --rebase --autostash origin main` 又被未跟踪文件 `memory/2026-04-22.md` 阻塞，导致自动发布中断。

### Error
```
error: The following untracked working tree files would be overwritten by checkout:
	memory/2026-04-22.md
Aborting
error: could not detach HEAD
```

### Context
- Operation attempted: 日报 git 提交并 push main
- Trigger: remote main ahead of local
- Workspace: /Users/jamiewu/.openclaw/workspace

### Suggested Fix
在 rebase 前先安全转移或备份冲突的未跟踪文件，再执行 `git pull --rebase --autostash origin main` 与 `git push origin main`。

### Metadata
- Reproducible: yes
- Related Files: memory/2026-04-22.md, daily/2026-04-23-update.md

---
