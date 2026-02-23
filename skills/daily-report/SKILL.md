# 日报生成技能

## 日报配置

### 发送时间
- **每天21:00**（北京时间）
- 频道: Discord #日报

### 内容板块（6大板块）

#### 1. AI新闻板块
- 搜索今日最新AI新闻（国内外）
- 重点关注：大模型进展、产品发布、行业动态
- 格式：Top 10列表，每条含标题+摘要+链接
- 工具: `web_search`

#### 2. OpenClaw新闻（10大热门）
- ✅ **单独板块，必须详细**
- **主要信息源**：
  - ClawFeed: http://clawfeed.kevinhe.io/ (4H简报、日报、周报、月报)
  - GitHub: https://github.com/openclaw/openclaw/releases
  - Reddit: r/openclaw
  - Discord社区
  - 官方Blog: https://openclaws.io/blog/
- 格式：Top 10，每条含标题+详细说明+扩展阅读链接
- 工具: `web_fetch` (ClawFeed) + `web_search` + `x_quick_search.py`
- 要求：从ClawFeed获取最新OpenClaw动态

#### 3. 国内外金融新闻
- 与黄金、美股、A股、港股指数影响相关的资讯
- 重点关注：
  - 黄金价格变动及影响因素
  - 美股三大指数（道指、纳指、标普500）
  - A股市场动态
  - 港股市场表现
- 工具: `web_search`

#### 4. 社交媒体动态（AI和OpenClaw热门）

**借鉴ClawFeed的Sources系统管理X博主：**

| 博主 | Source类型 | 内容重点 |
|------|-----------|---------|
| @op7418 | twitter_feed | AIGC周刊、国产AI、产品评测 |
| @dotey | twitter_feed | 提示词工程、AI应用方法论 |
| @SamuelQZQ | twitter_feed | AI视频、编程工具、技术评测 |
| @gkxspace | twitter_feed | 多Agent协作、OpenClaw架构 |
| @yulin807 | twitter_feed | 时间线工具、独立开发 |

- ✅ **已配置X账号登录** (@jswu255)
- 工具: `x_quick_search.py`（类似ClawFeed的twitter_feed抓取）
- 命令：
  ```bash
  cd /root/.openclaw/workspace
  X_SEARCH_QUERY="from:op7418" python3 x_quick_search.py
  X_SEARCH_QUERY="from:dotey" python3 x_quick_search.py
  X_SEARCH_QUERY="from:SamuelQZQ" python3 x_quick_search.py
  X_SEARCH_QUERY="from:gkxspace" python3 x_quick_search.py
  X_SEARCH_QUERY="from:yulin807" python3 x_quick_search.py
  ```
- 要求：总结每位博主今天发的具体内容，不能泛泛而谈

**ClawFeed信息源（推荐）：**
- ClawFeed: http://clawfeed.kevinhe.io/
- 提供OpenClaw相关的4H简报、日报、周报
- 可作为OpenClaw新闻的补充来源

**微信公众号：**
- 财经早餐、香帅的金融江湖、小狼的Eft投资
- 工具: `web_search`
- 要求：深度观点分析，不是简单提及

**YouTube：**
- AI教程、OpenClaw相关视频
- 工具: `web_search`

#### 5. 基金和金融市场表现（保持现状）
- 美股、A股、港股表现
- 大宗商品（黄金、原油）
- 汇率变动
- 工具: `web_search`

#### 6. 天气信息（保持现状）
- **北京天气**（使用天气技能）
- 包含温度、湿度、风力、全天预报
- 工具: `curl wttr.in/Beijing`

## 生成流程

```
1. 获取当前日期 → date +%Y-%m-%d (注意：必须是2026年)
2. AI新闻 → web_search (Top 10)
3. OpenClaw新闻 → web_search + x_quick_search.py (Top 10)
4. 国内外金融新闻 → web_search (黄金、美股、A股、港股)
5. 社交媒体动态 → x_quick_search.py + web_search
6. 基金和金融市场 → web_search
7. 北京天气 → wttr.in
8. 整理成Markdown
9. 发送到Discord
10. 保存到Git: daily/YYYY-MM-DD-日报.md
11. git add → git commit → git push
```

## 日期验证
- **当前年份是2026年，不是2025年！**
- 文件命名: `2026-MM-DD-日报.md`
- 日报标题: `📰 Jamie每日综合日报 — 2026年M月D日`

## 各板块格式要求

### AI新闻（Top 10）
```
**1. [新闻标题]** 🔥
• [要点1]
• [要点2]
• [链接]
```

### OpenClaw新闻（Top 10）
```
**1. [标题]** [emoji]
• [详细说明]
• [影响/意义]
• [扩展阅读链接]
```

### 金融新闻
```
**黄金市场**
• [价格变动]
• [影响因素]
• [链接]

**美股市场**
• [道指/纳指/标普表现]
• [影响因素]
• [链接]

**A股市场**
• [主要指数表现]
• [热点板块]
• [链接]

**港股市场**
• [恒生指数表现]
• [热点板块]
• [链接]
```

### 社交媒体
```
**X博主**
**@[博主名]** - [身份]
• [今天发的具体内容1]
• [今天发的具体内容2]
• [推文链接]

**微信公众号**
**[公众号名]** - [主题]
• [深度观点1]
• [深度观点2]
• [链接]

**YouTube**
• [视频标题] - [频道] - [链接]
```

### 基金和金融市场
```
| 指数/商品 | 价格 | 变动 |
|-----------|------|------|
| [名称] | [价格] | [变动] |
```

### 天气
```
• 天气：[图标] [状况]
• 温度：[温度]
• 湿度：[湿度]
• 风力：[风力]
```

## Git提交信息模板
```
📰 添加2026-MM-DD日报

- AI新闻: [要点]
- OpenClaw: [要点]
- 金融新闻: [要点]
- 社交媒体: [博主/公众号摘要]
- 基金市场: [关键数据]
- 天气: [天气概况]
```

## 注意事项
- OpenClaw必须作为单独板块，Top 10格式
- X博主内容必须具体（今天发了什么），不能泛泛介绍
- 金融新闻要涵盖黄金、美股、A股、港股
- 公众号观点要深入分析，不是简单提及
- 所有外部链接需要可点击
- 每天21:00准时发送
