# 🚀 5 角色 AI 协作系统 - 详细设置教程

## 📋 准备工作

### 你需要准备：
1. Discord 账号
2. 一个 Discord 服务器（或创建新的）
3. 约 30 分钟时间

---

## 第一步：创建 Discord 服务器

### 1.1 打开 Discord
- 访问 https://discord.com 或打开 Discord App
- 登录你的账号

### 1.2 创建服务器
1. 点击左侧栏的 **"+"** 号
2. 选择 **"创建我自己的"**
3. 选择 **"仅供我和我的朋友使用"**
4. 输入服务器名称：`AI协作团队`
5. 点击 **"创建"**

✅ **完成标志**: 看到新的服务器出现在左侧栏

---

## 第二步：创建 5 个 Discord Bot

### 2.1 进入 Discord Developer Portal
1. 访问 https://discord.com/developers/applications
2. 点击右上角的 **"New Application"**

### 2.2 创建第一个 Bot - 总指挥
1. 输入名称：`Commander-Bot`
2. 点击 **"Create"**
3. 点击左侧菜单的 **"Bot"**
4. 点击 **"Reset Token"**
5. 点击 **"Copy"** 复制 Token（⚠️ 保存好，只显示一次！）
6. 在 **"Privileged Gateway Intents"** 下开启：
   - ✅ SERVER MEMBERS INTENT
   - ✅ MESSAGE CONTENT INTENT
7. 点击 **"Save Changes"**

### 2.3 设置 Bot 头像和描述
1. 点击 **"General Information"**
2. 上传头像（可以使用 emoji 🎯 生成的图片）
3. 描述填写：`AI协作团队总指挥`

### 2.4 重复创建其他 4 个 Bot
按照同样步骤创建：

| Bot 名称 | 头像 | 描述 |
|---------|------|------|
| Junshi-Bot | 🧠 | AI协作团队军师 |
| Engineer-Bot | 🔧 | AI协作团队工程师 |
| Creator-Bot | ✨ | AI协作团队创作官 |
| Exam-Bot | ✅ | AI协作团队检查官 |

✅ **完成标志**: 5 个 Application 都创建完成，每个都有 Token

---

## 第三步：邀请 Bot 到服务器

### 3.1 生成邀请链接
对每个 Bot 执行以下操作：

1. 进入 Application → **"OAuth2"** → **"URL Generator"**
2. 在 **SCOPES** 中选择：
   - ✅ `bot`
   - ✅ `applications.commands`
3. 在 **BOT PERMISSIONS** 中选择：
   - ✅ Send Messages
   - ✅ Send Messages in Threads
   - ✅ Create Public Threads
   - ✅ Embed Links
   - ✅ Attach Files
   - ✅ Read Message History
   - ✅ Mention Everyone
   - ✅ Add Reactions
   - ✅ Use Slash Commands
4. 复制生成的 URL

### 3.2 邀请 Bot
1. 在浏览器中打开生成的 URL
2. 选择你的服务器 `AI协作团队`
3. 点击 **"授权"**
4. 完成人机验证

### 3.3 重复邀请所有 Bot
5 个 Bot 都要邀请进服务器

✅ **完成标志**: 在服务器成员列表中看到 5 个 Bot

---

## 第四步：配置 OpenClaw

### 4.1 创建配置目录
```bash
mkdir -p /root/.openclaw/agents/{commander,junshi,engineer,creator,exam}
```

