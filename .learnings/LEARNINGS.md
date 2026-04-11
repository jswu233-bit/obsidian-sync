## [LRN-20260401-001] correction

**Logged**: 2026-04-01T01:25:00+08:00
**Priority**: high
**Status**: pending
**Area**: config

### Summary
用户明确纠正票务检索时间窗：不要“近一年新票”，应默认“近一个月”。

### Details
在 Discord ticket 线程中，用户指出 Spy_Bot 的新票设定时间范围过长（近一年），导致结果不符合预期。用户要求将默认窗口收敛到近一个月。

### Suggested Action
后续涉及“新票/近期票务”检索时，默认时间窗使用近30天（近一个月）；除非用户明确指定更长区间。

### Metadata
- Source: user_feedback
- Related Files: AGENTS.md
- Tags: ticketing,default-window,correction

---
## [LRN-20260411-001] correction

**Logged**: 2026-04-11T00:45:00+08:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
用户要求 Spy 日报恢复为“昨天那版”的固定输出格式，不接受随意改版。

### Details
在 ticket 线程中，用户明确表示“今天跑的不太行”，要求“再按照昨天跑的内容格式跑给我”。这说明日报不仅要内容正确，还要保持既有版式稳定，尤其是按 A 版模板输出（每条：发生了什么 / 为什么重要 / Zoe 点评）。

### Suggested Action
后续跑 Spy 日报时，默认沿用已确认的昨日格式/A版模板；若要改版，必须先征得用户同意。

### Metadata
- Source: user_feedback
- Related Files: MEMORY.md
- Tags: report-format,spy,daily-report,correction

---
## [LRN-20260411-002] correction

**Logged**: 2026-04-11T12:46:00+08:00
**Priority**: high
**Status**: pending
**Area**: messaging

### Summary
用户指出我在 Discord 里对同一问题重复回复，要求反思并避免再次发生。

### Details
在 #assistant 频道中，用户明确反馈“你每次都回答两遍”。这说明我对重复触发/重复消息缺少去重判断，导致同一轮问题出现重复作答，影响体验。

### Suggested Action
后续在 Discord 尤其是群聊场景中，先检查是否已对同一问题作答；若是重复触发或同内容重复投递，默认不重复展开回复，优先简短确认或静默跳过。

### Metadata
- Source: user_feedback
- Related Files: AGENTS.md
- Tags: discord,dedup,messaging,correction

---
## [LRN-20260411-003] best_practice

**Logged**: 2026-04-11T21:40:00+08:00
**Priority**: medium
**Status**: pending
**Area**: tools

### Summary
使用 `web_search` 时不能同时传 `freshness` 和 `date_after/date_before`；执行日报前应先固定时间过滤策略。

### Details
本次日报采集过程中，多次对 `web_search` 同时传入 freshness 与日期区间，工具返回 `conflicting_time_filters`。这会打断采集节奏，并浪费日报窗口时间。

### Suggested Action
后续搜索任务开始前先决定使用“freshness”还是“date range”其中一种；默认优先日期区间，除非用户只要求近 day/week/month 粗粒度检索。

### Metadata
- Source: error
- Related Files: SOPs/search-sop.md
- Tags: web_search,time-filters,search-sop,best-practice

---
## [LRN-20260411-004] best_practice

**Logged**: 2026-04-11T21:41:00+08:00
**Priority**: medium
**Status**: pending
**Area**: tools

### Summary
依赖 `summarize` 技能前，先确认本机已安装 `summarize` CLI；未安装时先补装再执行总结步骤。

### Details
本次日报执行到《日报总结》阶段时，按 SOP 调用 `summarize`，但本机 initially 返回 `command not found`。后续通过 Homebrew 安装 `steipete/tap/summarize` 后恢复可用。

### Suggested Action
凡是 SOP 明确要求使用 summarize 的任务，先执行 `which summarize` 检查环境；若缺失则先安装，再继续生成总结段，避免中途返工。

### Metadata
- Source: error
- Related Files: SOPs/daily-report-sop-v1.md
- Tags: summarize,cli,dependency,environment,best-practice
