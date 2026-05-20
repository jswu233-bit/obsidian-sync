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

## [ERR-20260520-001] browser-openclaw-targetid-instability

**Logged**: 2026-05-20T21:05:00+08:00
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
使用 browser 工具抓取 X 页面时，`open` 返回的 `targetId` 随后在 `navigate` / `act` 中可能失效或跳到其他标签页，且 `profiles` 查询一度超时，导致批量采集流程中断。

### Error
```
Error: page.evaluate: Execution context was destroyed, most likely because of a navigation.
Error: tab not found
profiles: timed out. Restart the OpenClaw gateway ... Do NOT retry the browser tool ...
```

### Context
- 操作：按子任务要求，用 browser 逐个访问 X 主页并抓取今日推文
- 环境：host browser / openclaw profile / Chrome CDP
- 现象：`open` 后能读到 `x.com/op7418` 页面，但后续 `act` 返回了其他 tab 的 targetId；再次 `navigate` 报 `tab not found`；`profiles` 进一步超时

### Suggested Fix
- 在长链路抓取前，优先用独立新 tab 并立即做一次轻量校验（url/title/articleCount）
- 如发现 targetId 漂移或 gateway 超时，尽快放弃 browser 路线并切换替代抓取方式，避免在同一 browser 会话里继续重试
- 排查 openclaw browser target 绑定稳定性，尤其是多 tab / 现有用户浏览器干扰场景

### Metadata
- Reproducible: unknown
- Related Files: none
- See Also: none

---

## [ERR-20260520-002] python-json-literal-bool

**Logged**: 2026-05-20T21:12:00+08:00
**Priority**: low
**Status**: pending
**Area**: docs

### Summary
临时 Python 写 JSON 脚本时误用了 JSON 的 `true` 字面量，导致脚本退出。

### Error
```
NameError: name 'true' is not defined. Did you mean: 'True'?
```

### Context
- 操作：将已抓取的 X 推文结果写入 `/tmp/x_today_posts_20260520.json`
- 原因：在 Python 字面量里直接粘贴了 JSON 风格布尔值

### Suggested Fix
- 在 Python 字面量中统一使用 `True/False`
- 或者先组织 Python dict，再 `json.dumps`

### Metadata
- Reproducible: yes
- Related Files: /tmp/x_today_posts_20260520.json
- See Also: none

---
