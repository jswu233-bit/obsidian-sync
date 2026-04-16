# ERRORS.md

## [ERR-20260415-001] sync_obsidian_core_precheck

**Logged**: 2026-04-15T23:01:00+08:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
核心同步前置检查失败：受保护文件 `SOPs/daily-report-sop-v1.md` 在工作区缺失，导致同步任务中断。

### Error
```
ls: /Users/jamiewu/.openclaw/workspace/SOPs/daily-report-sop-v1.md: No such file or directory
```

### Context
- 触发任务：每日 Obsidian Git 核心资料同步
- 检查命令：`test -f /Users/jamiewu/.openclaw/workspace/SOPs/daily-report-sop-v1.md && /Users/jamiewu/.openclaw/workspace/scripts/sync_obsidian_core.sh`
- 发现问题后，已从 Git 历史提交 `3f4ac01` 恢复该 SOP 文件。

### Suggested Fix
继续保留并严格执行“sync / 覆盖 / 清理后必须检查并恢复受保护 SOP”的规则；后续若再出现，优先自动恢复后再执行同步。

### Metadata
- Reproducible: unknown
- Related Files: SOPs/daily-report-sop-v1.md, scripts/sync_obsidian_core.sh, AGENTS.md

---


## 2026-04-16
- daily report: 北京政府天气直链 `https://www.beijing.gov.cn/fuwu/bmfw/sy/jrts/20260416_4583328.html` 返回“页面已撤稿或删除”。处理：改用搜索/公开天气源补位，不在日报中直接留空或写“无法获取”。
- web_search: Brave 参数 `freshness:"week"` 在当前接口下可能报错，改为空字符串或省略该参数更稳。
