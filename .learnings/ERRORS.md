## [ERR-20260412-001] message_send_empty_components

**Logged**: 2026-04-12T00:14:00+08:00
**Priority**: low
**Status**: pending
**Area**: config

### Summary
向 Discord 发送消息时带了空的 components.modal 结构，导致 message 工具参数校验失败。

### Error
```
components.modal.fields must be a non-empty array
```

### Context
- Operation: message action=send
- Channel: discord
- accountId: eva
- 问题原因：调用时传入了默认空的 `components` 对象，而不是完全省略该字段。

### Suggested Fix
发送普通文本消息时不要附带空 `components`；只在确实需要交互组件时传该字段。

### Metadata
- Reproducible: yes
- Related Files: none

---

## [ERR-20260412-001] gateway.config.patch.json5

**Logged**: 2026-04-12T17:34:00+08:00
**Priority**: medium
**Status**: pending
**Area**: config

### Summary
First config.patch attempt failed because the raw JSON5 patch string was malformed (missing closing braces).

### Error
```
SyntaxError: JSON5: invalid end of input at 1:443
```

### Context
- Operation attempted: gateway config.patch
- Goal: set Discord channel 1482070717838266518 to require mentions and ignore mentions to other agents
- Cause: malformed raw patch payload assembled manually

### Suggested Fix
Validate brace balance before sending gateway.config.patch payloads; prefer building minimal patch objects carefully.

### Metadata
- Reproducible: yes
- Related Files: /Users/jamiewu/.openclaw/openclaw.json
- Source: tool failure

---

## [ERR-20260412-002] daily_report_missing_sop

**Logged**: 2026-04-12T21:00:00+08:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
定时日报任务因缺少强制前置 SOP 文件 `SOPs/daily-report-sop-v1.md` 而在前置检查阶段立即失败，未进入采集、生成、发送、Git 提交流程。

### Error
```
ENOENT: no such file or directory, access '/Users/jamiewu/.openclaw/workspace/SOPs/daily-report-sop-v1.md'
```

### Context
- Operation: cron 日报任务执行
- Required SOP: /Users/jamiewu/.openclaw/workspace/SOPs/daily-report-sop-v1.md
- Workdir: /Users/jamiewu/.openclaw/workspace
- SOPs directory listing at failure time:
  - instreet-intel-v1.md
  - proactive-boundary-v1.md
  - search-sop.md
- Result: 按任务要求立即失败并停止发送

### Suggested Fix
补齐 `SOPs/daily-report-sop-v1.md`，然后重新运行 cron 任务。

### Metadata
- Reproducible: yes
- Related Files: /Users/jamiewu/.openclaw/workspace/SOPs
- Source: tool failure / missing dependency

---
## [ERR-20260412-003] daily_report_sop_deleted_by_sync

**Logged**: 2026-04-12T21:20:00+08:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
`SOPs/daily-report-sop-v1.md` 反复丢失的直接原因已定位：`sync(core)` 提交把该文件删除并同步到 main，导致后续 cron/人工执行都报 SOP 缺失。

### Error
```
commit f257c91 sync(core): 2026-04-10 23:00:13 CST
D    SOPs/daily-report-sop-v1.md
```

### Context
- Current check on 2026-04-12: `HAS_SOP=0`
- `git log -- SOPs/daily-report-sop-v1.md` 显示该文件在 `f257c91` 被删除
- 恢复来源：`exports/SOPs-skill-pack-20260323-121302.zip` 中的 `SOPs/daily-report-sop-v1.md`
- Impact: cron 前置检查失败，用户多次要求“找回这个 SOP”

### Suggested Fix
1. 恢复并提交 `SOPs/daily-report-sop-v1.md`
2. 排查 `sync(core)` 流程为何会把 `SOPs/` 下文件视为待删除
3. 给日报 cron 增加“若 SOP 丢失则从备份恢复/显式报警”的保护

### Metadata
- Reproducible: yes
- Related Files: /Users/jamiewu/.openclaw/workspace/SOPs/daily-report-sop-v1.md
- See Also: ERR-20260412-002
- Source: tool failure / git history audit

---
## [ERR-20260412-004] browser_gateway_timeout_for_x_fetch

**Logged**: 2026-04-12T22:12:00+08:00
**Priority**: medium
**Status**: pending
**Area**: integration

### Summary
按新版 X 搜索 SOP 重跑日报时，尝试用 host/user 浏览器补抓 X 内容，但 browser 工具因 OpenClaw gateway 超时不可用，无法进入登录态抓取链路。

### Error
```
browser: timed out. Restart the OpenClaw gateway (OpenClaw.app menubar, or `openclaw gateway`). Do NOT retry the browser tool — it will keep failing.
```

### Context
- Goal: 按新版 X SOP 提升日报中 X 板块质量
- Tried: browser status target=host profile=user
- Result: browser tool unavailable, 只能退回公开搜索/网页补位

### Suggested Fix
1. 重启 OpenClaw gateway
2. 恢复 host/user 浏览器登录态链路后再跑 X 板块
3. 若仍不可用，让用户直接提供 X 链接作为输入

### Metadata
- Reproducible: yes
- Related Files: SOPs/daily-report-sop-v1.md, SOPs/search-sop.md
- Source: tool failure / browser gateway

---
## [ERR-20260413-001] x_public_fetch_unstable

**Logged**: 2026-04-13T21:36:00+08:00
**Priority**: medium
**Status**: pending
**Area**: search

### Summary
X 平台公开搜索 + 网页抓取在日报任务中命中质量不稳定，无法可靠支撑“指定账号 + 当日动态 + 详细解读”。

### Error
```
web_fetch(x.com/<handle>) frequently returned generic error pages like:
"Something went wrong, but don’t fret — let’s give it another shot."

browser snapshot also intermittently failed with:
"tab not found"
```

### Context
- Operation: 日报任务中的 X 板块采集
- Sources attempted: web_search, web_fetch(x.com), browser open/snapshot
- Impact: 不能高置信度还原指定账号当日帖文，只能保守降级

### Suggested Fix
1. X 板块默认升级到登录态浏览器或直接输入帖文链接
2. 不再把公开搜索当主链路
3. 浏览器拿到 targetId 后尽快 snapshot，减少 tab 丢失窗口

### Metadata
- Reproducible: yes
- Related Files: SOPs/search-sop.md, daily/2026-04-13-update.md
- Source: tool failure / external site instability

---
