#!/bin/bash
# Obsidian Sync Helper Script
# 运行在 VPS 上，用于同步笔记到 Obsidian

REPO_DIR="/root/.openclaw/workspace/obsidian-sync"
REMOTE_URL=""  # 待配置：填入你的 Git 仓库地址

cd "$REPO_DIR"

# 配置远程仓库（首次运行）
setup_remote() {
    if [ -z "$REMOTE_URL" ]; then
        echo "❌ 请先编辑此脚本，设置 REMOTE_URL"
        exit 1
    fi
    git remote add origin "$REMOTE_URL" 2>/dev/null || true
    echo "✅ 远程仓库已配置"
}

# 拉取最新内容
pull() {
    git pull origin main
}

# 推送本地更改
push() {
    git add .
    git commit -m "Zoe update: $(date '+%Y-%m-%d %H:%M')" || true
    git push origin main
}

# 创建新笔记到 inbox
create_note() {
    local filename="$1"
    local content="$2"
    local filepath="$REPO_DIR/inbox/$(date +%Y%m%d)_${filename}.md"
    
    echo -e "# ${filename}\n\n${content}\n\n---\n*Created by Zoe at $(date '+%Y-%m-%d %H:%M')*" > "$filepath"
    echo "✅ 笔记已创建: $filepath"
}

case "$1" in
    setup)
        setup_remote
        ;;
    pull)
        pull
        ;;
    push)
        push
        ;;
    create)
        create_note "$2" "$3"
        ;;
    *)
        echo "用法: $0 {setup|pull|push|create <filename> <content>}"
        ;;
esac
