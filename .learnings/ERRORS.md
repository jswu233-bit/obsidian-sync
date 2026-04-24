# ERRORS


## [ERR-20260424-001] message-tool-discord-send-schema

**Logged**: 2026-04-24T13:32:44Z
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
Discord `message.send` failed during daily report delivery because the tool schema unexpectedly required non-empty `components.modal.fields` and then non-empty `components.blocks[0].text`, even for a plain text send attempt.

### Error
```
components.modal.fields must be a non-empty array
components.blocks[0].text cannot be empty
```

### Context
- Operation attempted: send daily report to Discord channel `1472964925696512000`
- Tool: `message`
- Parameters: plain text message with `channelId` only, then a retry with placeholder components
- Expected behavior: allow a minimal plain text send without requiring component payloads

### Suggested Fix
Document the minimum valid `message.send` payload for Discord in OpenClaw, or relax schema validation so plain text sends do not require component objects.

### Metadata
- Reproducible: yes
- Related Files: /Users/jamiewu/.openclaw/workspace/daily/2026-04-24-update.md

---

## [ERR-20260423-001] git pull --rebase --autostash blocked by untracked file

**Logged**: 2026-04-23T13:43:53.412333+00:00
**Priority**: medium
**Status**: pending
**Area**: infra

### Summary
日报发布时，`git push origin main` 被远端领先拒绝，随后 `git pull --rebase --autostash origin main` 又被未跟踪文件 `memory/2026-04-22.md` 阻塞，导致自动发布中断。

### Error
```
error: The following untracked working tree files would be overwritten by checkout:
	memory/2026-04-22.md
Aborting
error: could not detach HEAD
```

### Context
- Operation attempted: 日报 git 提交并 push main
- Trigger: remote main ahead of local
- Workspace: /Users/jamiewu/.openclaw/workspace

### Suggested Fix
在 rebase 前先安全转移或备份冲突的未跟踪文件，再执行 `git pull --rebase --autostash origin main` 与 `git push origin main`。

### Metadata
- Reproducible: yes
- Related Files: memory/2026-04-22.md, daily/2026-04-23-update.md

---
