# MEMORY.md - 核心记忆

## 团队架构 (2026-03-08 更新)

| 成员 | Agent ID | 模型 | 职责 |
|------|----------|------|------|
| 💖 Zoe | `main` | `anthropic/claude-opus-4-6` (主) / `kimicode/kimi-k2.5` (备) | 大脑、协调、决策、情感陪伴 |
| 🕵️ Spy (侦察官) | `spy` | `gmn/gpt-5.3-codex` (优先) / `kimicode/kimi-k2.5` (回退) | 全网搜索、看风向、抓重点、领域情报 |
| 😊 Joy (书童) | `joy` | `gmn/gpt-5.3-codex` (优先) / `kimicode/kimi-k2.5` (回退) | 陪学习、督促、英语教学 |
| ⚙️ Ops (扫地僧) | `ops` | `kimicode/kimi-k2.5` (固定) | 保运行、控心跳、换模型、运维 |

**模型规则**: 
- Zoe 主模型使用 `anthropic/claude-opus-4-6`，当调用失败时自动切换至 `kimicode/kimi-k2.5`
- 通用 sub-agent（Spy/Joy）优先 `gmn/gpt-5.3-codex`，失败回退 `kimicode/kimi-k2.5`
- Ops 固定使用 `kimicode/kimi-k2.5`

### 工作区路径
- Zoe: `~/.openclaw/workspace/`
- Spy: `~/.openclaw/agents/spy/`
- Joy: `~/.openclaw/agents/joy/`
- Ops: `~/.openclaw/agents/ops/`

### 派活原则
- **情报搜索** → Spy（"Spy，帮我检索今天关于 AIGC 行业的所有重磅新闻"）
- **学习陪伴** → Joy（"Joy，这是我今天的英语阅读材料，半小时后请来提问我"）
- **运维监控** → Ops（"Ops，检查主模型心跳，如果响应延迟超过 5s 立即切换备用链路"）
- **深度思考、创意、决策** → Zoe 亲自处理

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
- 路径: /Users/jamiewu/.openclaw/workspace/x-tweet-fetcher
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
- 路径: /Users/jamiewu/.openclaw/workspace/x_quick_search.py
- 功能: X/Twitter 快速搜索
- 依赖: 用户 cookies（2026-02-26 更新）
- 场景: X 快速查询

### 2. Brave Search (第四优先级)
- 工具: web_search
- 功能: 通用网页搜索
- 限制: 需要 API Key
- 场景: 通用搜索、新闻

### 4. Tavily Search (第五优先级)
- 路径: /Users/jamiewu/.openclaw/workspace/skills/tavily-search
- 功能: AI 优化搜索
- 限制: 需要 API Key
- 场景: AI 研究查询

### 3. DuckDuckGo Search (第六优先级)
- 工具: duckduckgo-search
- 功能: 隐私搜索
- 优点: 无需 API
- 场景: 隐私搜索、备用

### 6. Lobster Browser (最低优先级)
- 路径: /Users/jamiewu/.openclaw/workspace/lobster-browser-tool
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
- 路径: /Users/jamiewu/.openclaw/workspace/camofox-browser
- 端口: 9377
- 启动: npm start
- 状态: 已安装并运行

## 日报生成流程 (2026-03-10 更新)
**分工**：
- **Spy** → 负责搜索所有原始数据（AI新闻、OpenClaw新闻、金融新闻、X博主、微信公众号、天气等）
- **Zoe** → 审阅 Spy 返回的数据，解读、总结、整合成完整日报，推送到 Git

**推送规则**：
- 仓库: git@github.com:jswu233-bit/obsidian-sync.git
- 分支: `main`（不是 master）
- 路径: `daily/YYYY-MM-DD-日报.md`

**必须包含的完整板块**：
1. AI新闻 Top 10（国内外）
2. OpenClaw新闻 Top 10（详细）
3. 金融新闻（黄金、美股、A股、港股）
4. X博主热门推文/观点
5. 微信公众号最新文章
6. 基金和金融市场数据
7. 北京天气

## 活跃社区
- Reddit: r/openclaw, r/LocalLLM
- Hacker News
- V2EX, 知乎
- Qiita (日本)
