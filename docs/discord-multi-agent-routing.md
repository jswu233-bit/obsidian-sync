# Discord 多 Agent 路由配置指南

## 配置文件位置

主配置文件：`~/.openclaw/openclaw.json`

## 配置架构

### 1. Agent 定义 (`agents.list`)

定义所有可用的 agent，每个 agent 有独立的 workspace 和模型配置。

```json
{
  "agents": {
    "list": [
      {
        "id": "main",
        "model": "aigocode/claude-opus-4-6",
        "workspace": "/Users/jamiewu/.openclaw/workspace",
        "subagents": {
          "allowAgents": ["joy", "ops", "spy"]
        }
      },
      {
        "id": "spy",
        "name": "Spy",
        "workspace": "/Users/jamiewu/.openclaw/workspace-spy",
        "agentDir": "/Users/jamiewu/.openclaw/workspace-spy/agent",
        "model": "kimicode/kimi-k2.5"
      },
      {
        "id": "joy",
        "name": "Joy",
        "workspace": "/Users/jamiewu/.openclaw/workspace-joy",
        "agentDir": "/Users/jamiewu/.openclaw/workspace-joy/agent",
        "model": "kimicode/kimi-k2.5"
      },
      {
        "id": "ops",
        "name": "Ops",
        "workspace": "/Users/jamiewu/.openclaw/workspace-ops",
        "agentDir": "/Users/jamiewu/.openclaw/workspace-ops/agent",
        "model": "kimicode/kimi-k2.5"
      }
    ]
  }
}
```

**字段说明**：
- `id`: Agent 唯一标识符
- `name`: 显示名称
- `workspace`: 工作目录路径（存放 SOUL.md、MEMORY.md 等）
- `agentDir`: Agent 配置目录
- `model`: 使用的 AI 模型
- `subagents.allowAgents`: 允许调用的子 agent 列表

### 2. Discord 账号配置 (`channels.discord.accounts`)

为每个 Discord bot 配置独立的账号。

```json
{
  "channels": {
    "discord": {
      "enabled": true,
      "groupPolicy": "allowlist",
      "accounts": {
        "zoe": {
          "name": "Zoe",
          "enabled": true,
          "token": "MTQ3MjgzNDI4MzgwMTQxNTcwMg.GvZmQh...",
          "groupPolicy": "open"
        },
        "spy": {
          "name": "Spy",
          "enabled": true,
          "token": "MTQ4MDExNDYzOTA2Mzg3NTY4Ng.G43VYD...",
          "groupPolicy": "allowlist",
          "guilds": {
            "1472836335151747296": {
              "channels": {
                "1480092226754183229": {
                  "allow": true
                }
              }
            }
          }
        },
        "joy": {
          "name": "Joy",
          "enabled": true,
          "token": "MTQ4MDExNjUxNTczMzc3MDM1Mg.Gi0MfA...",
          "groupPolicy": "allowlist",
          "guilds": {
            "1472836335151747296": {
              "channels": {
                "1480092226754183229": {
                  "allow": true
                }
              }
            }
          }
        },
        "ops": {
          "name": "Ops",
          "enabled": true,
          "token": "MTQ4MDExNzIxODg3OTQ3MTc0OA.GncHah...",
          "groupPolicy": "allowlist",
          "guilds": {
            "1472836335151747296": {
              "channels": {
                "1480092226754183229": {
                  "allow": true
                }
              }
            }
          }
        }
      }
    }
  }
}
```

**字段说明**：
- `token`: Discord bot token（从 Discord Developer Portal 获取）
- `groupPolicy`: 群组消息策略（`open` 或 `allowlist`）
- `guilds`: 允许的服务器和频道白名单

### 3. 路由绑定 (`bindings`) ⭐ 核心配置

通过 `bindings` 将 Discord 账号映射到对应的 agent。

```json
{
  "bindings": [
    {
      "match": {
        "channel": "discord",
        "accountId": "spy"
      },
      "agentId": "spy"
    },
    {
      "match": {
        "channel": "discord",
        "accountId": "joy"
      },
      "agentId": "joy"
    },
    {
      "match": {
        "channel": "discord",
        "accountId": "ops"
      },
      "agentId": "ops"
    }
  ]
}
```

**工作原理**：
- 当消息发送给 Discord 账号 `spy` 时，OpenClaw 匹配到 `accountId: "spy"`
- 然后路由到 `agentId: "spy"`，使用 spy 的 workspace 和配置
- 每个 bot 账号都有独立的路由规则

## 路由优先级

OpenClaw 按以下顺序匹配路由规则（从高到低）：

