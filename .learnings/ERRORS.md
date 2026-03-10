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
