#!/usr/bin/env python3
"""
文字转吴语 - Edge-TTS 后端服务
"""

import http.server
import socketserver
import json
import subprocess
import os
import tempfile
import base64
from urllib.parse import parse_qs, urlparse

PORT = 8080

class TTSHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        parsed = urlparse(self.path)
        
        # API: 获取可用语音列表
        if parsed.path == '/api/voices':
            self.send_voices_list()
            return
        
        # API: 文字转语音
        if parsed.path == '/api/tts':
            query = parse_qs(parsed.query)
            text = query.get('text', [''])[0]
            voice = query.get('voice', ['zh-CN-XiaoxiaoNeural'])[0]
            
            if not text:
                self.send_error(400, "Missing text parameter")
                return
            
            self.handle_tts(text, voice)
            return
        
        # 静态文件服务
        super().do_GET()
    
    def do_POST(self):
        parsed = urlparse(self.path)
        
        # API: 文字转语音 (POST方式)
        if parsed.path == '/api/tts':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            try:
                data = json.loads(post_data)
                text = data.get('text', '')
                voice = data.get('voice', 'zh-CN-XiaoxiaoNeural')
                
                if not text:
                    self.send_json_response({'error': 'Missing text'}, 400)
                    return
                
                self.handle_tts(text, voice)
                return
            except json.JSONDecodeError:
                self.send_json_response({'error': 'Invalid JSON'}, 400)
                return
        
        # 默认返回404
        self.send_error(404)
    
    def handle_tts(self, text, voice):
        """处理TTS请求"""
        try:
            # 创建临时文件
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
                output_file = f.name
            
            # 调用 edge-tts
            cmd = [
                'edge-tts',
                '--voice', voice,
                '--text', text,
                '--write-media', output_file
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode != 0:
                print(f"Edge-TTS Error: {result.stderr}")
                # 如果 edge-tts 失败，返回模拟音频数据（空音频）
                self.send_json_response({
                    'success': False,
                    'error': 'TTS generation failed',
                    'fallback': True
                })
                return
            
            # 读取生成的音频文件
            with open(output_file, 'rb') as f:
                audio_data = f.read()
            
            # 删除临时文件
            os.unlink(output_file)
            
            # 发送音频数据
            self.send_response(200)
            self.send_header('Content-Type', 'audio/mpeg')
            self.send_header('Content-Length', len(audio_data))
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(audio_data)
            
        except subprocess.TimeoutExpired:
            self.send_json_response({'error': 'TTS timeout'}, 504)
        except FileNotFoundError:
            # edge-tts 未安装
            self.send_json_response({
                'success': False,
                'error': 'edge-tts not installed. Run: pip install edge-tts',
                'install_command': 'pip install edge-tts'
            }, 503)
        except Exception as e:
            print(f"Error: {e}")
            self.send_json_response({'error': str(e)}, 500)
    
    def send_voices_list(self):
        """发送可用语音列表"""
        voices = [
            {'name': 'zh-CN-XiaoxiaoNeural', 'desc': '晓晓 - 女声（活泼）', 'gender': 'female'},
            {'name': 'zh-CN-XiaoyiNeural', 'desc': '晓伊 - 女声（温柔）', 'gender': 'female'},
            {'name': 'zh-CN-YunjianNeural', 'desc': '云健 - 男声', 'gender': 'male'},
            {'name': 'zh-CN-YunxiNeural', 'desc': '云希 - 男声（年轻）', 'gender': 'male'},
            {'name': 'zh-CN-YunyangNeural', 'desc': '云扬 - 男声（新闻）', 'gender': 'male'},
            {'name': 'zh-CN-liaoning-XiaobeiNeural', 'desc': '晓北 - 东北话女声', 'gender': 'female'},
            {'name': 'zh-CN-shaanxi-XiaoniNeural', 'desc': '晓妮 - 陕西话女声', 'gender': 'female'},
            {'name': 'zh-HK-HiuMaanNeural', 'desc': '晓曼 - 粤语女声', 'gender': 'female'},
            {'name': 'zh-TW-HsiaoChenNeural', 'desc': '晓晨 - 台湾女声', 'gender': 'female'},
        ]
        self.send_json_response({'voices': voices})
    
    def send_json_response(self, data, status=200):
        """发送JSON响应"""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())
    
    def end_headers(self):
        # 添加CORS支持
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def guess_type(self, path):
        if path.endswith('.js'):
            return 'application/javascript'
        return super().guess_type(path)

def get_ip():
    """获取本机IP地址"""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 获取IP地址
    HOST = "0.0.0.0"  # 监听所有网络接口
    LOCAL_IP = get_ip()
    
    with socketserver.TCPServer((HOST, PORT), TTSHandler) as httpd:
        print(f"🎭 文字转吴语服务器已启动！")
        print(f"=" * 50)
        print(f"📱 本地访问: http://localhost:{PORT}")
        print(f"🌐 局域网访问: http://{LOCAL_IP}:{PORT}")
        print(f"🌍 外网访问: http://<你的腾讯云公网IP>:{PORT}")
        print(f"=" * 50)
        print(f"🎙️ API地址: http://{LOCAL_IP}:{PORT}/api/tts")
        print()
        print("⚠️  注意：")
        print("   1. 首次使用需要先安装 edge-tts: pip install edge-tts")
        print("   2. 确保腾讯云安全组已开放端口 8080")
        print("   3. 确保服务器防火墙允许 8080 端口")
        print()
        print("🛑 按 Ctrl+C 停止服务器")
        print()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 服务器已停止")
