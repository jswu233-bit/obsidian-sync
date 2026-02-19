# X (Twitter) 搜索技能

## 用户X账号信息
- **账号**: @jswu255 (jingshanwu@126.com)
- **Cookies已配置**: ✅
  - auth_token
  - ct0
  - guest_id

## 使用方法

### 快速搜索脚本
```bash
cd /root/.openclaw/workspace
X_SEARCH_QUERY="搜索关键词" python3 x_quick_search.py
```

### 搜索特定博主
```bash
X_SEARCH_QUERY="from:op7418" python3 x_quick_search.py
X_SEARCH_QUERY="from:dotey" python3 x_quick_search.py
X_SEARCH_QUERY="from:SamuelQZQ" python3 x_quick_search.py
X_SEARCH_QUERY="from:gkxspace" python3 x_quick_search.py
X_SEARCH_QUERY="from:yulin807" python3 x_quick_search.py
```

### 搜索多个博主
```bash
X_SEARCH_QUERY="from:op7418 OR from:dotey OR from:SamuelQZQ" python3 x_quick_search.py
```

## 关注博主列表

### 核心关注
1. **@op7418 (歸藏)** - AIGC周刊作者，guizang.ai
   - 关注：国产AI、大模型动态、AI产品评测

2. **@dotey (宝玉)** - Prompt Engineer
   - 关注：提示词工程、AI应用方法论、产品分析

3. **@SamuelQZQ (DN-Samuel)** - AI视频博主，前微软工程师
   - 关注：AI视频生成、编程工具、技术评测

### 新增关注
4. **@gkxspace (余温)** - OpenClaw深度用户
   - 关注：多Agent协作、OpenClaw架构、AI工具链

5. **@yulin807 (Qingyue)** - 独立开发者
   - 关注：时间线工具、用户画像分析、独立开发

## 输出文件
- 截图: `x_search_final.png`
- 结果: `x_search_summary.json`

## 注意事项
- X平台偶尔会有服务中断
- 需要保持cookies有效性
- 搜索结果保存5条最新推文
