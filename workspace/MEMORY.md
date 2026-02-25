# MEMORY.md - 核心记忆更新

## 搜索技能优先级 (2026-02-25 更新)
**优先级: 1 > 5 > 2 > 4 > 3 > 6**

### 1. x-tweet-fetcher ⭐ (最高优先级)
- 路径: /root/.openclaw/workspace/x-tweet-fetcher
- 功能: X/Twitter、微信公众号
- 依赖: Camofox (端口 9377)
- 场景: X 内容、社交媒体监控

### 5. X Quick Search (第二优先级)
- 路径: /root/.openclaw/workspace/x_quick_search.py
- 功能: X/Twitter 快速搜索
- 依赖: 用户 cookies
- 场景: X 快速查询

### 2. Brave Search (第三优先级)
- 工具: web_search
- 功能: 通用网页搜索
- 限制: 需要 API Key
- 场景: 通用搜索、新闻

### 4. Tavily Search (第四优先级)
- 路径: /root/.openclaw/workspace/skills/tavily-search
- 功能: AI 优化搜索
- 限制: 需要 API Key
- 场景: AI 研究查询

### 3. DuckDuckGo Search (第五优先级)
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
1. X/Twitter → x-tweet-fetcher (1)
2. X 快速查询 → X Quick Search (5)
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

## 关注博主
- @gkxspace (余温) - OpenClaw 多角色协作
- @yulin807 (Qingyue) - Issue Driven 系统

## 活跃社区
- Reddit: r/openclaw, r/LocalLLM
- Hacker News
- V2EX, 知乎
- Qiita (日本)
