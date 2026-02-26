# Search Skill 配置
# 优先级: 1 > 5 > 2 > 4 > 3 > 6

## 搜索技能优先级

### 1. x-tweet-fetcher ⭐ (最高优先级)
- **路径**: /root/.openclaw/workspace/x-tweet-fetcher
- **功能**: X/Twitter 用户时间线、关键词搜索、微信公众号
- **依赖**: Camofox (端口 9377)
- **优点**: 无需 API 密钥，本地运行
- **使用场景**: X 内容、微信公众号、社交媒体监控

### 5. X Quick Search (第二优先级)
- **路径**: /root/.openclaw/workspace/x_quick_search.py
- **功能**: X/Twitter 快速搜索
- **依赖**: 用户配置的 cookies
- **优点**: 无需 Camofox，快速启动
- **使用场景**: X 快速查询、简单搜索

### 2. Brave Search (第三优先级)
- **工具**: web_search
- **功能**: 通用网页搜索
- **优点**: 快速、准确
- **限制**: 需要 API Key
- **使用场景**: 通用网页搜索、新闻、文档

### 4. Tavily Search (第四优先级)
- **路径**: /root/.openclaw/workspace/skills/tavily-search
- **功能**: AI 优化搜索
- **优点**: 专为 AI Agent 设计，结果结构化
- **限制**: 需要 API Key
- **使用场景**: AI 优化搜索、研究查询

### 3. DuckDuckGo Search (第五优先级)
- **工具**: duckduckgo-search
- **功能**: 隐私搜索
- **优点**: 无需 API，隐私保护
- **限制**: 结果可能不如 Brave 准确
- **使用场景**: 隐私搜索、备用方案

### 6. Lobster Browser (最低优先级)
- **路径**: /root/.openclaw/workspace/lobster-browser-tool
- **功能**: 浏览器自动化
- **优点**: 可视化操作
- **限制**: 配置复杂，需要 Playwright
- **使用场景**: 复杂网页操作、需要视觉确认

---

## 使用规则

1. **X/Twitter 内容**: 优先使用 x-tweet-fetcher (1)
2. **X 快速查询**: 使用 X Quick Search (5)
3. **通用搜索**: 使用 Brave Search (2)
4. **AI 研究**: 使用 Tavily (4)
5. **隐私搜索**: 使用 DuckDuckGo (3)
6. **复杂操作**: 使用 Lobster Browser (6)

## 依赖检查

```bash
# 检查 Camofox 是否运行
netstat -tlnp | grep 9377

# 如未运行，启动 Camofox
cd /root/.openclaw/workspace/camofox-browser && npm start
```

## 执行命令示例

### 优先级 1: x-tweet-fetcher
cd /root/.openclaw/workspace/x-tweet-fetcher
python3 scripts/fetch_tweet.py --user username --limit 10
python3 scripts/x_discover.py --keywords "关键词" --limit 10
python3 scripts/sogou_wechat.py --keyword "关键词" --limit 10

### 优先级 5: X Quick Search
cd /root/.openclaw/workspace
X_SEARCH_QUERY="关键词" python3 x_quick_search.py

### 优先级 2: Brave Search
web_search --query "关键词" --count 10

### 优先级 4: Tavily
# 使用 tavily-search skill

### 优先级 3: DuckDuckGo
# 使用 duckduckgo-search

### 优先级 6: Lobster Browser
cd /root/.openclaw/workspace/lobster-browser-tool
node browser-control.js navigate <url>
