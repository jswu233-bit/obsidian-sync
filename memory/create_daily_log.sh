#!/bin/bash
# 自动创建每日 memory 日记文件

MEMORY_DIR="/root/.openclaw/workspace/memory"
TODAY=$(date +%Y-%m-%d)
FILE="$MEMORY_DIR/$TODAY.md"

# 如果文件已存在，不创建
if [ -f "$FILE" ]; then
    echo "✅ 日记文件已存在: $FILE"
    exit 0
fi

# 创建日记文件
cat > "$FILE" << EOF
# $TODAY 工作日志

## 今日完成

### 1. 

### 2. 

### 3. 

## 重要对话

## 待办事项
- [ ] 

---
*记录时间: $TODAY*
EOF

echo "📝 已创建日记文件: $FILE"
