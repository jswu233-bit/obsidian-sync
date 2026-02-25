# Search Skill 配置更新
# 优先级：x-tweet-fetcher > 其他方法

## X/Twitter 搜索
- **主工具**: x-tweet-fetcher (本地)
- **路径**: /root/.openclaw/workspace/x-tweet-fetcher
- **依赖**: Camofox (端口 9377)
- **备用**: X_SEARCH + x_quick_search.py

## 微信公众号搜索
- **工具**: sogou_wechat.py (x-tweet-fetcher)
- **无需额外依赖**

## 通用网页搜索
- **工具**: web_search (Brave API)
- **备用**: duckduckgo-search

## 执行命令示例

### X 用户时间线
```bash
cd /root/.openclaw/workspace/x-tweet-fetcher
python3 scripts/fetch_tweet.py --user <username> --limit 10
```

### X 关键词搜索
```bash
cd /root/.openclaw/workspace/x-tweet-fetcher
python3 scripts/x_discover.py --keywords "关键词" --limit 10
```

### 微信公众号
```bash
cd /root/.openclaw/workspace/x-tweet-fetcher
python3 scripts/sogou_wechat.py --keyword "关键词" --limit 10
```

## 依赖检查
- Camofox 必须运行: netstat -tlnp | grep 9377
- 如未运行: cd /root/.openclaw/workspace/camofox-browser && npm start
