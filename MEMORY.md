# MEMORY.md - 核心记忆

## 团队架构 (2026-02-26 建立)

| 成员 | Agent ID | 模型 | 职责 |
|------|----------|------|------|
| 💖 Zoe | `main` | `anthropic/claude-opus-4-6` | 大脑、协调、决策、情感陪伴 |
| 🕵️ 情报官 | `intel` | `kimicode/kimi-k2.5` | 搜索、情报收集、信息验证 |
| 🔧 打杂工 | `handyman` | `kimicode/kimi-k2.5` | 模型切换、心跳维护、配置管理 |

### 工作区路径
- Zoe: `~/.openclaw/workspace/`
- 情报官: `~/.openclaw/agents/intel/`
- 打杂工: `~/.openclaw/agents/handyman/`

### 派活原则
- 搜索类 → 情报官
- 运维类 → 打杂工
- 深度思考、创意、聊天 → Zoe 亲自处理
- 简单快速搜索 → Zoe 自己来（不值得派活开销）

## 可用模型 (2026-02-26 更新)

| Provider | 模型 | 备注 |
|---------|------|------|
| anthropic | claude-opus-4-6 | Zoe 主力模型 |
| kimicode | kimi-k2.5 | sub-agent 模型，Anthropic API 格式 |
| kimi-coding | k2p5 | 编程专用，支持 reasoning |
| moonshot | kimi-k2-thinking | 思考模式 |
| moonshot | kimi-k2-thinking-turbo | 思考加速版 |
| moonshot | kimi-k2.5 | 通用版本 |
| moonshot | moonshot-v1-128k | 128K 上下文 |

> ⚠️ hajimi provider 已于 2026-02-26 移除

## 记忆管理规则
- 每天写 `memory/YYYY-MM-DD.md` 日记
- 重要内容归档到本文件（MEMORY.md）
- 超过 7 天的日记可清理

---

## 搜索技能优先级 (2026-02-26 更新)
**优先级: 1 > 7 > 5 > 2 > 4 > 3 > 6**

### 1. x-tweet-fetcher ⭐ (最高优先级)
- 路径: /root/.openclaw/workspace/x-tweet-fetcher
- 功能: X/Twitter、微信公众号
- 依赖: Camofox (端口 9377)
- 场景: X 内容、社交媒体监控

### 7. x-reader 🆕 (第二优先级 - 多平台)
- 安装: pip (全局)，CLI 命令 `x-reader`
- 功能: 7+ 平台内容抓取（微信、B站、小红书、YouTube、Telegram、RSS、任意网页）
- X/Twitter: 需要 Playwright + session（当前被反爬限制，X 内容用 x_quick_search 替代）
- Session: ~/.x-reader/sessions/twitter.json
- 场景: 多平台内容抓取、URL 解析

### 5. X Quick Search (第三优先级)
- 路径: /root/.openclaw/workspace/x_quick_search.py
- 功能: X/Twitter 快速搜索
- 依赖: 用户 cookies（2026-02-26 更新）
- 场景: X 快速查询

### 2. Brave Search (第四优先级)
- 工具: web_search
- 功能: 通用网页搜索
- 限制: 需要 API Key
- 场景: 通用搜索、新闻

### 4. Tavily Search (第五优先级)
- 路径: /root/.openclaw/workspace/skills/tavily-search
- 功能: AI 优化搜索
- 限制: 需要 API Key
- 场景: AI 研究查询

### 3. DuckDuckGo Search (第六优先级)
- 工具: duckduckgo-search
- 功能: 隐私搜索
- 优点: 无需 API
- 场景: 隐私搜索、备用

### 6. Lobster Browser (最低优先级)
- 路径: /root/.openclaw/workspace/lobster-browser-tool
- 功能: 浏览器自动化
- 限制: 配置复杂
- 场景: 复杂网页操作

## 使用规则
1. X/Twitter 内容 → x-tweet-fetcher (1) 或 X Quick Search (5)
2. 微信/B站/小红书/YouTube/RSS → x-reader (7)
3. 通用搜索 → Brave Search (2)
4. AI 研究 → Tavily (4)
5. 隐私搜索 → DuckDuckGo (3)
6. 复杂操作 → Lobster Browser (6)

## Camofox 配置
- 路径: /root/.openclaw/workspace/camofox-browser
- 端口: 9377
- 启动: npm start
- 状态: 已安装并运行

## 日报技能
- 脚本: /root/.openclaw/workspace/skills/daily-report/generate.sh
- 数据源: x-tweet-fetcher + sogou_wechat
- 输出: /obsidian-sync/daily/YYYY-MM-DD/
- 定时: 每天 21:00

## 活跃社区
- Reddit: r/openclaw, r/LocalLLM
- Hacker News
- V2EX, 知乎
- Qiita (日本)