1. **精确 peer 匹配** - 特定用户/群组 ID
2. **Parent peer 匹配** - 线程继承
3. **Guild + roles 匹配** - Discord 服务器 + 角色
4. **Guild 匹配** - Discord 服务器
5. **Account 匹配** ⭐ - Discord 账号（我们使用的方式）
6. **Channel 匹配** - 整个渠道
7. **默认 agent** - 兜底规则

## 配置方法

### 方法 1：使用 CLI 命令（推荐）

```bash
# 1. 设置 bindings
openclaw config set bindings '[
  {
    "match": {"channel": "discord", "accountId": "spy"},
    "agentId": "spy"
  },
  {
    "match": {"channel": "discord", "accountId": "joy"},
    "agentId": "joy"
  },
  {
    "match": {"channel": "discord", "accountId": "ops"},
    "agentId": "ops"
  }
]' --json

# 2. 验证配置
openclaw config get bindings

# 3. 重启 gateway 应用配置
openclaw gateway restart
```

### 方法 2：直接编辑配置文件

```bash
# 1. 编辑配置文件
nano ~/.openclaw/openclaw.json

# 2. 在根级别添加 bindings 字段（与 agents、channels 同级）
# 3. 保存后重启
openclaw gateway restart
```

## 验证配置

```bash
# 查看当前 bindings
openclaw config get bindings

# 查看 agents 列表
openclaw config get agents.list

# 查看 Discord 账号配置
openclaw config get channels.discord.accounts

# 检查 gateway 状态
openclaw gateway status

# 查看实时日志
openclaw logs --follow
```

## 工作流程示例

### 场景 1：单聊 Spy

1. 用户在 Discord 单聊 Spy bot
2. OpenClaw 识别到 `accountId: "spy"`
3. 匹配到 binding 规则：`agentId: "spy"`
4. 使用 `/Users/jamiewu/.openclaw/workspace-spy/` 作为工作目录
5. 使用 `kimicode/kimi-k2.5` 模型回复

### 场景 2：群聊 @Joy

1. 用户在 Discord 群聊 @Joy
2. OpenClaw 识别到 `accountId: "joy"`
3. 匹配到 binding 规则：`agentId: "joy"`
4. 使用 `/Users/jamiewu/.openclaw/workspace-joy/` 作为工作目录
5. 使用 `kimicode/kimi-k2.5` 模型回复

### 场景 3：Zoe（默认）

1. 用户在 Discord 单聊 Zoe bot
2. OpenClaw 识别到 `accountId: "zoe"`
3. 没有匹配的 binding，使用默认 agent `main`
4. 使用 `/Users/jamiewu/.openclaw/workspace/` 作为工作目录
5. 使用 `aigocode/claude-opus-4-6` 模型回复

## 常见问题

### Q1: 为什么 @Spy 还是路由到 Zoe？

**原因**：没有配置 bindings 或 gateway 没有重启。

**解决**：
```bash
# 检查 bindings
openclaw config get bindings

# 如果为空，设置 bindings
openclaw config set bindings '[...]' --json

# 重启 gateway
openclaw gateway restart
```

### Q2: 如何添加新的 agent？

**步骤**：
1. 在 `agents.list` 中添加新 agent 定义
2. 在 `channels.discord.accounts` 中添加新 bot 账号
3. 在 `bindings` 中添加路由规则
4. 重启 gateway

### Q3: 如何查看当前路由状态？

```bash
# 查看所有 sessions
openclaw sessions list

# 查看 gateway 日志
openclaw logs --follow

# 检查配置
openclaw doctor
```

## 目录结构

```
~/.openclaw/
├── openclaw.json              # 主配置文件
├── workspace/                 # Zoe (main) 工作目录
│   ├── SOUL.md
│   ├── MEMORY.md
│   └── ...
├── workspace-spy/             # Spy 工作目录
│   ├── agent/
│   ├── SOUL.md
│   └── ...
├── workspace-joy/             # Joy 工作目录
│   ├── agent/
│   ├── SOUL.md
│   └── ...
└── workspace-ops/             # Ops 工作目录
    ├── agent/
    ├── SOUL.md
    └── ...
```

## 相关文档

- [OpenClaw Discord 文档](https://docs.openclaw.ai/channels/discord)
- [Channel Routing 文档](https://docs.openclaw.ai/channels/channel-routing)
- [Multi-Agent 文档](https://docs.openclaw.ai/concepts/multi-agent)

---

**最后更新**: 2026-03-09
**配置版本**: OpenClaw 2026.3.2
