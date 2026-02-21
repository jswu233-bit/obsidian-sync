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

#### 2. X博主动态（详细版）
- 使用X账号登录获取实时推文
- 关注博主:
  - @op7418 (歸藏)
  - @dotey (宝玉)
  - @SamuelQZQ (DN-Samuel)
  - @gkxspace (余温) ⭐新增
  - @yulin807 (Qingyue) ⭐新增
- 工具: `x_quick_search.py`
- 要求: 总结每位博主今天发的具体内容

#### 3. YouTube精选
- 搜索最新AI教程、产品评测
- 工具: `web_search`

#### 4. 微信公众号
- 搜索AI相关文章
- 工具: `web_search`

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
