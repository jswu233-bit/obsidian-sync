#!/usr/bin/env python3
"""
囤货库存可视化 Web 应用
"""

from flask import Flask, render_template, jsonify
from pathlib import Path
from datetime import datetime
from typing import Dict
from inventory import InventoryManager

app = Flask(__name__)
DATA_FILE = Path("/root/.openclaw/workspace/inventory/stock.yaml")


def get_inventory_overview(manager: InventoryManager) -> Dict:
    """获取库存总览数据"""
    overview = {
        'categories': [],
        'total_items': len(manager.data.get('items', [])),
        'low_stock_count': 0
    }

    for cat in manager.data.get('categories', []):
        items_in_cat = [i for i in manager.data.get('items', []) if i['category'] == cat]
        if not items_in_cat:
            continue

        cat_data = {
            'name': cat,
            'groups': [],
            'ungrouped': []
        }

        # 对物品进行分组
        grouped, ungrouped = manager._group_items_by_pattern(items_in_cat)

        # 处理分组
        for group_name, group_items in grouped.items():
            total_stock, unit, days_left = manager._calculate_group_stats(group_items)
            group_data = {
                'name': group_name,
                'total_stock': total_stock,
                'unit': unit,
                'days_left': days_left,
                'item_list': []
            }

            # 只对非特殊分组显示明细
            if group_name not in ['抽纸', '卷纸', '湿厕纸']:
                for item in group_items:
                    group_data['item_list'].append({
                        'name': item['name'],
                        'stock': item['current_stock'],
                        'unit': item['unit']
                    })

            if days_left and days_left < 14:
                overview['low_stock_count'] += 1

            cat_data['groups'].append(group_data)

        # 处理未分组物品
        for item in ungrouped:
            days_left = manager._estimate_days_left(item)
            item_data = {
                'name': item['name'],
                'stock': item['current_stock'],
                'unit': item['unit'],
                'days_left': days_left
            }

            if days_left and days_left < 14:
                overview['low_stock_count'] += 1

            cat_data['ungrouped'].append(item_data)

        overview['categories'].append(cat_data)

    return overview


def get_chart_data(manager: InventoryManager) -> Dict:
    """获取图表数据"""
    category_stats = {}
    items_with_days = []

    for cat in manager.data.get('categories', []):
        items_in_cat = [i for i in manager.data.get('items', []) if i['category'] == cat]
        category_stats[cat] = len(items_in_cat)

        for item in items_in_cat:
            days_left = manager._estimate_days_left(item)
            if days_left is not None:
                items_with_days.append({
                    'name': item['name'],
                    'days_left': days_left
                })

    return {
        'category_stats': category_stats,
        'items_with_days': sorted(items_with_days, key=lambda x: x['days_left'])[:10]
    }


# Flask 路由
@app.route('/')
def index():
    """首页：库存总览"""
    manager = InventoryManager(DATA_FILE)
    overview = get_inventory_overview(manager)
    return render_template('index.html', overview=overview)


@app.route('/charts')
def charts():
    """图表页"""
    return render_template('charts.html')


@app.route('/report')
def report():
    """周报页"""
    manager = InventoryManager(DATA_FILE)
    report_text = manager.generate_weekly_report()
    return render_template('report.html', report=report_text)


@app.route('/api/chart-data')
def api_chart_data():
    """API：获取图表数据"""
    manager = InventoryManager(DATA_FILE)
    chart_data = get_chart_data(manager)
    return jsonify(chart_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
