#!/bin/bash
# 自动同步 obsidian-sync 仓库到 Git
# 每天凌晨 2 点运行

REPO_DIR="/root/.openclaw/workspace/obsidian-sync"

echo "🔄 开始同步 obsidian-sync 到 Git..."
echo "📁 仓库路径: $REPO_DIR"
echo "⏰ 时间: $(date '+%Y-%m-%d %H:%M:%S')"

cd "$REPO_DIR" || exit 1

# 先拉取远程最新更改（避免冲突）
echo "📥 拉取远程最新更改..."
git pull origin main || echo "⚠️ 拉取失败，继续本地同步"

# 检查是否有更改
if git diff --quiet && git diff --staged --quiet; then
    echo "📦 没有需要同步的更改"
    echo "✅ 同步检查完成，无需提交"
    exit 0
fi

# 添加所有更改
echo "📤 添加更改到暂存区..."
git add .

# 提交更改
echo "💾 提交更改..."
git commit -m "Auto sync: $(date '+%Y-%m-%d %H:%M')" || true

# 推送到远程
echo "🚀 推送到 GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo "🎉 已成功同步到 GitHub!"
else
    echo "❌ Git 同步失败，请检查网络或权限"
    exit 1
fi
