# Daily Report SOP v1（Jamie专用）

> 目标：确保日报稳定、可验证、只发 #daily。

## 0. 交付定义（DoD）
必须同时满足：
1. 当天文件存在：`daily/YYYY-MM-DD-update.md`（或 `-update2.md`）
2. 只发一份总日报（OpenClaw 融合，不单独二发）
3. A版结构完整（每条：发生了什么 / 为什么重要 / Zoe点评）
4. 重点条目长摘要达标（AI、OpenClaw、公众号建议 220-400 字）
5. 无占位词（未获取/待补/留空/xxxxx/example.com）
6. 已 push 到 `main`，并回传 commit hash

---

## 1. 第一步：Spy采集流程（强制）
按全局搜索技能执行：`skills/search-priority/SKILL.md`

固定顺序：
1. Pinchtab
2. x-reader
3. multi-search-engine
4. x-tweet-fetcher
5. Brave（`web_search`）

必采集板块：
- AI 新闻
- OpenClaw（release/blog/community）
- X 博主：@op7418 @dotey @gkxspace @SamuelQZQ @yulin807
- 微信公众号：财经早餐 / 香帅的金融江湖 / 小狼的Eft投资
- 金融市场：美股/A股/港股/黄金/原油/汇率
- 北京天气

失败兜底纪律：
- 禁止以“限制/找不到”收尾
- 任一源失败时，立即降级到下一个工具
- 若 X 无法直读，按顺序降级，不得直接结束
- 必要时 `web_fetch` + 二手源交叉验证

---

## 2. 第二步：Zoe点评与成稿（强制）
结构固定：
1. 🤖 AI新闻板块
2. 🦞 OpenClaw日报融合板块
3. 🐦 X博主动态
4. 📱 微信公众号精选
5. 📈 基金与金融市场
6. 🌤️ 北京天气
7. 📌 日报总结

写作规则：
- 每条三段：发生了什么 / 为什么重要 / Zoe点评
- 每条都给可点击链接
- 重点条目写长摘要
- 《日报总结》信息提炼优先用 summarize

Zoe点评硬规则：
- 必须给明确立场（继续/暂停、上调/下调、短期/长期）
- 禁止“值得关注”类空话
- AI/OpenClaw/公众号三板块各≥2条明确立场点评
- 《日报总结》至少2条次日可执行判断
- 必须含《Zoe今日点评》（方向+风险+动作建议）

---

## 3. 发布流程（Git）
1. 保存到 `daily/YYYY-MM-DD-update*.md`
2. `git add` -> `git commit` -> `git push origin main`
3. 若 push 被拒：`git pull --rebase --autostash origin main` 后重推

---

## 4. 发送约束（硬闸）
- 只允许发送到 Discord `#daily`（channelId: `1472964925696512000`）
- 非该频道：直接终止，不发送

### 发送重试机制（新增）
- 首次发送失败时，自动重试最多 3 次（总计最多 4 次尝试）
- 重试间隔建议：30秒 / 90秒 / 180秒
- 重试过程中禁止改发其他频道，必须保持 `#daily`
- 任一重试成功即停止；全部失败则在回执中写清失败原因与各次尝试结果

---

## 5. 发布前强校验
- [ ] 今天日期文件存在
- [ ] 单份总日报（已融合 OpenClaw）
- [ ] A版三段式完整
- [ ] Zoe点评密度达标（重点三板块各≥2条）
- [ ] 《日报总结》含≥2条次日可执行判断（已用 summarize）
- [ ] 含《Zoe今日点评》
- [ ] 重点长摘要达标
- [ ] 链接齐全
- [ ] 无占位词/留空
- [ ] 已 push main
- [ ] 已回报 commit hash

任一未勾选：禁止报“完成”。
