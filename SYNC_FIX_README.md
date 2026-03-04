# Obsidian Git 同步修复说明

## 当前状态
- 远程：`https://github.com/jswu233-bit/obsidian-sync.git`，默认分支 **main**（有提交）
- 本地：在 **master** 分支，且**没有任何提交**，所以无法 push

## 方案 A：以远程为主（推荐）

让本地和 GitHub 上的 `main` 一致，之后在 Obsidian 里正常改笔记、用 Obsidian Git 备份即可。

在 **PowerShell** 里进入仓库目录后执行：

```powershell
cd "d:\Mi2\03_openclaw\openclaw"

# 1. 切换到 main 并和远程对齐（会得到远程已有内容）
git checkout -B main origin/main

# 2. 之后在 Obsidian 里点「Pull」再「Commit」+「Push」即可
```

若本地有未跟踪文件（如 `.obsidian`）且不想被覆盖，可先备份再执行上述命令。

---

## 方案 B：以本地为主，把当前内容推上去

若你希望把**当前 vault 里的内容**作为“第一版”推到 GitHub（注意：可能覆盖或与远程 main 冲突）：

```powershell
cd "d:\Mi2\03_openclaw\openclaw"

# 1. 添加并提交所有文件
git add .
git commit -m "vault backup: initial"

# 2. 推送到远程 main（若远程 main 已有内容，会冲突，需先 pull 或协商）
git branch -M main
git push -u origin main
```

若远程 `main` 已有重要内容，请先用方案 A 拉下来再合并，不要直接 force push。

---

## 常见“没法同步”原因

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| Push 失败 / 无内容可推 | 本地没有 commit | 先在 Obsidian Git 里点「Commit」或按方案 B 在命令行 commit |
| Pull 没反应或报错 | 本地在 master、远程默认 main | 用方案 A 切换到 `main` 并 `git pull` |
| 认证失败 (403/401) | GitHub 账号或权限问题 | 检查 GitHub 登录、Token 或 SSH key；HTTPS 需用 Personal Access Token |

按上面选一个方案执行后，再在 Obsidian 里试一次「Pull」/「Push」即可。
