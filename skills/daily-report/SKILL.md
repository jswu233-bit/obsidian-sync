# 日报生成技能（Jamie专用 · A版）

## 目标
产出**一份**“精炼且详细”的总日报（含 OpenClaw 融合板块），可直接阅读做判断，不依赖读者点链接。

> 执行SOP（强制）：`/Users/jamiewu/.openclaw/workspace/SOPs/daily-report-sop-v1.md`

---

## 固定分工
- **Spy（搜集）**：负责全网检索与原始信息收集。
- **Zoe（主编）**：负责筛选、归纳、判断、点评、成稿与发布。

---

## 领导纪律（强制）
1. Spy 不得以“平台限制/接口限制/抓取失败”结束任务。
2. 只要有缺口，Zoe 必须继续推动 Spy 当轮补齐。
3. 兜底链路必须按顺序执行：
   - 原工具
   - `web_search`（site 定向）
   - `web_fetch`（抓正文）
   - 可信二手源交叉验证
4. 最终稿禁止出现：`未获取` / `留空` / `待补` / `xxxxx` / `example.com`。

---

## 输出风格（A版，强制）
每条必须三段：
1) **发生了什么**（事实）
2) **为什么重要**（影响）
3) **Zoe点评**（判断）

### 长摘要要求（2026-03-14新增，强制）
- 重点条目（AI新闻 / OpenClaw融合 / 公众号精选）每条必须提供**几百字级别摘要**（建议 220-400 字）。
- 摘要必须讲清：背景、核心事实、关键细节、影响与风险。
- 禁止只写一句话标题或两三个 bullet 充数。
- 用户不点链接也应能理解文章主要内容与结论。

每条都要有可点击链接（无原文直链时给检索页并注明）。

---

## 日报结构（单份总日报，强制顺序）
标题：`# 📰 Jamie每日综合日报 - YYYY年M月D日（Update版）`

顶部说明：更新时间 + 版本说明（A版）

正文顺序：
1. 🤖 AI新闻板块
2. 🦞 OpenClaw日报融合板块（Top更新 + Zoe点评）
3. 🐦 X博主动态（完整解读版）
4. 📱 微信公众号精选
5. 📈 基金与金融市场
6. 🌤️ 北京天气
7. 📌 日报总结（今日热点 + 今日洞察）

> 注意：OpenClaw内容必须融合在总日报中，禁止再单独发第二份 OpenClaw 日报。

---

## 搜索工具栈（固定优先级）
1. **Pinchtab** - 浏览器自动化采集
2. **x-reader** - 多平台内容抓取
3. **multi-search-engine** - 多引擎聚合
4. **x-tweet-fetcher** - X/Twitter 专用
5. **Brave Search (`web_search`)** - 通用网页搜索

> 规则：上游工具失败必须立即降级到下一个工具，不得停在“因限制找不到”。

## 必覆盖源
### AI & OpenClaw
- OpenClaw Releases: https://github.com/openclaw/openclaw/releases
- OpenClaw Blog: https://openclaws.io/blog/
- ClawFeed: http://clawfeed.kevinhe.io/
- Reddit: r/openclaw / r/LocalLLaMA / r/LocalLLM
- V2EX / HN / Qiita / Zenn（有更新就纳入）

### X博主（优先覆盖）
- @op7418
- @dotey
- @gkxspace
- @SamuelQZQ
- @yulin807

每人至少 1 条具体观点：
- 发生了什么
- 为什么重要
- Zoe点评
- 链接

### 微信公众号（优先）
- 财经早餐
- 香帅的金融江湖
- 小狼的Eft投资

---

## 生成流程
### Phase 1：Spy搜集（必须完整）
Spy 任务要求：
- AI新闻 Top（国内外）
- OpenClaw Top 更新（release/blog/community）
- X博主观点
- 微信公众号文章
- 金融市场（美股/A股/港股/黄金/原油/汇率）
- 北京天气

### Phase 2：Zoe主编（A版成稿）
- 删除噪音，保留高信号内容
- 每条改写为 A版三段
- Zoe点评必须是明确立场判断（继续/暂停、上调/下调、短期/长期），禁止空话点评
- 《日报总结》至少给出 2 条次日可执行判断

### Phase 3：发布与归档
- 文件路径：`daily/YYYY-MM-DD-update*.md`
- Git 分支：`main`
- 必须执行：`git add -> git commit -> git push origin main`
- 回报 commit hash

---

## 质量门槛（过线才可发）
- [ ] 只发**一份**总日报（含OpenClaw融合）
- [ ] 每条都有“发生了什么/为什么重要/Zoe点评”
- [ ] Zoe点评密度达标（AI/OpenClaw/公众号三板块各≥2条明确立场）
- [ ] 《日报总结》含至少2条次日可执行判断
- [ ] X五位优先博主尽量覆盖
- [ ] 无占位符、无留空结论
- [ ] 所有关键结论有可点击来源
- [ ] 已推送到 `main`

---

## Git 提交信息模板
`📰 添加YYYY-MM-DD update日报（A版）`

正文简述：
- A版重写
- OpenClaw融合
- X/公众号/金融/天气齐全
- commit + push 到 main
