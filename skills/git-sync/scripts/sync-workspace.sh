#!/bin/bash
# 自动同步 workspace 配置文件到 Git
# 每天运行，将 /root/.openclaw/workspace/ 下的关键文件同步到 obsidian-sync/workspace/

SOURCE_DIR="/root/.openclaw/workspace"
TARGET_DIR="/root/.openclaw/workspace/obsidian-sync/workspace"

echo "🔄 开始同步 workspace 文件..."
echo "⏰ 时间: $(date '+%Y-%m-%d %H:%M:%S')"

# 确保目标目录存在
mkdir -p "$TARGET_DIR"

# 同步关键文件
files=("IDENTITY.md" "SOUL.md" "USER.md" "MEMORY.md" "AGENTS.md" "TOOLS.md" "BOOTSTRAP.md" "HEARTBEAT.md")

for file in "${files[@]}"; do
    if [ -f "$SOURCE_DIR/$file" ]; then
        cp "$SOURCE_DIR/$file" "$TARGET_DIR/"
        echo "  ✅ 已同步: $file ($(stat -c%s "$SOURCE_DIR/$file") bytes)"
    else
        echo "  ⚠️  文件不存在: $file"
    fi
done

# 同步 memory 文件夹（如果存在）
if [ -d "$SOURCE_DIR/memory" ]; then
    mkdir -p "$TARGET_DIR/memory"
    cp -r "$SOURCE_DIR/memory/"* "$TARGET_DIR/memory/" 2>/dev/null || true
    echo "  ✅ 已同步: memory/ 文件夹"
fi

# 同步 skills 文件夹（如果存在）
if [ -d "$SOURCE_DIR/skills" ]; then
    mkdir -p "$TARGET_DIR/skills"
    cp -r "$SOURCE_DIR/skills/"* "$TARGET_DIR/skills/" 2>/dev/null || true
    echo "  ✅ 已同步: skills/ 文件夹"
fi

echo "✅ Workspace 文件同步完成"

# 执行 Git 同步
cd /root/.openclaw/workspace/obsidian-sync || exit 1

# 先拉取远程最新更改
echo "📥 拉取远程最新更改..."
git pull origin main || echo "⚠️ 拉取失败，继续本地同步"

# 检查是否有更改
if git diff --quiet && git diff --staged --quiet; then
    echo "📦 Git: 没有需要同步的更改"
    echo "✅ 同步检查完成，无需提交"
    exit 0
fi

# 添加所有更改
echo "📤 添加更改到暂存区..."
git add .

# 提交更改
echo "💾 提交更改..."
git commit -m "Sync workspace files: $(date '+%Y-%m-%d %H:%M')" || true

# 推送到远程
echo "🚀 推送到 GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo "🎉 已成功同步到 GitHub!"
else
    echo "❌ Git 同步失败"
    exit 1
fi
