---
name: git-sync
description: 当用户说"同步到git"、"上传到git"、"push到git"或类似指令时，自动将 Obsidian 笔记同步到 GitHub。适用于 VPS 和本地 Obsidian 的双向同步场景。
---

# Git 同步 Skill

## 触发条件

当用户说出以下任一指令时触发：
- "同步到git"
- "上传到git"  
- "push到git"
- "提交到git"
- "备份到git"
- "git同步"
- "git上传"

## 工作流程

1. **执行同步脚本**
   ```bash
   /root/.openclaw/workspace/skills/git-sync/scripts/sync-to-git.sh
   ```

2. **脚本会执行以下操作**：
   - 检查是否有未提交的更改
   - 自动添加所有更改 (`git add .`)
   - 自动提交 (`git commit`)
   - 推送到远程 (`git push origin main`)

3. **返回结果给用户**
   - 成功：告知用户同步完成
   - 失败：分析错误原因并提供解决方案

## 注意事项

- 同步的仓库路径：`/root/.openclaw/workspace/obsidian-sync`
- 提交信息格式：`Sync from Zoe: YYYY-MM-DD HH:MM`
- 如果没有更改，会提示"没有需要同步的更改"

## 常见错误处理

### 网络连接失败
如果提示无法连接 GitHub，建议用户：
1. 检查网络连接
2. 使用 VPN/代理
3. 考虑改用 Gitee（国内访问更快）

### 权限错误
如果提示权限不足，检查：
1. GitHub Token 是否有效
2. 仓库权限是否正确

## 扩展功能

未来可支持：
- 同步前预览更改内容
- 自定义提交信息
- 同步特定文件夹
- 双向同步（自动拉取远程更改）
