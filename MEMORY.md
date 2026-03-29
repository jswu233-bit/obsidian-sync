# MEMORY.md - 核心记忆


## 一、记忆部分

### 1) 记忆管理与架构（合并更新：2026-03-29）
- 每天写 `memory/YYYY-MM-DD.md` 日记（daily memory 不能断档）。
- `MEMORY.md` 仅保留长期规则/稳定偏好/关键决策；原始事实留在 daily memory。
- 飞书表格仅做第三层索引与管理视图，不存全量细节。
- 凡涉及“历史决策/用户偏好/既有规则”，先检索记忆再回答。
- Jamie 明确要求“记住/写进记忆”时：直接同步写入 daily memory 与飞书索引。

### 2) 判例库（CASE）写法（固定）
- 除纯索引信息外，长期记忆统一按 CASE 模板记录。
- 模板如下：

```md
### [CASE-YYYYMMDD-序号] 标题
- 场景：
- 判断：
- 动作：
- 验收：
- 回退：
- type: decision|todo|risk|insight
- temp: H|W|C
```

### 3) Hot/Warm/Cold 温度分层与检索策略（固定）
- H（Hot）：7天内高频会用
- W（Warm）：8-30天可能复用
- C（Cold）：30天+低频归档
- 检索策略：
  - Hot / Warm：优先精确匹配（daily 原文/精确索引）
  - Cold：优先模糊匹配（语义召回/向量化思路）后再回原文校验
- 执行顺序：先飞书索引定位条目，再回读对应 daily memory 详情。

### 4) 主动遗忘机制（固定）
- 每周执行一次一删（执行清单包含三项）：
  1. 删重复（同结论多版本只留最新）
  2. 删过期（已失效流程/入口）
  3. 删无行动价值（不能指导下次动作）

### 5) 长期层写入门槛（固定）
- 进入 `MEMORY.md` / 飞书索引的内容必须是：
  - decision
  - todo
  - risk
  - insight
- 其他内容全部留在 `daily memory`。

### 6) 飞书索引层主表（写入：2026-03-20）
- URL: `https://fhevyxypcl.feishu.cn/base/NTQnbfnthaTIMxsziNzcJaGNnld?table=tblez1cogebbBzwu&view=vewmQ6sC7t`
- app_token: `NTQnbfnthaTIMxsziNzcJaGNnld`
- table_id: `tblez1cogebbBzwu`
- view_id: `vewmQ6sC7t`
- 每次新增/更新 `memory/YYYY-MM-DD.md` 后，必须同步写入飞书索引（至少字段：`文本/type/status/priority/source/写入日期`）。
- 每条长期项同步一条飞书索引，并补充 `temp`（H/W/C）。
- 新增外部系统关键入口（表格/看板/文档）当天同步写入 `MEMORY.md`（URL + 唯一ID + 用途）。

### 7) 教训库纳入规则（写入：2026-03-21）
- 教训来源固定为工作区 `.learnings/`：`LEARNINGS.md`、`ERRORS.md`、`FEATURE_REQUESTS.md`。
- 出现可复用教训（失败根因/用户纠正/最佳实践）时，当天同步：
  1. 先写入 `.learnings/` 对应文件；
  2. 同步写入 `memory/YYYY-MM-DD.md`；
  3. 同步更新飞书索引表；
  4. 再在 `MEMORY.md` 记录长期适用结论与执行约束。
- 同类错误连续出现 2 次，必须升级沉淀到长期记忆与规范文件（`MEMORY.md` + `AGENTS.md/TOOLS.md/SOUL.md` 视类型归档）。

---

## 二、Skill 部分

### 1) 安装路径规则（写入：2026-03-21）
- 因多人/多 agent 共用，skills 统一放在 `~/.openclaw/` 目录下。
- 后续新增/安装 skill 默认安装到 `~/.openclaw/`，不放其他分散路径（除非 Jamie 另行指定）。

### 2) 清单维护规则（写入：2026-03-21）
- 在 `~/.openclaw/skills/` 维护 `SKILL_LIST.md`，记录所有 skill 简介。
- 当发生 skill 安装或删除时，必须同步更新 `SKILL_LIST.md`（新增/移除对应条目）。

---

## 三、日报部分

### 1) 报告完整性纪律（写入：2026-03-14）
- 若 Spy 报告“因限制找不到”，Zoe 必须推动立即切换备用链路，不接受留空。
- 备用顺序：原工具失败 → `web_search`/site 定向检索 → `web_fetch` 抓正文 → 可信二手源交叉验证。
- 日报最终稿禁止出现“未获取/留空/无法获取”等结论。

### 2) 交付规则（写入：2026-03-19）
- 日报按 A 版模板执行（每条：发生了什么 / 为什么重要 / Zoe 点评）。
- 只发一份总日报（OpenClaw 内容融合其中），不再单独发第二份 OpenClaw 日报。
- 当天产出并 push 到 `main`；回复中必须给 commit hash。

## 四、主动性边界 SOP（写入：2026-03-21）
- 新增 SOP：`SOPs/proactive-boundary-v1.md`（Zoe 主动性边界 v1）。
- 触发分级：
  - P0：即时发；
  - P1：同类合并后发（默认 2 小时最多 1 条）；
  - P2：不主动发，用户询问时统一汇总。
- 主动消息固定三行：发生了什么 / 影响是什么 / 建议怎么做（A/B）。
- 主动提案必须包含：收益、成本、回退方案。
- 心跳巡检项：模型可用性、任务卡住、自动化异常；正常静默记录，异常按 P0/P1 分级提醒。

## 五、每日记忆维护提醒执行规则（写入：2026-03-22）
- 当收到 daily-memory-log-creator 类 cron 提醒时，按固定顺序执行：
  1) 检查 `memory/YYYY-MM-DD.md` 是否存在，不存在则按模板创建（今日任务、重要事件⭐、待跟进、已完成、对话要点）；
  2) 从当日对话提炼“长期有效规则/关键决策”并同步到 `MEMORY.md`；
  3) 同步写入飞书索引主表（字段至少：`文本/type/status/priority/source/写入日期`）；
  4) 若无新增，必须显式写明“今日无新增长期记忆”或“今日无新增飞书索引”；
  5) 执行固定提交命令：`git add memory MEMORY.md .learnings || true && git commit -m "chore(memory): daily log + memory+feishu index sync" || true`。
- 本规则属长期生效 SOP，默认 `status=active`，优先级 `high`。

