#!/usr/bin/env python3
"""
智能囤货库存管理系统 v2
功能：入库、盘点、消耗、查询、周报、智能补货建议
"""

import yaml
import sys
import os
import tempfile
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict
from difflib import SequenceMatcher

# 配置
DATA_FILE = Path("/root/.openclaw/workspace/inventory/stock.yaml")
CATEGORIES = ["纸类", "厨房用品", "清洁用品", "旅行用品", "个人护理用品"]


class DataValidationError(Exception):
    """数据验证错误"""
    pass


class InventoryManager:
    """库存管理器"""

    def __init__(self, data_file: Path = DATA_FILE):
        self.data_file = data_file
        self.data = self._load_data()

        # 索引和缓存
        self._item_index: Dict[str, Dict] = {}  # id -> item
        self._name_index: Dict[str, str] = {}   # name -> id
        self._daily_usage_cache: Dict[str, Tuple[float, datetime]] = {}  # id -> (usage, timestamp)

        self._rebuild_indexes()

    def _rebuild_indexes(self):
        """重建索引"""
        self._item_index.clear()
        self._name_index.clear()

        for item in self.data.get('items', []):
            item_id = item.get('id')
            item_name = item.get('name')

            if item_id:
                self._item_index[item_id] = item
            if item_name:
                self._name_index[item_name.lower()] = item_id

    def _load_data(self) -> Dict:
        """加载数据"""
        if not self.data_file.exists():
            return self._init_data()

        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            if data is None:
                return self._init_data()

            # 验证数据结构
            self._validate_data(data)
            return data

        except yaml.YAMLError as e:
            raise DataValidationError(f"YAML 解析错误: {e}")
        except IOError as e:
            raise DataValidationError(f"文件读取错误: {e}")
        except Exception as e:
            raise DataValidationError(f"数据加载失败: {e}")

    def _validate_data(self, data: Dict):
        """验证数据结构"""
        if not isinstance(data, dict):
            raise DataValidationError("数据必须是字典类型")

        # 验证必需字段
        required_fields = ['categories', 'items', 'consumption', 'restock']
        for field in required_fields:
            if field not in data:
                data[field] = [] if field in ['items', 'restock'] else {}

        # 验证 items 结构
        if not isinstance(data['items'], list):
            raise DataValidationError("items 必须是列表类型")

        for item in data['items']:
            if not isinstance(item, dict):
                raise DataValidationError("每个 item 必须是字典类型")

            required_item_fields = ['id', 'name', 'category', 'unit', 'current_stock']
            for field in required_item_fields:
                if field not in item:
                    raise DataValidationError(f"item 缺少必需字段: {field}")

            # 验证库存数量
            if not isinstance(item['current_stock'], (int, float)) or item['current_stock'] < 0:
                raise DataValidationError(f"item {item['name']} 的库存数量无效")

        # 验证 consumption 结构
        if not isinstance(data['consumption'], dict):
            raise DataValidationError("consumption 必须是字典类型")

        # 确保 monthly_usage 存在
        if 'monthly_usage' not in data:
            data['monthly_usage'] = {}

        # 确保 item_groups 存在
        if 'item_groups' not in data:
            data['item_groups'] = {
                '抽纸': ['抽纸', '乳霜纸', '纸巾'],
                '卷纸': ['卷纸'],
                '湿厕纸': ['湿厕纸']
            }

    def _save_data(self):
        """原子保存数据"""
        try:
            # 确保目录存在
            self.data_file.parent.mkdir(parents=True, exist_ok=True)

            # 使用临时文件实现原子写入
            fd, temp_path = tempfile.mkstemp(
                dir=self.data_file.parent,
                prefix='.tmp_',
                suffix='.yaml'
            )

            try:
                with os.fdopen(fd, 'w', encoding='utf-8') as f:
                    yaml.dump(self.data, f, allow_unicode=True, sort_keys=False)

                # 原子替换
                os.replace(temp_path, self.data_file)

            except Exception as e:
                # 清理临时文件
                try:
                    os.unlink(temp_path)
                except:
                    pass
                raise e

        except IOError as e:
            raise DataValidationError(f"文件写入错误: {e}")
        except Exception as e:
            raise DataValidationError(f"数据保存失败: {e}")

    def _init_data(self) -> Dict:
        """初始化数据结构"""
        return {
            'categories': CATEGORIES,
            'items': [],
            'consumption': {},
            'restock': [],
            'monthly_usage': {},
            'item_groups': {
                '抽纸': ['抽纸', '乳霜纸', '纸巾'],
                '卷纸': ['卷纸'],
                '湿厕纸': ['湿厕纸']
            }
        }

    def _fuzzy_match_score(self, s1: str, s2: str) -> float:
        """计算模糊匹配分数"""
        s1_lower = s1.lower()
        s2_lower = s2.lower()

        # 完全匹配
        if s1_lower == s2_lower:
            return 1.0

        # 包含匹配
        if s1_lower in s2_lower or s2_lower in s1_lower:
            return 0.9

        # 使用序列匹配器
        return SequenceMatcher(None, s1_lower, s2_lower).ratio()

    def _find_item(self, name: str) -> Optional[Dict]:
        """根据名称查找物品（改进的模糊匹配）"""
        if not name:
            return None

        # 先尝试精确匹配（使用索引）
        name_lower = name.lower()
        if name_lower in self._name_index:
            item_id = self._name_index[name_lower]
            return self._item_index.get(item_id)

        # 模糊匹配
        best_match = None
        best_score = 0.6  # 最低匹配阈值

        for item in self.data['items']:
            score = self._fuzzy_match_score(name, item['name'])
            if score > best_score:
                best_score = score
                best_match = item

        return best_match

    def _calculate_daily_usage(self, item_id: str) -> float:
        """计算日均消耗量（带缓存）"""
        # 检查缓存（1小时有效期）
        if item_id in self._daily_usage_cache:
            cached_usage, cached_time = self._daily_usage_cache[item_id]
            if datetime.now() - cached_time < timedelta(hours=1):
                return cached_usage

        consumption_records = []

        for date, records in self.data['consumption'].items():
            try:
                for record in records:
                    if record['id'] == item_id:
                        consumption_records.append({
                            'date': datetime.strptime(date, '%Y-%m-%d'),
                            'quantity': record['quantity']
                        })
            except (ValueError, KeyError):
                continue

        if len(consumption_records) < 2:
            return 0.0

        # 按日期排序
        consumption_records.sort(key=lambda x: x['date'])

        # 计算总消耗和时间跨度
        total_consumed = sum(r['quantity'] for r in consumption_records)
        days_span = (consumption_records[-1]['date'] - consumption_records[0]['date']).days

        if days_span == 0:
            return 0.0

        daily_usage = total_consumed / days_span

        # 更新缓存
        self._daily_usage_cache[item_id] = (daily_usage, datetime.now())

        return daily_usage

    def _estimate_days_left(self, item: Dict) -> Optional[int]:
        """预计还能用多少天"""
        daily_usage = self._calculate_daily_usage(item['id'])

        # 如果有手动设置的月消耗量，优先使用
        if item['id'] in self.data.get('monthly_usage', {}):
            monthly = self.data['monthly_usage'][item['id']]
            daily_usage = monthly / 30

        if daily_usage <= 0:
            return None

        return round(item['current_stock'] / daily_usage)

    def _get_item_group(self, item_name: str) -> Optional[str]:
        """获取物品所属分组"""
        for group_name, patterns in self.data.get('item_groups', {}).items():
            for pattern in patterns:
                if pattern in item_name:
                    return group_name
        return None

    def _group_items_by_pattern(self, items: List[Dict]) -> Dict[str, List[Dict]]:
        """按分组模式对物品进行分组"""
        grouped = defaultdict(list)
        ungrouped = []

        for item in items:
            group_name = self._get_item_group(item['name'])
            if group_name:
                grouped[group_name].append(item)
            else:
                ungrouped.append(item)

        return dict(grouped), ungrouped

    def _calculate_group_stats(self, items: List[Dict]) -> Tuple[float, str, Optional[int]]:
        """计算分组统计信息
        返回: (总库存, 单位, 预计剩余天数)
        """
        if not items:
            return 0, '', None

        total_stock = sum(item['current_stock'] for item in items)
        unit = items[0]['unit']  # 假设同组物品单位相同

        # 计算总月消耗量
        total_monthly_usage = 0
        for item in items:
            if item['id'] in self.data.get('monthly_usage', {}):
                total_monthly_usage += self.data['monthly_usage'][item['id']]
            else:
                # 使用历史消耗计算
                daily_usage = self._calculate_daily_usage(item['id'])
                total_monthly_usage += daily_usage * 30

        # 计算剩余天数
        if total_monthly_usage > 0:
            days_left = round(total_stock / (total_monthly_usage / 30))
            return total_stock, unit, days_left
        else:
            return total_stock, unit, None

    def _validate_quantity(self, quantity: float, operation: str) -> None:
        """验证数量输入"""
        if not isinstance(quantity, (int, float)):
            raise ValueError(f"{operation}数量必须是数字")

        if quantity < 0:
            raise ValueError(f"{operation}数量不能为负数")

        if quantity == 0:
            raise ValueError(f"{operation}数量不能为零")

    def add_stock(self, item_name: str, quantity: int) -> str:
        """入库"""
        try:
            self._validate_quantity(quantity, "入库")
        except ValueError as e:
            return f"❌ {e}"

        item = self._find_item(item_name)

        if not item:
            return f"❌ 未找到物品：{item_name}，请先添加新物品"

        item['current_stock'] += quantity
        item['last_updated'] = datetime.now().strftime('%Y-%m-%d')

        # 记录入库
        today = datetime.now().strftime('%Y-%m-%d')
        self.data['restock'].append({
            'date': today,
            'items': [{'id': item['id'], 'quantity': quantity}]
        })

        # 清除缓存
        self._daily_usage_cache.pop(item['id'], None)

        try:
            self._save_data()
        except DataValidationError as e:
            return f"❌ 保存失败：{e}"

        return f"✅ 入库成功：{item['name']} +{quantity}{item['unit']}，当前库存：{item['current_stock']}{item['unit']}"

    def update_stock(self, item_name: str, quantity: int) -> str:
        """盘点更新"""
        try:
            if quantity < 0:
                raise ValueError("库存数量不能为负数")
        except ValueError as e:
            return f"❌ {e}"

        item = self._find_item(item_name)

        if not item:
            return f"❌ 未找到物品：{item_name}"

        old_stock = item['current_stock']
        consumed = old_stock - quantity

        # 如果是减少，记录消耗
        if consumed > 0:
            today = datetime.now().strftime('%Y-%m-%d')
            if today not in self.data['consumption']:
                self.data['consumption'][today] = []
            self.data['consumption'][today].append({
                'id': item['id'],
                'quantity': consumed
            })

        item['current_stock'] = quantity
        item['last_updated'] = datetime.now().strftime('%Y-%m-%d')

        # 清除缓存
        self._daily_usage_cache.pop(item['id'], None)

        try:
            self._save_data()
        except DataValidationError as e:
            return f"❌ 保存失败：{e}"

        if consumed > 0:
            return f"📦 盘点更新：{item['name']} 从 {old_stock} 更新为 {quantity}{item['unit']}（消耗了 {consumed}{item['unit']}）"
        elif consumed < 0:
            return f"📦 盘点更新：{item['name']} 从 {old_stock} 更新为 {quantity}{item['unit']}（增加了 {abs(consumed)}{item['unit']}）"
        else:
            return f"📦 盘点更新：{item['name']} 库存无变化（{quantity}{item['unit']}）"

    def consume(self, item_name: str, quantity: int) -> str:
        """记录消耗"""
        try:
            self._validate_quantity(quantity, "消耗")
        except ValueError as e:
            return f"❌ {e}"

        item = self._find_item(item_name)

        if not item:
            return f"❌ 未找到物品：{item_name}"

        if item['current_stock'] < quantity:
            return f"⚠️ 库存不足：{item['name']} 当前只有 {item['current_stock']}{item['unit']}"

        item['current_stock'] -= quantity
        item['last_updated'] = datetime.now().strftime('%Y-%m-%d')

        # 记录消耗
        today = datetime.now().strftime('%Y-%m-%d')
        if today not in self.data['consumption']:
            self.data['consumption'][today] = []
        self.data['consumption'][today].append({
            'id': item['id'],
            'quantity': quantity
        })

        # 清除缓存
        self._daily_usage_cache.pop(item['id'], None)

        try:
            self._save_data()
        except DataValidationError as e:
            return f"❌ 保存失败：{e}"

        return f"✅ 消耗记录：{item['name']} -{quantity}{item['unit']}，剩余：{item['current_stock']}{item['unit']}"

    def set_monthly_usage(self, item_name: str, quantity: float) -> str:
        """设置每月消耗量"""
        try:
            self._validate_quantity(quantity, "月消耗")
        except ValueError as e:
            return f"❌ {e}"

        item = self._find_item(item_name)

        if not item:
            return f"❌ 未找到物品：{item_name}"

        if 'monthly_usage' not in self.data:
            self.data['monthly_usage'] = {}

        self.data['monthly_usage'][item['id']] = quantity

        # 清除缓存
        self._daily_usage_cache.pop(item['id'], None)

        try:
            self._save_data()
        except DataValidationError as e:
            return f"❌ 保存失败：{e}"

        days_left = self._estimate_days_left(item)
        if days_left:
            return f"✅ 已设置 {item['name']} 每月消耗 {quantity}{item['unit']}，预计还能用 {days_left} 天"
        else:
            return f"✅ 已设置 {item['name']} 每月消耗 {quantity}{item['unit']}"

    def query(self, item_name: Optional[str] = None) -> str:
        """查询库存"""
        if item_name:
            item = self._find_item(item_name)
            if not item:
                return f"❌ 未找到：{item_name}"

            days_left = self._estimate_days_left(item)
            result = f"📦 {item['name']}：{item['current_stock']}{item['unit']}（{item['category']}）"

            if days_left:
                result += f"\n   预计还能用 {days_left} 天"

            return result
        else:
            # 显示全部
            result = "📦 当前库存清单\n\n"
            for cat in self.data['categories']:
                items_in_cat = [i for i in self.data['items'] if i['category'] == cat]
                if items_in_cat:
                    result += f"【{cat}】\n"

                    # 对物品进行分组
                    grouped, ungrouped = self._group_items_by_pattern(items_in_cat)

                    # 先显示分组汇总
                    for group_name, group_items in grouped.items():
                        total_stock, unit, days_left = self._calculate_group_stats(group_items)
                        result += f"  📦 {group_name} 总计：{total_stock}{unit}"
                        if days_left:
                            result += f" (还能用 {days_left} 天)"
                        result += "\n"

                        # 只对非特殊分组显示明细
                        if group_name not in ['抽纸', '卷纸', '湿厕纸']:
                            # 显示分组内明细
                            for i, item in enumerate(group_items):
                                is_last = (i == len(group_items) - 1)
                                prefix = "    └─ " if is_last else "    ├─ "
                                result += f"{prefix}{item['name']}：{item['current_stock']}{item['unit']}\n"
                            result += "\n"

                    # 显示未分组的物品
                    for item in ungrouped:
                        days_left = self._estimate_days_left(item)
                        stock_info = f"  • {item['name']}：{item['current_stock']}{item['unit']}"
                        if days_left:
                            stock_info += f" (还能用 {days_left} 天)"
                        result += stock_info + "\n"

                    if ungrouped:
                        result += "\n"
            return result

    def generate_weekly_report(self) -> str:
        """生成周报"""
        report = "📊 囤货周报\n"
        report += f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        report += "=" * 40 + "\n\n"

        low_stock_items = []

        for cat in self.data['categories']:
            items_in_cat = [i for i in self.data['items'] if i['category'] == cat]
            if items_in_cat:
                report += f"【{cat}】\n"

                # 对物品进行分组
                grouped, ungrouped = self._group_items_by_pattern(items_in_cat)

                # 先显示分组汇总
                for group_name, group_items in grouped.items():
                    total_stock, unit, days_left = self._calculate_group_stats(group_items)
                    report += f"  📦 {group_name} 总计：{total_stock}{unit}"
                    if days_left:
                        report += f" (还能用 {days_left} 天)"
                        if days_left < 14:  # 少于2周
                            report += " ⚠️"
                            # 将整个分组加入低库存列表
                            low_stock_items.append((f"{group_name}（分组）", days_left))
                    report += "\n"

                    # 只对非特殊分组显示明细
                    if group_name not in ['抽纸', '卷纸', '湿厕纸']:
                        # 显示分组内明细
                        for i, item in enumerate(group_items):
                            is_last = (i == len(group_items) - 1)
                            prefix = "    └─ " if is_last else "    ├─ "
                            report += f"{prefix}{item['name']}：{item['current_stock']}{item['unit']}\n"
                        report += "\n"

                # 显示未分组的物品
                for item in ungrouped:
                    stock = item['current_stock']
                    unit = item['unit']
                    days_left = self._estimate_days_left(item)

                    stock_info = f"  • {item['name']}：{stock}{unit}"
                    if days_left:
                        stock_info += f" (还能用 {days_left} 天)"
                        if days_left < 14:  # 少于2周
                            stock_info += " ⚠️"
                            low_stock_items.append((item['name'], days_left))

                    report += stock_info + "\n"

                if ungrouped:
                    report += "\n"

        # 补货建议
        if low_stock_items:
            report += "🛒 补货建议\n"
            report += "-" * 40 + "\n"
            for item_name, days_left in sorted(low_stock_items, key=lambda x: x[1]):
                report += f"  • {item_name}：还能用 {days_left} 天，建议尽快补货\n"
        else:
            report += "✅ 库存充足，暂无需补货\n"

        return report


