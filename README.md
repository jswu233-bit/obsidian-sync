# Zoe 同步笔记

这个仓库用于 VPS (OpenClaw) 和本地 Obsidian 之间的双向同步。

## 目录结构

```
obsidian-sync/
├── 📥 inbox/           # 我查询的内容先放在这里
├── 📤 outbox/          # 需要你处理的内容
├── 📚 knowledge/       # 整理后的知识库
└── 📝 daily/           # 每日笔记
```

## 工作流程

1. **我查询内容** → 写入 `inbox/`
2. **Git push** → 同步到远程仓库
3. **你本地 pull** → 在 Obsidian 中查看
4. **你整理后** → 移动到 `knowledge/` 或 `outbox/`
5. **Git push** → 我可以看到你的更新

---

*Last updated: 2026-02-17*
