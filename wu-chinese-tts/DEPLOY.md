# 🌐 腾讯云VPS部署指南

## 快速开始

### 1. 安装依赖

```bash
# 连接到腾讯云VPS
ssh root@你的VPS_IP

# 进入项目目录
cd /root/.openclaw/workspace/wu-chinese-tts

# 安装 edge-tts
pip3 install edge-tts

# 如果没有pip3，先安装
apt-get update && apt-get install -y python3-pip
```

### 2. 启动服务器

```bash
python3 server.py
```

你应该看到：
```
🎭 文字转吴语服务器已启动！
==================================================
📱 本地访问: http://localhost:8080
🌐 局域网访问: http://172.16.0.6:8080
🌍 外网访问: http://<你的腾讯云公网IP>:8080
==================================================
```

### 3. 开放端口（关键步骤！）

#### 方法一：腾讯云控制台（推荐）

1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/)
2. 进入「云服务器」→「安全组」
3. 找到你的服务器所在的安全组，点击「修改规则」
4. 点击「入站规则」→「添加规则」
5. 配置如下：
   - 协议端口：`TCP:8080`
   - 策略：`允许`
   - 来源：`0.0.0.0/0`（或你的本地IP）
6. 点击「完成」

#### 方法二：服务器命令行

```bash
# 使用 ufw（Ubuntu）
ufw allow 8080/tcp
ufw reload

# 或者使用 iptables
iptables -I INPUT -p tcp --dport 8080 -j ACCEPT

# 保存规则（CentOS）
service iptables save
```

### 4. 本地访问

在你的本地电脑浏览器中打开：
```
http://<你的腾讯云公网IP>:8080
```

例如：
```
http://123.456.789.012:8080
```

---

## 🔒 安全建议

### 1. 限制访问IP（可选）

如果你只想让自己访问，可以修改安全组规则：
- 来源：你的本地IP地址（如 `203.0.113.1/32`）

### 2. 使用Nginx反向代理（生产环境推荐）

```bash
# 安装 nginx
apt-get install nginx

# 创建配置文件
cat > /etc/nginx/sites-available/wu-chinese << 'EOF'
server {
    listen 80;
    server_name your-domain.com;  # 或使用你的IP

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
EOF

# 启用配置
ln -s /etc/nginx/sites-available/wu-chinese /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

然后就可以直接用 `http://your-domain.com` 访问，无需端口。

### 3. 使用 HTTPS（SSL证书）

```bash
# 安装 certbot
apt-get install certbot python3-certbot-nginx

# 申请证书
certbot --nginx -d your-domain.com

# 自动续期
certbot renew --dry-run
```

---

## 🚀 后台运行（守护进程）

### 方法一：使用 nohup

```bash
# 启动（后台运行，断开SSH也能保持）
nohup python3 server.py > server.log 2>&1 &

# 查看进程
ps aux | grep server.py

# 停止进程
kill <进程ID>
```

### 方法二：使用 systemd（推荐）

```bash
# 创建服务文件
sudo cat > /etc/systemd/system/wu-chinese.service << 'EOF'
[Unit]
Description=文字转吴语服务
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/.openclaw/workspace/wu-chinese-tts
ExecStart=/usr/bin/python3 server.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

# 启动服务
systemctl daemon-reload
systemctl enable wu-chinese
systemctl start wu-chinese

# 查看状态
systemctl status wu-chinese

# 查看日志
journalctl -u wu-chinese -f

# 停止服务
systemctl stop wu-chinese
```

---

## 📱 移动端访问

只要在同一个网络，或服务器有公网IP，手机浏览器也可以访问：
```
http://<你的腾讯云公网IP>:8080
```

---

## 🆘 常见问题

### 1. 无法访问，连接超时

检查清单：
- [ ] 服务器是否已启动 `python3 server.py`
- [ ] 腾讯云安全组是否已开放 8080 端口
- [ ] 服务器防火墙是否允许 8080 端口
- [ ] 使用的IP是否正确（公网IP，不是内网IP）

### 2. 端口冲突

如果8080被占用，可以修改端口：
```python
# 修改 server.py 中的 PORT 变量
PORT = 8081  # 或其他端口
```

### 3. edge-tts 安装失败

```bash
# 尝试升级pip
python3 -m pip install --upgrade pip

# 或者使用conda
conda install -c conda-forge edge-tts
```

### 4. 音频无法播放

检查浏览器控制台（F12）是否有CORS错误。server.py已经配置了CORS，如果还有问题，检查是否有CDN或其他代理。

---

## 📝 总结

最简单的部署流程：

```bash
# 1. 连接服务器
ssh root@你的VPS_IP

# 2. 进入目录
cd /root/.openclaw/workspace/wu-chinese-tts

# 3. 安装依赖
pip3 install edge-tts

# 4. 开放端口（在腾讯云控制台操作）
# 安全组 → 入站规则 → 添加 TCP:8080

# 5. 启动服务
python3 server.py

# 6. 本地访问
# http://你的VPS_IP:8080
```

搞定！🎉
