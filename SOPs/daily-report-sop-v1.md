# Daily Report SOP v1（Jamie专用）

> 目的：把“日报技能”变成可重复执行的标准作业流程，确保**每天稳定交付**。

## 0. 交付定义（Definition of Done）
必须同时满足：
1. 当天文件存在：`daily/YYYY-MM-DD-update.md`（或 `-update2.md`）
2. 只发一份总日报（OpenClaw 融合，不单独二发）
3. A版结构完整（每条：发生了什么 / 为什么重要 / Zoe点评）
4. 重点条目长摘要达标（AI、OpenClaw、公众号建议 220-400 字）
5. 无占位词（未获取/待补/留空/xxxxx/example.com）
6. 已 push 到 `main`，并对 Jamie 回传 commit hash

---

## 1. 每日执行时点
- 建议执行窗口：每日晚间固定时段（如 21:00-23:30）
- 若当天中断，必须在当日补齐，不跨日常态化延期

---

## 2. 第一步：Spy采集流程（强制）
按统一搜索 SOP 执行：`SOPs/search-sop.md`

关键原则（摘要）：
1. `agent-reach` 优先级高于 `multi-search-engine`
2. X 平台优先 `x-reader-repo`
3. YouTube 平台优先 `youtube-watcher`
4. 浏览器自动化兜底时：`pinchtab` 优先于 `agent-browser`

> 执行要求：Spy 必须先完成信息池，Zoe 才能进入点评阶段。
### 必采集板块
- AI 新闻
- OpenClaw（release/blog/community）
- X 博主：@op7418 @dotey @gkxspace @SamuelQZQ @yulin807
- 微信公众号：财经早餐 / 香帅的金融江湖 / 小狼的Eft投资
- 金融市场：美股/A股/港股/黄金/原油/汇率
- 北京天气

### 失败兜底纪律（含X平台）
- 禁止以“限制/找不到”收尾
- 任一源失败时，立即按 `SOPs/search-sop.md` 的平台优先级切换下一工具
- 不再使用历史搜索链路（如 `x-tweet-fetcher` / `search-priority`）
- 必要时用 `web_fetch` 抓正文 + 可信二手源交叉验证

---

## 3. 第二步：Zoe点评与成稿（强制）
### 结构固定
1. 🤖 AI新闻板块
2. 🦞 OpenClaw日报融合板块
3. 🐦 X博主动态（完整解读版）
4. 📱 微信公众号精选
5. 📈 基金与金融市场
6. 🌤️ 北京天气
7. 📌 日报总结

### 写作规则
- 每条都写三段：发生了什么 / 为什么重要 / Zoe点评
- 每条都给可点击链接
- 重点条目写长摘要，不写短bullet敷衍
- 《日报总结》信息压缩与提炼优先使用 **summarize** 技能（用于长文/多链接归纳）

### Zoe点评（关键KPI，硬性要求）
- Zoe点评不是装饰语，必须给**明确判断**：看多/看空、建议继续/暂停、优先级上调/下调、短期机会/长期价值。
- 禁止“中性空话”点评（如：值得关注、持续观察、有一定意义）作为主点评。
- AI、OpenClaw、公众号三大重点板块：每个板块至少 2 条带明确立场的 Zoe点评。
- 《日报总结》必须有“今日洞察”：至少 2 条可执行判断（明天该做什么/不该做什么）。
- 必须新增单独小节《Zoe今日点评》：给出当天一条总判断（方向+风险+动作建议）。
- 若当日信息噪声高，Zoe 需主动做取舍并说明取舍理由（为什么删、为什么留）。

---

## 4. 发布流程（Git）
1. 保存文件到 `daily/YYYY-MM-DD-update*.md`
2. 执行：
   - `git add`
   - `git commit`
   - `git push origin main`
3. 若 push 被拒：
   - `git pull --rebase --autostash origin main`
   - 再 `git push origin main`

提交信息模板：
`📰 添加YYYY-MM-DD update日报（A版）`

---

## 5. 发布前强校验（硬闸）
发布前逐项打勾：
- [ ] 是今天日期文件
- [ ] 单份总日报（已融合 OpenClaw）
- [ ] A版三段式完整
- [ ] Zoe点评密度达标（重点三板块每板块≥2条明确立场）
- [ ] 《日报总结》含至少2条次日可执行判断（已用 summarize 做信息提炼）
- [ ] 含《Zoe今日点评》（方向+风险+动作建议）
- [ ] 重点长摘要达标
- [ ] 关键来源有链接
- [ ] 无占位符/留空结论
- [ ] 已 push main
- [ ] 已回报 commit hash

任一未勾选：禁止发布“已完成”。

---

## 6. 发布后回执模板
```
已产出并推送完成 ✅
- 文件：daily/YYYY-MM-DD-update.md
- 分支：main
- commit：<hash>
```

---

## 7. 复盘触发条件
满足任一条件，必须复盘并修正流程：
- 漏产 / 迟产
- 结构回退（非A版）
- 未 push main
- 缺来源链接
- 被 Jamie 指出“不符合要求”
