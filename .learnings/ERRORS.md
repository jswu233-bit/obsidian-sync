# ERRORS

## [ERR-20260524-001] zsh-glob-nomatch-on-daily-file-check

**Logged**: 2026-05-24T21:02:00+08:00
**Priority**: medium
**Status**: pending
**Area**: ops

### Summary
用 zsh 通配符检查日报文件是否存在时触发 `no matches found`，导致检测输出混淆。

### Error
```bash
zsh:1: no matches found: /Users/jamiewu/.openclaw/workspace/daily/2026-05-24*
文件尚未生成
```

### Context
- 操作：检查 `daily/2026-05-24*.md` 是否已生成
- 环境：Darwin + zsh
- 根因：zsh 默认开启 nomatch，裸 glob 在无匹配时直接报错

### Suggested Fix
检查文件存在时避免裸 glob；改用 `find`, `ls ... 2>/dev/null`, 或先 `setopt NULL_GLOB` / 用数组安全处理。

### Metadata
- Reproducible: yes
- Related Files: /Users/jamiewu/.openclaw/workspace/daily

---
## [ERR-20260524-002] market-quote-fetch-rate-limited

**Logged**: 2026-05-24T21:22:00+08:00
**Priority**: medium
**Status**: pending
**Area**: ops

### Summary
批量抓取市场行情时被上游站点限流，多个指数返回 HTTP 429。

### Error
```text
SPX ERR HTTP Error 429: Too Many Requests
IXIC ERR HTTP Error 429: Too Many Requests
DJI ERR HTTP Error 429: Too Many Requests
HSI ERR HTTP Error 429: Too Many Requests
000001.SS ...
```

### Context
- 操作：批量获取 SPX / IXIC / DJI / HSI / 上证指数 等行情
- 结果：命令退出码为 0，但核心数据请求被源站拒绝
- 可能原因：同一来源短时间请求过密，触发限流

### Suggested Fix
对行情源做串行抓取与退避重试；必要时切换备用数据源，避免短时间并发命中 429。

### Metadata
- Reproducible: yes
- Related Files: /Users/jamiewu/.openclaw/workspace/.learnings/ERRORS.md

---
