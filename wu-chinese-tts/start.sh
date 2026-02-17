#!/bin/bash

# 文字转吴语服务器启动脚本

cd /root/.openclaw/workspace/wu-chinese-tts

# 检查端口是否被占用
PORT=8080
PID=$(lsof -t -i:$PORT 2>/dev/null || netstat -tlnp 2>/dev/null | grep ":$PORT " | awk '{print $7}' | cut -d'/' -f1)

if [ ! -z "$PID" ]; then
    echo "Port $PORT is already in use by PID $PID, killing..."
    kill -9 $PID 2>/dev/null
    sleep 1
fi

# 启动服务器
echo "Starting server..."
nohup python3 server.py > server.log 2>&1 &

# 等待服务器启动
sleep 3

# 检查是否成功
if lsof -i:8080 >/dev/null 2>&1 || netstat -tlnp 2>/dev/null | grep -q ":8080"; then
    echo "✅ Server started successfully!"
    echo "🌐 Access: http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4 2>/dev/null || echo 'YOUR_VPS_IP'):8080"
    echo "📋 Logs: tail -f /root/.openclaw/workspace/wu-chinese-tts/server.log"
else
    echo "❌ Failed to start server"
    echo "📋 Check logs: cat /root/.openclaw/workspace/wu-chinese-tts/server.log"
fi
