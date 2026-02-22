# 日报生成技能

## 日报配置

### 发送时间
- **每天21:00**（北京时间）
- 频道: Discord #日报

### 内容板块

#### 1. AI新闻板块
- 搜索今日最新AI新闻（国内外）
- 重点关注：大模型进展、产品发布、行业动态
- 工具: `web_search`

#### 2. X博主动态（必须详细）
⚠️ **重要：必须使用x_quick_search.py获取具体内容，不能只列博主介绍！**

**执行步骤：**
1. 切换到工作目录：`cd /root/.openclaw/workspace`
2. 执行搜索命令（逐个博主）：
   ```bash
   X_SEARCH_QUERY="from:op7418" python3 x_quick_search.py
   X_SEARCH_QUERY="from:dotey" python3 x_quick_search.py
   X_SEARCH_QUERY="from:SamuelQZQ" python3 x_quick_search.py
   X_SEARCH_QUERY="from:gkxspace" python3 x_quick_search.py
   X_SEARCH_QUERY="from:yulin807" python3 x_quick_search.py
   ```
3. 读取结果文件：`cat x_search_summary.json`
4. 总结每位博主今天发的**具体内容**（不是泛泛介绍博主是谁）

**关注博主：**
- @op7418 (歸藏) - AIGC周刊
- @dotey (宝玉) - Prompt Engineer  
- @SamuelQZQ (DN-Samuel) - AI视频博主
- @gkxspace (余温) - OpenClaw深度用户
- @yulin807 (Qingyue) - 独立开发者

**要求：**
- ❌ 不能写"@op7418是AIGC周刊作者"这种泛泛介绍
- ✅ 必须写"@op7418今天发了推文，内容是..."
- ✅ 包含推文链接
- ✅ 总结推文核心观点

#### 3. YouTube精选
- 搜索最新AI教程、产品评测
- 工具: `web_search`

#### 4. 微信公众号
- ✅ **可搜索**，使用Brave API
- 搜索AI相关文章
- 工具: `web_search`
- 搜索示例:
  ```
  AI人工智能 微信公众号 2026年2月 site:mp.weixin.qq.com
  OpenClaw 微信公众号 site:mp.weixin.qq.com
  ```

#### 5. 基金与金融市场
- 美股、A股、港股表现
- 大宗商品（黄金、原油）
- 工具: `web_search`

#### 6. 天气信息
- **北京天气**（使用天气技能）
- 工具: `curl wttr.in/Beijing`

## 生成流程

```
1. 获取当前日期 → date +%Y-%m-%d (注意：必须是2026年，不是2025年)
2. 搜索AI新闻 → web_search
3. 获取X博主推文 → x_quick_search.py
4. 搜索YouTube → web_search
5. 搜索公众号 → web_search
6. 搜索金融市场 → web_search
7. 获取北京天气 → wttr.in
8. 整理成Markdown (验证日期为2026年)
9. 发送到Discord
10. 保存到Git: daily/YYYY-MM-DD-日报.md (YYYY=2026)
11. git add → git commit → git push
```

## 日期验证
- **当前年份是2026年，不是2025年！**
- 文件命名: `2026-MM-DD-日报.md`
- 日报标题: `📰 Jamie每日综合日报 — 2026年M月D日`
- 提交信息: `📰 添加2026-MM-DD日报`

## 文件格式

### Discord格式
- 使用emoji美化
- 每个板块清晰分隔
- 所有链接可点击

### Git文件格式
- Markdown格式
- 包含完整链接
- 文件命名: `YYYY-MM-DD-日报.md`

## Git提交信息模板
```
📰 添加YYYY-MM-DD日报

- AI新闻: [要点]
- X博主: [博主名] - [内容摘要]
- YouTube: [视频标题]
- 公众号: [文章标题]
- 金融市场: [关键数据]
- 天气: [天气概况]
```

## 注意事项
- 每个X博主内容需要具体总结，不能泛泛而谈
- 所有外部链接需要可点击
- 天气固定使用北京
- 每天21:00准时发送
