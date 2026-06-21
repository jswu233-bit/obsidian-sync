# ERRORS.md

## [ERR-20260621-001] read .learnings files missing

**Logged**: 2026-06-21T23:33:00+08:00
**Priority**: medium
**Status**: pending
**Area**: docs

### Summary
读取 `.learnings/LEARNINGS.md` 和 `.learnings/ERRORS.md` 时发现工作区缺少 `.learnings/` 目录。

### Error
```
ENOENT: no such file or directory, access '/Users/jamiewu/.openclaw/workspace/.learnings/LEARNINGS.md'
ENOENT: no such file or directory, access '/Users/jamiewu/.openclaw/workspace/.learnings/ERRORS.md'
```

### Context
- Operation attempted: daily-memory-log-creator 维护时读取 `.learnings/` 日志文件
- Workspace: `/Users/jamiewu/.openclaw/workspace`
- Trigger: `.learnings/` 目录尚未初始化

### Suggested Fix
初始化 `.learnings/` 目录及基础日志文件，后续按 self-improvement 规则持续记录。

### Metadata
- Reproducible: yes
- Related Files: .learnings/ERRORS.md, .learnings/LEARNINGS.md, .learnings/FEATURE_REQUESTS.md

---
