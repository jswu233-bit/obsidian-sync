# Zoe 的状态看板

这里会同步 Zoe (main agent) 和 sub-agent 的运行状态。

## 当前 Zoe (main) 状态
- **模型**: {{ZOE_MODEL}}
- **当前任务**: 正在协助 Jamie 处理 Obsidian Git 同步及 Opencode 集成
- **上次更新**: {{CURRENT_DATETIME}}

## Sub-agent 状态
- **🕵️ 情报官 (intel)**:
    - **模型**: {{INTEL_MODEL}}
    - **职责**: 搜索、情报收集、信息验证
- **🔧 打杂工 (handyman)**:
    - **模型**: {{HANDYMAN_MODEL}}
    - **职责**: 运维、配置、心跳维护

## Zoe 的核心信息
- **名称**: {{ZOE_NAME}}
- **角色**: {{ZOE_ROLE}}
- **座右铭**: {{ZOE_MOTTO}}

---
**提示**: 此文件会在每次执行 `git-sync` 时自动更新。
