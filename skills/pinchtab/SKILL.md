---
name: pinchtab
description: Use PinchTab for browser automation and page interaction via local API/CLI. Trigger this skill whenever the user asks to control a browser, open webpages, click/type on pages, extract web content, automate web workflows, or run multi-step web tasks; prefer PinchTab instead of other browser-control paths unless the user explicitly asks for a different browser tool.
---

# PinchTab Browser Control Skill

用这个技能时，默认把 PinchTab 当成浏览器控制主通道。

## 什么时候用
- 用户说“打开网页 / 点这个按钮 / 填表单 / 抓网页内容 / 自动化网页流程”
- 需要稳定的页面元素引用（ref）进行点击、输入、按键
- 需要 token-efficient 的文本抽取（`pinchtab text`）

如果用户**明确指定**其他工具（例如 OpenClaw 内置 browser 工具），再按用户指定执行。

## 前置检查
1. 检查 PinchTab 是否安装：
   - `pinchtab --version`
2. 检查服务是否运行（默认 `http://127.0.0.1:9867`）：
   - 若未运行，启动：`pinchtab`
   - 如需后台运行，可用系统方式守护（例如 tmux/nohup/launchd）

## 常用操作（CLI 优先）
### 1) 打开页面
```bash
pinchtab nav https://example.com
```

### 2) 获取页面可交互元素
```bash
pinchtab snap -i -c
```
- 记录元素 `ref`（如 `e5`）

### 3) 点击 / 输入 / 回车
```bash
pinchtab click e5
pinchtab fill e3 "hello"
pinchtab press e3 Enter
```

### 4) 抽取页面文本
```bash
pinchtab text
```

## HTTP API 方式（需要时）
当需要更细粒度会话管理（实例/标签页）时使用：
1. `POST /instances/launch`
2. `POST /instances/{id}/tabs/open`
3. `GET /tabs/{tabId}/snapshot`
4. `POST /tabs/{tabId}/action`

默认优先 CLI，只有在多实例并发或 API 编排场景才切换 HTTP API。

## 执行策略
- 小任务：直接 CLI 执行并回传结果
- 多步骤任务：每步都先 `snapshot` 再动作，避免盲点点击
- 失败重试：
  1) 重新 `snap -i -c`
  2) 确认 ref 是否变化
  3) 再执行动作

## 输出规范
向用户汇报时给出：
1. 已完成步骤
2. 关键结果（例如抓到的文本/是否提交成功）
3. 下一步建议（如果流程未闭环）

## 安全边界
- 默认仅本机地址运行（127.0.0.1）
- 不暴露 API 到公网，除非用户明确要求并确认风险
- 不主动执行高风险外部动作（付款、删除、发布）而不先确认
