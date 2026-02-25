---
name: git-sync
description: 当用户说"同步到git"、"上传到git"、"push到git"或类似指令时，自动将 workspace 文件同步到 GitHub。适用于所有对话频道，全局有效。
---

# Git 同步 Skill

## 触发条件（全局有效）

**在任何对话频道中**，当用户说出以下任一指令时触发：
- "同步到git" / "同步到 git"
- "上传到git" / "上传到 git"
- "push到git" / "push 到 git"
- "提交到git" / "提交到 git"
- "备份到git"
- "git同步" / "git 同步"
- "git上传" / "git 上传"

## 同步内容

执行以下同步脚本：
```bash
/root/.openclaw/workspace/skills/git-sync/scripts/sync-workspace.sh
```

### 同步的文件包括：
1. **核心配置文件**
   - IDENTITY.md
   - SOUL.md
   - USER.md
   - MEMORY.md
   - AGENTS.md
   - TOOLS.md
   - BOOTSTRAP.md
   - HEARTBEAT.md

2. **记忆文件夹**
   - memory/YYYY-MM-DD.md

3. **技能文件夹**
   - skills/ 所有技能文件

### 同步目标
- **GitHub 仓库**: https://github.com/jswu233-bit/obsidian-sync
- **本地路径**: `/root/.openclaw/workspace/obsidian-sync/workspace/`

## 工作流程

1. **复制文件** - 将 workspace 文件复制到 obsidian-sync/workspace/
2. **拉取远程** - git pull origin main（避免冲突）
3. **检查更改** - git status
4. **添加更改** - git add .
5. **提交更改** - git commit -m "Sync: 时间戳"
6. **推送到 GitHub** - git push origin main

## 自动同步

**每天凌晨 2:00（北京时间）自动执行**
- Cron 任务: `sync-workspace-to-git-daily`
- 自动同步所有 workspace 文件到 GitHub

## 注意事项

- 此技能在所有对话频道中全局有效
- 用户不需要指定路径，自动同步 workspace 根目录
- 如果网络连接失败，会提示错误信息

## 常见错误

### 网络连接失败
```
fatal: unable to access 'https://github.com/...': Failed to connect
```
**解决**: 检查网络或稍后重试

### 权限错误
```
Permission denied
```
**解决**: GitHub Token 可能过期，需要更新
