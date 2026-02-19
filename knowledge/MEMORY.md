# MEMORY.md - 核心记忆

## 用户
- 主要沟通渠道：飞书
- WhatsApp: +8618616818233
- Discord: jswu233
- X (Twitter): @jswu255 (jingshanwu@126.com)

## 搜索技能优先级（重要！）

当用户需要搜索信息时，按以下优先级使用：

### 1️⃣ lobster-browser-tool（首选）
- **路径**: `/root/.openclaw/workspace/lobster-browser-tool/`
- **依赖**: Playwright + xvfb + Chromium（已安装）
- **使用方法**:
  ```bash
  cd /root/.openclaw/workspace/lobster-browser-tool
  xvfb-run --auto-servernum node browser-control.js navigate <url>
  xvfb-run --auto-servernum node browser-control.js screenshot
  ```
- **适用场景**: 
  - X (Twitter) 搜索（配合 cookies）
  - 任意网站浏览和截图
  - 需要视觉确认的操作
- **状态**: ✅ 已安装可用

### 2️⃣ X (Twitter) Cookie 搜索（次选）
- **脚本**: `/root/.openclaw/workspace/x_quick_search.py`
- **凭证**: 已配置用户的 cookies (auth_token, ct0, guest_id)
- **使用方法**: 
  ```bash
  cd /root/.openclaw/workspace && X_SEARCH_QUERY="关键词" python3 x_quick_search.py
  ```
- **适用场景**: 专门用于 X 快速搜索
- **状态**: ✅ 已验证可用

### 3️⃣ Brave API 搜索（第三选择）
- **工具**: `web_search`
- **使用方法**: 直接调用 web_search 工具
- **适用场景**: 通用网页搜索、新闻、文档
- **状态**: ✅ 随时可用

### 4️⃣ OpenClaw Chrome 扩展（最后选择）
- **条件**: 需要用户在本地 Chrome 上开启 OpenClaw 扩展（badge ON）
- **使用方法**: `browser` 工具配合 `profile="chrome"`
- **适用场景**: 需要用户交互、复杂网页操作、登录态网站
- **状态**: ⚠️ 需要用户手动开启

## 活跃配置
- **主模型**: `hajimi/claude-sonnet-4-5`
- **Subagent模型**: `kimicode/kimi-k2.5`
- **日报推送**: 每天21:00 Discord #日报 频道 + 自动上传Git
  - 内容：AI新闻 + X博主 + YouTube + 微信公众号 + 基金/金融市场 + 国际政治影响 + 北京天气
- **上下文修剪**: 1小时TTL

## 已取消配置
- ❌ 12:00 AI资讯（已合并到21:00）
- ❌ 飞书12:00 AI博主推送
- ❌ WhatsApp日报
- ❌ 常州天气（已改为北京）

## 关注AI博主
1. @op7418 (歸藏) - AIGC周刊，guizang.ai
2. @dotey (宝玉) - Prompt Engineer，baoyu.io
3. @SamuelQZQ - AI视频博主，qzq.at
4. @gkxspace (余温) - OpenClaw深度用户，多Agent协作
5. @yulin807 (Qingyue) - 独立开发者，时间线工具

## X (Twitter) 账号信息
- **用户账号**: @jswu255 (jingshanwu@126.com)
- **Cookies已配置**: ✅ 可用于登录获取实时推文
- **脚本**: `/root/.openclaw/workspace/x_quick_search.py`

## 已安装技能
- **amap-skill**: 高德地图API，位置/天气/POI查询
- **tavily-search**: AI优化搜索
- **duckduckgo-search**: 隐私搜索
- **lobster-browser-tool**: 浏览器自动化（首选搜索工具）
- **x-search**: X(Twitter)搜索，使用用户cookies登录
- **daily-report**: 日报生成技能

## Git 同步指令（全局有效）
当用户说以下任一指令时，自动执行 Git 同步：
- "同步到git" / "同步到 git"
- "上传到git" / "上传到 git"
- "push到git" / "push 到 git"
- "提交到git" / "提交到 git"
- "git同步" / "git 同步"
- "git上传" / "git 上传"

**执行动作**：
```bash
cd /root/.openclaw/workspace/obsidian-sync
git add .
git commit -m "Sync: $(date '+%Y-%m-%d %H:%M')"
git push origin main
```

**同步仓库**: https://github.com/jswu233-bit/obsidian-sync
**本地路径**: `/root/.openclaw/workspace/obsidian-sync`
**文件夹结构**:
- `inbox/` - Zoe 发送的信息
- `outbox/` - 需要 Jamie 确认的信息
- `knowledge/` - 知识库
- `daily/` - 每日日志

## 旅行计划
- **印尼科莫多**: 2026年2月19-22日
- **酒店**: Katamaran Hotel & Resort
- **游船待订**: Padar岛、粉红沙滩、科莫多龙

## 监控任务
- **黄金价格**: 下跌2%提醒（当前$5,085/盎司）

---

## 记忆管理策略

### 短期记忆（7天滚动）
- **位置**: `memory/YYYY-MM-DD.md`
- **保留**: 最近7天的详细日记
- **内容**: 每日任务、临时信息、待办事项
- **清理**: 超过7天的文件自动归档或删除

### 长期记忆（精华归档）
- **位置**: `MEMORY.md`（本文件）
- **更新**: 每天从当日日记中提取重要信息
- **内容**: 
  - 用户偏好变更
  - 重要技能安装/配置
  - API密钥更新
  - 长期关注的项目
  - 关键关系信息

### 每日归档流程
```
1. 检查当日日记 (memory/2026-XX-XX.md)
2. 识别重要信息（用 ⭐ 标记）
3. 更新到 MEMORY.md 对应章节
4. 清理超过7天的日记文件
```

### 归档标记规则
在日记中使用以下标记：
- `⭐ 长期记忆` - 需要归档到 MEMORY.md
- `📌 待跟进` - 需要后续关注
- `✅ 已完成` - 可以清理

---

# Active Context & Memory

## Current Focus (High Priority)
目前用户最关注的是以下领域的动态，请在搜索时增加权重：
1.  **OpenClaw**: 任何关于 OpenClaw 的更新、插件、最佳实践或社区讨论。
2.  **Opencode**: 相关的技术进展或应用案例。
3.  **AI Agents**: 能够独立完成任务的智能体应用案例。
4.  **Viral Apps**: 最近一周在社媒（Twitter/X/小红书）上突然火爆的 AI 产品。

## Active Projects
* **Project**: "Daily AI Intelligence Briefing" (每日 AI 情报简报)
    * **Goal**: 每天生成一份 Top 10 行业动态。
    * **Status**: Setup phase complete. Ready for first run.

## Key Relationships
* **User**: The Product Manager (Boss).
* **Zoe**: The Assistant (You).
