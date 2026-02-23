#!/bin/bash
# 记忆管理脚本 - 每天自动执行
# 功能：
# 1. 清理7天前的日记文件
# 2. 提醒归档重要信息到 MEMORY.md

MEMORY_DIR="/root/.openclaw/workspace/memory"
DAYS_TO_KEEP=7

echo "=== 记忆管理 - $(date '+%Y-%m-%d %H:%M') ==="
echo ""

# 1. 显示最近7天的日记
echo "📂 最近${DAYS_TO_KEEP}天日记文件："
find ${MEMORY_DIR} -name "*.md" -type f -mtime -${DAYS_TO_KEEP} | sort | while read file; do
    filename=$(basename "$file")
    size=$(du -h "$file" | cut -f1)
    echo "  ✓ ${filename} (${size})"
done
echo ""

# 2. 显示即将被清理的文件（7天前）
echo "🗑️ 即将被清理的文件（超过${DAYS_TO_KEEP}天）："
count=0
find ${MEMORY_DIR} -name "*.md" -type f -mtime +${DAYS_TO_KEEP} | while read file; do
    filename=$(basename "$file")
    echo "  × ${filename}"
    count=$((count + 1))
done

if [ $count -eq 0 ]; then
    echo "  （无）"
else
    echo ""
    echo "⚠️  这些文件将在下次清理时删除"
fi
echo ""

# 3. 检查今日日记是否存在
today="$(date '+%Y-%m-%d').md"
if [ ! -f "${MEMORY_DIR}/${today}" ]; then
    echo "📝 今日日记 (${today}) 尚未创建"
else
    echo "📝 今日日记已创建"
    
    # 检查是否有需要归档的内容
    if grep -q "⭐ 长期记忆" "${MEMORY_DIR}/${today}" 2>/dev/null; then
        echo ""
        echo "⚡ 检测到需要归档的内容（标记 ⭐ 长期记忆）："
        grep -A 2 "⭐ 长期记忆" "${MEMORY_DIR}/${today}" | head -10
        echo ""
        echo "💡 请手动更新到 MEMORY.md"
    fi
fi
echo ""

# 4. 显示 MEMORY.md 统计
echo "📊 长期记忆文件统计："
memory_size=$(du -h /root/.openclaw/workspace/MEMORY.md | cut -f1)
echo "  MEMORY.md: ${memory_size}"
echo ""

echo "=== 记忆管理完成 ==="