def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("用法: inventory_v2.py {add|update|consume|query|report|set-usage} [参数...]")
        print("\n示例:")
        print("  add 抽纸 2        # 入库2包抽纸")
        print("  update 抽纸 8     # 盘点，抽纸剩8包")
        print("  consume 抽纸 1    # 消耗1包抽纸")
        print("  query 抽纸        # 查询抽纸库存")
        print("  query             # 查询全部库存")
        print("  report            # 生成周报")
        print("  set-usage 抽纸 6  # 设置抽纸每月消耗6包")
        return

    try:
        manager = InventoryManager()
    except DataValidationError as e:
        print(f"❌ 初始化失败：{e}")
        return
    except Exception as e:
        print(f"❌ 未知错误：{e}")
        import traceback
        traceback.print_exc()
        return

    cmd = sys.argv[1]

    try:
        if cmd == "add" and len(sys.argv) >= 4:
            print(manager.add_stock(sys.argv[2], int(sys.argv[3])))

        elif cmd == "update" and len(sys.argv) >= 4:
            print(manager.update_stock(sys.argv[2], int(sys.argv[3])))

        elif cmd == "consume" and len(sys.argv) >= 4:
            print(manager.consume(sys.argv[2], int(sys.argv[3])))

        elif cmd == "query":
            name = sys.argv[2] if len(sys.argv) > 2 else None
            print(manager.query(name))

        elif cmd == "report":
            print(manager.generate_weekly_report())

        elif cmd == "set-usage" and len(sys.argv) >= 4:
            print(manager.set_monthly_usage(sys.argv[2], float(sys.argv[3])))

        else:
            print("❌ 未知命令或参数不足")

    except ValueError as e:
        print(f"❌ 参数错误：{e}")
    except Exception as e:
        print(f"❌ 执行错误：{e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
