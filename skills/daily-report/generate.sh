#!/bin/bash
# Daily Report Skill - 使用 x-tweet-fetcher 生成日报

REPO_DIR="/root/.openclaw/workspace/obsidian-sync"
DATE=$(date '+%Y-%m-%d')
X_FETCHER="/root/.openclaw/workspace/x-tweet-fetcher"

echo "🔄 生成 OpenClaw 日报: $DATE"

# 检查 Camofox 是否运行
if ! netstat -tlnp | grep -q 9377; then
    echo "⚠️  Camofox 未运行，启动中..."
    cd /root/.openclaw/workspace/camofox-browser && npm start &
    sleep 5
fi

# 爬取 X 热门内容
echo "📱 爬取 X 热门资讯..."
cd $X_FETCHER

# 搜索 OpenClaw 相关推文
python3 scripts/x_discover.py --keywords "OpenClaw,AI Agent" --limit 10 --json > /tmp/x_openclaw.json 2>/dev/null || true

# 搜索 gkxspace 的推文
python3 scripts/fetch_tweet.py --user gkxspace --limit 5 > /tmp/x_gkxspace.json 2>/dev/null || true

# 搜索微信公众号
echo "📰 爬取微信公众号..."
python3 scripts/sogou_wechat.py --keyword "AI Agent" --limit 5 --json > /tmp/wechat_ai.json 2>/dev/null || true

# 整合到日报目录
cd $REPO_DIR
mkdir -p daily/$DATE

# 复制数据
cp /tmp/x_openclaw.json daily/$DATE/x_openclaw.json 2>/dev/null || true
cp /tmp/x_gkxspace.json daily/$DATE/x_gkxspace.json 2>/dev/null || true
cp /tmp/wechat_ai.json daily/$DATE/wechat_ai.json 2>/dev/null || true

# Git 提交
git add daily/$DATE/
git commit -m "Daily report: $DATE" || true
git push origin main

echo "✅ 日报生成完成: $DATE"
