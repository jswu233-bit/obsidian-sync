# OpenClaw 多角色 Bot 配置指南

## 概述
需要为 5 个角色创建 5 个独立的 Discord Bot，连接到同一个 OpenClaw Gateway。

## Discord Bot 创建步骤

### 1. 创建 Discord Application
访问 https://discord.com/developers/applications
- 创建 5 个 Application：
  - Commander-Bot
  - Junshi-Bot
  - Engineer-Bot
  - Creator-Bot
  - Exam-Bot

### 2. 获取 Bot Token
每个 Application → Bot → Reset Token → 复制 Token

### 3. 设置 Bot 权限
- Send Messages
- Read Message History
- Mention Everyone
- Add Reactions
- Use Slash Commands

### 4. 邀请 Bot 到服务器
使用 OAuth2 URL Generator：
- scope: bot
- permissions: 发送消息、读取历史、提及所有人

## OpenClaw 配置

### 每个 Bot 的独立配置

创建 5 个配置文件：
```bash
/root/.openclaw/agents/commander/openclaw.json
/root/.openclaw/agents/junshi/openclaw.json
/root/.openclaw/agents/engineer/openclaw.json
/root/.openclaw/agents/creator/openclaw.json
/root/.openclaw/agents/exam/openclaw.json
```

### 配置模板

```json
{
  "meta": {
    "name": "commander",
    "role": "总指挥"
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "moonshot/kimi-k2.5"
      },
      "workspace": "/root/.openclaw/workspace-agents/commander",
      "contextTokens": 200000
    }
  },
  "channels": {
    "discord": {
      "enabled": true,
      "token": "YOUR_COMMANDER_BOT_TOKEN",
      "groupPolicy": "open"
    }
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "loopback"
  }
}
```

### 关键配置差异

每个角色的配置主要区别：
1. `meta.name` - 角色标识
2. `meta.role` - 角色名称
3. `agents.defaults.workspace` - 工作目录
4. `channels.discord.token` - Bot Token

## 启动脚本

创建启动脚本 `/root/.openclaw/start-agents.sh`：

```bash
#!/bin/bash
# 启动 5 个角色 Bot

echo "🚀 启动 5 角色协作系统..."

# 启动总指挥
CONFIG_DIR=/root/.openclaw/agents/commander
openclaw --config $CONFIG_DIR/openclaw.json &
echo "✅ 总指挥已启动"

# 启动军师
CONFIG_DIR=/root/.openclaw/agents/junshi
openclaw --config $CONFIG_DIR/openclaw.json &
echo "✅ 军师已启动"

# 启动工程师
CONFIG_DIR=/root/.openclaw/agents/engineer
openclaw --config $CONFIG_DIR/openclaw.json &
echo "✅ 工程师已启动"

# 启动创作官
CONFIG_DIR=/root/.openclaw/agents/creator
openclaw --config $CONFIG_DIR/openclaw.json &
echo "✅ 创作官已启动"

# 启动检查官
CONFIG_DIR=/root/.openclaw/agents/exam
openclaw --config $CONFIG_DIR/openclaw.json &
echo "✅ 检查官已启动"

echo "🎉 所有角色已启动！"
echo "在 Discord 中使用 @Commander @军师 @工程师 @创作官 @检查官 召唤他们"
```

## 文件结构

```
/root/.openclaw/
├── agents/
│   ├── commander/
│   │   └── openclaw.json
│   ├── junshi/
│   │   └── openclaw.json
│   ├── engineer/
│   │   └── openclaw.json
│   ├── creator/
│   │   └── openclaw.json
│   └── exam/
│       └── openclaw.json
├── workspace-agents/          # 每个角色的工作目录
│   ├── commander/
│   ├── junshi/
│   ├── engineer/
│   ├── creator/
│   └── exam/
└── start-agents.sh           # 启动脚本
```

## 下一步操作

1. 在 Discord Developer Portal 创建 5 个 Bot
2. 获取 5 个 Bot Token
3. 将 Token 填入对应的配置文件
4. 邀请 5 个 Bot 到你的 Discord 服务器
5. 运行启动脚本

## 注意事项

- 所有 Bot 连接到同一个 Gateway (port 18789)
- 每个 Bot 有独立的 workspace 目录
- 每个 Bot 有独立的记忆和上下文
- 通过 @ 提及可以在 Discord 中召唤特定角色
