#!/bin/bash
# 自动同步 workspace 配置文件到 Git
# 每天运行，将 /root/.openclaw/workspace/ 下的关键文件同步到 obsidian-sync/workspace/

SOURCE_DIR="/Users/jamiewu/.openclaw/workspace"
TARGET_DIR="/Users/jamiewu/.openclaw/workspace/obsidian-sync/workspace"

echo "🔄 开始同步 workspace 文件..."
echo "⏰ 时间: $(date '+%Y-%m-%d %H:%M:%S')"

# 确保目标目录存在
mkdir -p "$TARGET_DIR"

# 同步关键文件
files=("IDENTITY.md" "SOUL.md" "USER.md" "MEMORY.md" "AGENTS.md" "TOOLS.md" "BOOTSTRAP.md" "HEARTBEAT.md")

for file in "${files[@]}"; do
    if [ -f "$SOURCE_DIR/$file" ]; then
        cp "$SOURCE_DIR/$file" "$TARGET_DIR/"
        echo "  ✅ 已同步: $file ($(stat -c%s "$SOURCE_DIR/$file") bytes)"
    else
        echo "  ⚠️  文件不存在: $file"
    fi
done

# 同步 memory 文件夹（如果存在）
if [ -d "$SOURCE_DIR/memory" ]; then
    mkdir -p "$TARGET_DIR/memory"
    cp -r "$SOURCE_DIR/memory/"* "$TARGET_DIR/memory/" 2>/dev/null || true
    echo "  ✅ 已同步: memory/ 文件夹"
fi

# 同步 skills 文件夹（如果存在）
if [ -d "$SOURCE_DIR/skills" ]; then
    mkdir -p "$TARGET_DIR/skills"
    cp -r "$SOURCE_DIR/skills/"* "$TARGET_DIR/skills/" 2>/dev/null || true
    echo "  ✅ 已同步: skills/ 文件夹"
fi

# 确保 daily 目录存在 (Obsidian 仓库根目录下的 daily)
DAILY_DIR="/Users/jamiewu/.openclaw/workspace/obsidian-sync/daily"
if [ ! -d "$DAILY_DIR" ]; then
    mkdir -p "$DAILY_DIR"
    echo "  📁 已创建: daily/ 目录"
fi

# 确保 box 目录存在（用于 Jamie 和 Zoe 之间的信息交换）
BOX_DIR="/Users/jamiewu/.openclaw/workspace/obsidian-sync/box"
if [ ! -d "$BOX_DIR" ]; then
    mkdir -p "$BOX_DIR"
    echo "  📁 已创建: box/ 目录"
fi

# 移除 dashboard 目录及其相关逻辑 (根据 Jamie 的要求)
# DASHBOARD_DIR="/root/.openclaw/workspace/obsidian-sync/box/dashboard"
# if [ ! -d "$DASHBOARD_DIR" ]; then
#     mkdir -p "$DASHBOARD_DIR"
#     echo "  📁 已创建: box/dashboard/ 目录"
# fi

# # 生成并同步 Zoe 的状态文件 (status.md)
# STATUS_TEMPLATE_PATH="$DASHBOARD_DIR/status_template.md"
# STATUS_OUTPUT_PATH="$DASHBOARD_DIR/status.md"

# # 临时创建 status_template.md，以防不存在
# if [ ! -f "$STATUS_TEMPLATE_PATH" ]; then
#     cat << EOF > "$STATUS_TEMPLATE_PATH"
# # Zoe 的状态看板

# 这里会同步 Zoe (main agent) 和 sub-agent 的运行状态。

# ## 当前 Zoe (main) 状态
# - **模型**: {{ZOE_MODEL}}
# - **当前任务**: 正在协助 Jamie 处理 Obsidian Git 同步及 Opencode 集成
# - **上次更新**: {{CURRENT_DATETIME}}

# ## Sub-agent 状态
# - **🕵️ 情报官 (intel)**:
#     - **模型**: {{INTEL_MODEL}}
#     - **职责**: 搜索、情报收集、信息验证
# - **🔧 打杂工 (handyman)**:
#     - **模型**: {{HANDYMAN_MODEL}}
#     - **职责**: 运维、配置、心跳维护

