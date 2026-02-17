#!/bin/bash
# 清理过期 memory 日志（保留最近7天）

MEMORY_DIR="/root/.openclaw/workspace/memory"
CUTOFF_DATE=$(date -d '7 days ago' +%Y-%m-%d)

cd "$MEMORY_DIR" 2>/dev/null || exit 0

for file in 2*.md; do
    # 提取文件名中的日期 (YYYY-MM-DD.md)
    file_date="${file%.md}"
    if [[ "$file_date" < "$CUTOFF_DATE" ]]; then
        echo "Removing old log: $file"
        rm "$file"
    fi
done
