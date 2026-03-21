# Search Skill 全局配置（已对齐 Jamie 指令）

## 全局默认搜索工作流（强制顺序）
当 Jamie 说“搜一下/查一下/检索”时，统一按以下顺序执行：

1. **Pinchtab** - 浏览器自动化采集（必须优先）
2. **x-reader** - 多平台内容抓取
3. **multi-search-engine** - 多引擎聚合
4. **x-tweet-fetcher** - X/Twitter 专用
5. **Brave Search (`web_search`)** - 通用网页搜索兜底

## 执行规则
- 任何搜索任务都从第1步开始。
- 上游失败才允许降级下一步。
- 禁止跳步，除非该工具当前不可用。
- X 无法直读时，继续沿顺序降级，不得以“无法获取”直接结束。
- 输出必须附来源链接。

## 备注
- 默认全局技能文件：`skills/search-priority/SKILL.md`
- 本配置用于保证搜索优先级与日报SOP一致。