### 4.2 创建总指挥的配置文件
创建文件 `/root/.openclaw/agents/commander/openclaw.json`：

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
      "contextTokens": 200000,
      "memorySearch": {
        "provider": "local"
      }
    }
  },
  "channels": {
    "discord": {
      "enabled": true,
      "token": "YOUR_COMMANDER_BOT_TOKEN_HERE",
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

⚠️ **重要**: 将 `YOUR_COMMANDER_BOT_TOKEN_HERE` 替换为实际的 Bot Token

### 4.3 创建军师的配置文件
创建文件 `/root/.openclaw/agents/junshi/openclaw.json`：

```json
{
  "meta": {
    "name": "junshi",
    "role": "军师"
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "moonshot/kimi-k2.5"
      },
      "workspace": "/root/.openclaw/workspace-agents/junshi",
      "contextTokens": 200000
    }
  },
  "channels": {
    "discord": {
      "enabled": true,
      "token": "YOUR_JUNSHI_BOT_TOKEN_HERE",
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

### 4.4 创建其他 3 个角色的配置文件
按照同样格式创建：
- `/root/.openclaw/agents/engineer/openclaw.json`
- `/root/.openclaw/agents/creator/openclaw.json`
- `/root/.openclaw/agents/exam/openclaw.json`

分别替换：
- `name` 和 `role`
- `workspace` 路径
- `token` 为对应的 Bot Token

---

## 第五步：创建启动脚本

### 5.1 创建启动脚本
创建文件 `/root/.openclaw/start-agents.sh`：

```bash
#!/bin/bash
# 启动 5 角色协作系统

echo "🚀 启动 5 角色协作系统..."
echo "=========================="

# 启动总指挥
echo "🎯 启动总指挥..."
CONFIG_DIR=/root/.openclaw/agents/commander
openclaw --config $CONFIG_DIR/openclaw.json &
sleep 2

# 启动军师
echo "🧠 启动军师..."
CONFIG_DIR=/root/.openclaw/agents/junshi
openclaw --config $CONFIG_DIR/openclaw.json &
sleep 2

# 启动工程师
echo "🔧 启动工程师..."
CONFIG_DIR=/root/.openclaw/agents/engineer
openclaw --config $CONFIG_DIR/openclaw.json &
sleep 2

# 启动创作官
echo "✨ 启动创作官..."
CONFIG_DIR=/root/.openclaw/agents/creator
openclaw --config $CONFIG_DIR/openclaw.json &
sleep 2

# 启动检查官
echo "✅ 启动检查官..."
CONFIG_DIR=/root/.openclaw/agents/exam
openclaw --config $CONFIG_DIR/openclaw.json &
sleep 2

echo ""
echo "🎉 所有角色已启动！"
echo "=========================="
echo "在 Discord 中使用以下命令召唤他们："
echo "  @Commander - 总指挥"
echo "  @军师 - 军师"
echo "  @工程师 - 工程师"
echo "  @创作官 - 创作官"
echo "  @检查官 - 检查官"
```

### 5.2 赋予执行权限
```bash
chmod +x /root/.openclaw/start-agents.sh
```

---

## 第六步：启动系统

### 6.1 运行启动脚本
```bash
/root/.openclaw/start-agents.sh
```

### 6.2 检查状态
在 Discord 服务器中：
1. 查看成员列表，确认 5 个 Bot 都显示为在线（绿色状态）
2. 在任意频道发送：`@Commander 你好`
3. 如果 Bot 回复，说明配置成功！

---

## 🎯 快速测试

在 Discord 服务器中测试：

```
你: @Commander 召集团队，我要做一个网站

Commander: 收到！让我召集团队：
@军师 请分析这个需求
@工程师 准备技术方案

军师: [分析结果]
工程师: [技术方案]
```

---

## ⚠️ 常见问题

### Q1: Bot 显示离线？
- 检查 Token 是否正确
- 检查 OpenClaw 是否正常运行
- 查看日志：`openclaw logs`

### Q2: Bot 不回复？
- 确认 Bot 有发送消息权限
- 检查频道权限设置
- 尝试 @Bot 看是否有反应

### Q3: 如何停止所有 Bot？
```bash
pkill -f openclaw
```

---

## 📁 文件清单

创建的文件：
```
/root/.openclaw/
├── agents/
│   ├── commander/openclaw.json
│   ├── junshi/openclaw.json
│   ├── engineer/openclaw.json
│   ├── creator/openclaw.json
│   └── exam/openclaw.json
├── workspace-agents/          # 角色工作目录（已创建）
└── start-agents.sh           # 启动脚本
```

---

**祝你配置顺利！有问题随时问我！** 🎉
