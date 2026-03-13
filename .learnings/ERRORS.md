# Errors Log

Command failures, exceptions, and unexpected behaviors.

---

## [ERR-20260310-001] web_search (Brave API)

**Logged**: 2026-03-10T21:07:00+08:00
**Priority**: low
**Status**: pending
**Area**: infra

### Summary
Brave search_lang 参数使用 `zh` 导致 422 校验失败。

### Error
```
Brave Search API error (422): Unable to validate request parameter(s)
Input should be ... 'zh-hans' or 'zh-hant' ...
input: "zh"
```

### Context
- Operation: web_search("知乎 OpenClaw 2026-03-10")
- Params: search_lang="zh", country="ALL"
- Expected: 中文结果过滤

### Suggested Fix
后续统一使用 Brave 支持的语言枚举（中文用 `zh-hans` 或 `zh-hant`），避免 `zh`。

### Metadata
- Reproducible: yes
- Related Files: none

---

## [ERR-20260310-002] git-sync script on macOS

**Logged**: 2026-03-10T23:00:30+08:00
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
每日 git 同步脚本执行失败：`stat -c` 在 macOS 不兼容，且推送阶段缺少 GitHub 凭证。

### Error
```
stat: illegal option -- c
usage: stat [-FLnq] [-f format | -l | -r | -s | -x] [-t timefmt] [file ...]
...
fatal: could not read Username for 'https://github.com': Device not configured
```

### Context
- Command: `/Users/jamiewu/.openclaw/workspace/skills/git-sync/scripts/sync-workspace.sh`
- Environment: Darwin 25.2.0 (macOS)
- Observed behavior:
  - 文件大小显示为空（`( bytes)`）
  - `git pull` 被未跟踪 `.DS_Store` 阻塞
  - `git push` 因 HTTPS 认证缺失失败

### Suggested Fix
1. 脚本适配 macOS：`stat -f%z`（或做 GNU/BSD 分支判断）。
2. 在 `obsidian-sync` 仓库加入 `.gitignore`（至少忽略 `.DS_Store`）。
3. 统一 Git 认证：改用 SSH remote 或配置 GitHub credential helper/token。

### Metadata
- Reproducible: yes
- Related Files: 
  - skills/git-sync/scripts/sync-workspace.sh
  - obsidian-sync/.gitignore
- See Also: none

---

## [ERR-20260314-001] sessions_spawn (ACP thread-bound on Discord)

**Logged**: 2026-03-14T01:26:00+08:00
**Priority**: medium
**Status**: pending
**Area**: config

### Summary
在 Discord 频道中尝试用 `sessions_spawn(runtime="acp", thread=true)` 调用 Claude Code 创建新 agent 时失败，当前账号未开启 thread-bound ACP。

### Error
```
Discord thread-bound ACP spawns are disabled for this account
(set channels.discord.threadBindings.spawnAcpSessions=true to enable).
```

### Context
- Operation: sessions_spawn
- Params: runtime=acp, agentId=claude-code, thread=true, mode=session
- User intent: 让 Claude Code 创建新 subagent（Eva/解花语）

### Suggested Fix
1. 在网关配置中启用 `channels.discord.threadBindings.spawnAcpSessions=true`；
2. 或者临时改为非 thread-bound ACP 会话（`thread=false`）执行创建任务。

### Metadata
- Reproducible: yes
- Related Files: gateway config (channels.discord.threadBindings)
- See Also: none

---

## [ERR-20260314-002] exec command not found (rg)

**Logged**: 2026-03-14T02:18:00+08:00
**Priority**: low
**Status**: pending
**Area**: infra

### Summary
在当前主机上使用 `rg` 搜索时失败，系统未安装 ripgrep。

### Error
```
zsh:1: command not found: rg
```

### Context
- Operation: exec
- Command: `rg -n ...`
- Task: 批量定位 workspace 中的 subagent 描述与模型配置

### Suggested Fix
改用系统自带 `grep -R -n`，避免依赖 `rg`。

### Metadata
- Reproducible: yes
- Related Files: none
- See Also: none

---
