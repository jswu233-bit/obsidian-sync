## [LRN-20260616-001] correction

**Logged**: 2026-06-16T22:47:00+08:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
不要把用户对当前会话入口的短句纠正，直接泛化成长期的群聊回复规则。

### Details
在 `webchat` 直聊会话中，用户发来“不能群聊”。我一度把它扩写理解成“以后不在群聊主动说话”的稳定边界，并尝试写入长期记忆。正确做法是先核对当前会话 metadata 与用户当下语境：这句话是在纠正我对当前入口/场景的判断，而不是授权我新建一条更广的跨场景规则。

### Suggested Action
凡遇到“群聊 / 频道 / @规则 / 不能群聊”这类短句，先核对当前 channel、surface、chat_type，再决定是记录为场景纠正，还是提升为长期规则。

### Metadata
- Source: conversation
- Related Files: memory/2026-06-16.md, MEMORY.md
- Tags: correction, context, chat-boundary, memory

---
