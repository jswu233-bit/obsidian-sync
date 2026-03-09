#!/bin/bash
# 囤货库存可视化 Web 应用启动脚本

echo "🚀 启动囤货库存可视化 Web 应用..."

# 检查依赖
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 安装依赖..."
    pip3 install -r requirements.txt
fi

# 启动应用
echo "✅ 启动 Flask 服务器 (端口 5000)..."
echo "📱 访问地址: http://localhost:5000"
echo "按 Ctrl+C 停止服务器"
echo ""

python3 web_app.py
