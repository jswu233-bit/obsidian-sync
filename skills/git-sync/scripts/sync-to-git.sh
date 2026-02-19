#!/bin/bash
# Git Sync Helper Script for Obsidian
# 自动同步 Obsidian 笔记到 GitHub

REPO_DIR="/root/.openclaw/workspace/obsidian-sync"

cd "$REPO_DIR" || exit 1

echo "🔄 开始同步到 Git..."

# 检查是否有更改
if git diff --quiet && git diff --staged --quiet; then
    echo "✅ 没有需要同步的更改"
    exit 0
fi

# 添加所有更改
git add .

# 提交更改
git commit -m "Sync from Zoe: $(date '+%Y-%m-%d %H:%M')" || true

# 推送到远程
git push origin main

if [ $? -eq 0 ]; then
    echo "✅ 同步成功！"
else
    echo "❌ 同步失败"
    exit 1
fi
