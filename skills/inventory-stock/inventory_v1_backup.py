#!/usr/bin/env python3
"""
囤货库存管理脚本
处理入库、盘点、消耗、生成周报
"""

import yaml
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path("/root/.openclaw/workspace/inventory/stock.yaml")

def load_data():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

def find_item(data, name):
    """根据名称查找物品"""
    for item in data['items']:
        if name in item['name'] or item['name'] in name:
            return item
    return None

def add_stock(item_name, quantity):
    """入库"""
    data = load_data()
    item = find_item(data, item_name)
    
    if item:
        item['current_stock'] += quantity
        item['last_updated'] = datetime.now().strftime('%Y-%m-%d')
        
        # 记录入库
        today = datetime.now().strftime('%Y-%m-%d')
        restock_entry = {'date': today, 'items': [{'id': item['id'], 'quantity': quantity}]}
        data['restock'].append(restock_entry)
        
        save_data(data)
        return f"✅ 入库成功：{item['name']} +{quantity}{item['unit']}，当前库存：{item['current_stock']}{item['unit']}"
    else:
        return f"❌ 未找到物品：{item_name}，请检查名称或先添加新物品"

def update_stock(item_name, quantity):
    """盘点更新"""
    data = load_data()
    item = find_item(data, item_name)
    
    if item:
        old_stock = item['current_stock']
        item['current_stock'] = quantity
        item['last_updated'] = datetime.now().strftime('%Y-%m-%d')
        save_data(data)
        
        diff = quantity - old_stock
        if diff < 0:
            return f"📦 盘点更新：{item['name']} 从 {old_stock} 更新为 {quantity}{item['unit']}（消耗了 {abs(diff)}{item['unit']}）"
        elif diff > 0:
            return f"📦 盘点更新：{item['name']} 从 {old_stock} 更新为 {quantity}{item['unit']}（增加了 {diff}{item['unit']}）"
        else:
            return f"📦 盘点更新：{item['name']} 库存无变化（{quantity}{item['unit']}）"
    else:
        return f"❌ 未找到物品：{item_name}"

def consume(item_name, quantity):
    """记录消耗"""
    data = load_data()
    item = find_item(data, item_name)
    
    if item:
        if item['current_stock'] >= quantity:
            item['current_stock'] -= quantity
            item['last_updated'] = datetime.now().strftime('%Y-%m-%d')
            
            # 记录消耗
            today = datetime.now().strftime('%Y-%m-%d')
            if today not in data['consumption']:
                data['consumption'][today] = []
            data['consumption'][today].append({'id': item['id'], 'quantity': quantity})
            
            save_data(data)
            return f"✅ 消耗记录：{item['name']} -{quantity}{item['unit']}，剩余：{item['current_stock']}{item['unit']}"
        else:
            return f"⚠️ 库存不足：{item['name']} 当前只有 {item['current_stock']}{item['unit']}"
    else:
        return f"❌ 未找到物品：{item_name}"

def query(item_name=None):
    """查询库存"""
    data = load_data()
    
    if item_name:
        item = find_item(data, item_name)
        if item:
            return f"📦 {item['name']}：{item['current_stock']}{item['unit']}（{item['category']}）"
        else:
            return f"❌ 未找到：{item_name}"
    else:
        # 显示全部
        result = "📦 当前库存清单\n\n"
        for cat in data['categories']:
            items_in_cat = [i for i in data['items'] if i['category'] == cat]
            if items_in_cat:
                result += f"【{cat}】\n"
                for item in items_in_cat:
                    result += f"  • {item['name']}：{item['current_stock']}{item['unit']}\n"
                result += "\n"
        return result

def generate_weekly_report():
    """生成周报"""
    data = load_data()
    
    report = "📊 囤货周报\n"
    report += f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    report += "=" * 30 + "\n\n"
    
    for cat in data['categories']:
        items_in_cat = [i for i in data['items'] if i['category'] == cat]
        if items_in_cat:
            report += f"【{cat}】\n"
            for item in items_in_cat:
                stock = item['current_stock']
                unit = item['unit']
                report += f"  • {item['name']}：{stock}{unit}\n"
            report += "\n"
    
    report += "💡 提示：告诉我每月消耗量，我可以帮你预测什么时候需要补货"
    return report

def main():
    if len(sys.argv) < 2:
        print("用法: inventory.py {add|update|consume|query|report} [参数...]")
        return
    
    cmd = sys.argv[1]
    
    if cmd == "add" and len(sys.argv) >= 4:
        print(add_stock(sys.argv[2], int(sys.argv[3])))
    elif cmd == "update" and len(sys.argv) >= 4:
        print(update_stock(sys.argv[2], int(sys.argv[3])))
    elif cmd == "consume" and len(sys.argv) >= 4:
        print(consume(sys.argv[2], int(sys.argv[3])))
    elif cmd == "query":
        name = sys.argv[2] if len(sys.argv) > 2 else None
        print(query(name))
    elif cmd == "report":
        print(generate_weekly_report())
    else:
        print("未知命令或参数不足")

if __name__ == "__main__":
    main()
