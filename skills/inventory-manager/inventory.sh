#!/bin/bash
# 囤货管理脚本

INVENTORY_FILE="/root/.openclaw/workspace/inventory/囤货清单.md"
BACKUP_DIR="/root/.openclaw/workspace/obsidian-sync/box"

# 获取当前日期
TODAY=$(date +%Y-%m-%d)

# 添加物品到清单
add_item() {
    local category=$1
    local brand=$2
    local item=$3
    local quantity=$4
    local spec=$5
    local note=$6
    
    # 找到对应分类的表格，添加新行
    # 这里简化处理，实际使用时通过 agent 工具操作
    echo "[$TODAY] 入库: $category - $brand $item $quantity"
}

# 同步到 GitHub
sync_to_git() {
    cd /root/.openclaw/workspace/obsidian-sync
    cp "$INVENTORY_FILE" "$BACKUP_DIR/"
    git add box/
    git commit -m "Update inventory: $TODAY"
    git push origin main
    echo "已同步到 GitHub"
}

# 主命令
case "$1" in
    add)
        add_item "$2" "$3" "$4" "$5" "$6" "$7"
        ;;
    sync)
        sync_to_git
        ;;
    *)
        echo "用法: $0 {add|sync}"
        ;;
esac
