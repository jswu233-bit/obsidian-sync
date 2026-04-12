## [LRN-20260412-003] correction

**Logged**: 2026-04-12T16:18:00+08:00
**Priority**: high
**Status**: pending
**Area**: messaging

### Summary
用户明确纠正：Discord `#ll` 频道里，Zoe 不用回复；该频道应由 Eva 承接，Zoe 保持静默。

### Details
用户直接说“这个频道不用Zoe来回复”。这比此前的“@谁，谁说话”更进一步，说明在该频道的实际偏好里，Zoe 不仅不应代答 `Eva_Bot`，而且即使被提及，也不应继续参与普通回复。此前我仍有越界回复与过程外显，造成干扰。

### Suggested Action
后续在 Discord `#ll` 频道：
1. Zoe 默认静默；
2. 与亲密关系沟通、小F相关记忆与回复全部交由 Eva；
3. 若用户再次对 Zoe 说 `/stop` 或说明“不用Zoe回复”，视为本频道长期静默指令，除非用户明确撤销。

### Metadata
- Source: user_feedback
- Related Files: memory/2026-04-12.md, AGENTS.md
- Tags: discord,channel-boundary,zoe,stop,correction

---

## [LRN-20260412-004] correction

**Logged**: 2026-04-12T17:20:00+08:00
**Priority**: high
**Status**: pending
**Area**: messaging

### Summary
用户明确要求：Zoe 说话要简洁直接，减少啰嗦，并将这一偏好写入 SOUL。

### Details
在 Discord 对话中，用户直接反馈“你说话太啰嗦了，我希望你说话简洁直接一些。写入你的soul”。这属于明确的风格纠正，不是临时偏好。后续默认回复应更短、更直接，少铺垫、少重复、少解释式废话。

### Suggested Action
1. 将“默认简洁直接”写入 `SOUL.md`；
2. 后续先给结论，再按需展开；
3. 非复杂任务避免长段分析式回复。

### Metadata
- Source: user_feedback
- Related Files: SOUL.md
- Tags: style,concise,discord,correction

---

## [LRN-20260412-005] best_practice

**Logged**: 2026-04-12T21:23:00+08:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
`SOPs/daily-report-sop-v1.md` 需要视为受保护文件，不能再被 sync / 覆盖 / 清理流程顺手删除。

### Details
用户明确要求“就不要再把这个文件丢了”。此前该文件多次在 `sync(core)` 提交中被删除，说明仅靠记忆或临时恢复不够，必须把它升级为受保护 SOP，并在执行同步类操作后显式校验是否仍存在。

### Suggested Action
1. 在 `AGENTS.md` 中加入保护规则；
2. 后续执行 sync / 覆盖 / 清理后，必须检查该文件是否存在；
3. 若丢失，立即恢复再继续。

### Metadata
- Source: user_feedback
- Related Files: AGENTS.md, SOPs/daily-report-sop-v1.md
- Tags: sop,protection,sync,docs,best_practice

---
