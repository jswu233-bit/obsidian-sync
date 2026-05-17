# ERRORS

## [ERR-20260516-001] git-daily-report-rebase-conflict

**Logged**: 2026-05-16T21:16:00+08:00
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
日报 git push 被远端更新顶住后，`git pull --rebase --autostash origin main` 因 `memory/.dreams/*` 冲突和未跟踪 `memory/2026-05-14.md` 阻塞。

### Error
```
error: The following untracked working tree files would be overwritten by checkout:
	memory/2026-05-14.md
...
CONFLICT (content): Merge conflict in memory/.dreams/events.jsonl
CONFLICT (content): Merge conflict in memory/.dreams/short-term-recall.json
```

### Context
- 操作：每日日报提交后推送 main
- 仓库内存在会变化的 memory 缓存文件与未跟踪 memory 文件
- 缓存冲突本身不影响日报正文，但会卡住 rebase/push

### Suggested Fix
- 每日日报提交时尽量只暂存目标日报文件
- 遇到 `memory/.dreams/*` 冲突时，优先视为缓存文件处理，选更新侧并继续 rebase
- rebase 前先检查是否存在会挡 checkout 的未跟踪 `memory/*.md`，必要时临时挪开再恢复

### Metadata
- Reproducible: yes
- Related Files: memory/.dreams/events.jsonl, memory/.dreams/short-term-recall.json, memory/2026-05-14.md
- See Also: none

---

## [ERR-20260516-002] wx-cli-init-task-for-pid-denied

**Logged**: 2026-05-16T14:26:58Z
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
`wx init --force` 能找到微信本地数据目录，但在扫描加密密钥时被 macOS `task_for_pid` 权限拦截，导致无法完成初始化。

### Error
```
检测微信数据目录...
找到数据目录: /Users/jamiewu/Library/Containers/com.tencent.xinWeChat/Data/Documents/xwechat_files/saint_js_05e3/db_storage
扫描加密密钥（需要 root 权限）...
WeChat PID: 94911
错误: task_for_pid 失败 (kr=5)
```

### Context
- 操作：在 `/Users/jamiewu/.wx-cli` 下执行 `wx init --force`
- `wx-cli` 依赖从运行中的 WeChat 进程提取解密密钥
- 当前 WeChat 未满足工具要求的可调试/重签名状态，因此 root 也不够

### Suggested Fix
- 先按工具提示对 `/Applications/WeChat.app` 重新签名，再重启 WeChat
- 然后用 root 执行 `sudo wx init`
- 若重签名时报 `signature in use`，先移除提示中的 dylib 签名再重签

### Metadata
- Reproducible: yes
- Related Files: /Users/jamiewu/.wx-cli/daemon.log, /Applications/WeChat.app
- See Also: none

---
