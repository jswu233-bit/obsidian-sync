# ERRORS

*错误记录文件 - 用于追踪和修复重复出现的问题*

---

## [ERR-20260319-001] git-sync-script-path

**Logged**: 2026-03-19T15:00:00Z
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
定时提醒中的 workspace 同步脚本路径不存在，导致无法执行同步脚本。

### Error
```bash
zsh:1: no such file or directory: /Users/jamiewu/.openclaw/workspace/skills/git-sync/scripts/sync-workspace.sh
Command not found
```

### Context
- Command attempted: `/Users/jamiewu/.openclaw/workspace/skills/git-sync/scripts/sync-workspace.sh`
- Reminder source claimed this script should run daily sync.
- Verified `/Users/jamiewu/.openclaw/workspace/skills` only contains `ima-skills/`; no `git-sync/` directory.

### Suggested Fix
- 更新定时任务配置中的脚本路径到真实位置，或恢复 `skills/git-sync/scripts/sync-workspace.sh`。
- 在 cron 任务前加 `test -x <script>` 预检查，并在失败时输出清晰告警。

### Metadata
- Reproducible: yes
- Related Files: .learnings/ERRORS.md

---