# ## Zoe 的核心信息
# - **名称**: {{ZOE_NAME}}
# - **角色**: {{ZOE_ROLE}}
# - **座右铭**: {{ZOE_MOTTO}}

# ---
# **提示**: 此文件会在每次执行 `git-sync` 时自动更新。
# EOF
# fi

# if [ -f "$STATUS_TEMPLATE_PATH" ]; then
#     # 获取 Zoe 的当前模型 (从 SOUL.md 提取)
#     SOUL_FILE="$SOURCE_DIR/SOUL.md"
#     ZOE_MODEL=$(grep -A 2 "运行配置 (Runtime)" "$SOUL_FILE" | grep "模型:" | cut -d ':' -f 2- | sed 's/^[[:space:]]*`//g; s/`$//g')

#     # 获取 Zoe 的核心信息 (从 SOUL.md)
#     ZOE_NAME=$(grep -m 1 "Name:" "$SOUL_FILE" | cut -d ':' -f 2- | sed 's/^[[:space:]]*//')
#     ZOE_ROLE=$(grep -m 1 "Role:" "$SOUL_FILE" | cut -d ':' -f 2- | sed 's/^[[:space:]]*//')
#     ZOE_MOTTO=$(grep -m 1 ">" "$SOUL_FILE" | head -n 1 | sed 's/^> //') # 提取座右铭

#     # 获取 Sub-agent 的模型信息 (从 MEMORY.md)
#     MEMORY_FILE="$SOURCE_DIR/MEMORY.md"
#     INTEL_MODEL=$(grep "🕵️ 情报官" "$MEMORY_FILE" | awk '{print $NF}' | head -n 1)
#     HANDYMAN_MODEL=$(grep "🔧 打杂工" "$MEMORY_FILE" | awk '{print $NF}' | head -n 1)

#     CURRENT_DATETIME=$(date '+%Y-%m-%d %H:%M:%S')

#     # 读取模板并替换占位符
#     # 使用 cat 结合 sed -e 的方式进行多行替换，并更换分隔符
#     cat "$STATUS_TEMPLATE_PATH" | \
#     sed -e "s#{{ZOE_MODEL}}#$ZOE_MODEL#g" \
#         -e "s#{{CURRENT_TASK}}#正在协助 Jamie 处理 Obsidian Git 同步及 Opencode 集成#g" \
#         -e "s#{{CURRENT_DATETIME}}#$CURRENT_DATETIME#g" \
#         -e "s#{{INTEL_MODEL}}#$INTEL_MODEL#g" \
#         -e "s#{{HANDYMAN_MODEL}}#$HANDYMAN_MODEL#g" \
#         -e "s#{{ZOE_NAME}}#$ZOE_NAME#g" \
#         -e "s#{{ZOE_ROLE}}#$ZOE_ROLE#g" \
#         -e "s#{{ZOE_MOTTO}}#$ZOE_MOTTO#g" \
#         > "$STATUS_OUTPUT_PATH"

#     echo "  ✅ 已生成并同步: box/dashboard/status.md"
# else
#     echo "  ⚠️  Zoe 状态模板文件不存在: $STATUS_TEMPLATE_PATH"
# fi

echo "✅ Workspace 文件同步完成"

# 执行 Git 同步
cd /Users/jamiewu/.openclaw/workspace/obsidian-sync || exit 1

# 先拉取远程最新更改
echo "📥 拉取远程最新更改..."
git pull origin main || echo "⚠️ 拉取失败，继续本地同步"

# 检查是否有更改
if git diff --quiet && git diff --staged --quiet; then
    echo "📦 Git: 没有需要同步的更改"
    echo "✅ 同步检查完成，无需提交"
    exit 0
fi

# 添加所有更改
echo "📤 添加更改到暂存区..."
git add .

# 提交更改
echo "💾 提交更改..."
git commit -m "Sync workspace files: $(date '+%Y-%m-%d %H:%M')" || true

# 推送到远程
echo "🚀 推送到 GitHub..."
git push origin main

if [ $? -eq 0 ]; then
    echo "🎉 已成功同步到 GitHub!"
else
    echo "❌ Git 同步失败"
    exit 1
fi
