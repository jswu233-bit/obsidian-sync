# 囤货库存可视化 Web 应用

一个简洁的 Flask Web 应用，用于可视化展示囤货库存数据。

## 功能特性

- **首页**：库存总览，显示分组汇总和品牌明细
- **图表页**：饼图显示各分类占比，柱状图显示剩余天数
- **周报页**：显示完整的库存周报
- **响应式设计**：支持手机和桌面浏览

## 文件结构

```
inventory-stock/
├── web_app.py              # Flask 主程序
├── templates/              # HTML 模板
│   ├── index.html         # 首页
│   ├── charts.html        # 图表页
│   └── report.html        # 周报页
├── static/                 # 静态资源
│   └── style.css          # 样式文件
├── requirements.txt        # Python 依赖
├── start.sh               # 启动脚本
└── README.md              # 说明文档
```

## 安装依赖

```bash
pip3 install -r requirements.txt
```

## 启动应用

### 方式 1：使用启动脚本

```bash
chmod +x start.sh
./start.sh
```

### 方式 2：直接运行

```bash
python3 web_app.py
```

## 访问应用

启动后，在浏览器中访问：

- 首页：http://localhost:5000
- 图表：http://localhost:5000/charts
- 周报：http://localhost:5000/report

## 数据源

应用从 `/Users/jamiewu/.openclaw/workspace/inventory/stock.yaml` 读取库存数据。

## 技术栈

- **后端**：Flask 3.0
- **前端**：HTML5 + CSS3 + Chart.js 4.4
- **数据**：YAML
