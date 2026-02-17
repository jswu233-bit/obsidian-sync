#!/usr/bin/env python3
"""
文字转吴语 - Edge-TTS 后端服务 (简化版)
"""

import http.server
import socketserver
import json
import subprocess
import os
import tempfile
from urllib.parse import parse_qs, urlparse

PORT = 8080

class TTSHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        
        if parsed.path == '/api/voices':
            self.send_voices_list()
            return
        
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
        
        self.send_error(404)
    
    def handle_tts(self, text, voice):
        """处理TTS请求"""
        try:
            # 检查 edge-tts 是否安装
            result = subprocess.run(['which', 'edge-tts'], capture_output=True)
            if result.returncode != 0:
                self.send_json_response({
                    'error': 'edge-tts not found',
                    'install': 'pip3 install edge-tts'
                }, 503)
                return
            
            # 创建临时文件
            output_file = tempfile.mktemp(suffix='.mp3')
            
            # 调用 edge-tts
            cmd = ['edge-tts', '--voice', voice, '--text', text, '--write-media', output_file]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode != 0:
                self.send_json_response({'error': 'TTS generation failed'}, 500)
                return
            
            # 读取音频文件
            with open(output_file, 'rb') as f:
                audio_data = f.read()
            
            os.unlink(output_file)
            
            # 发送音频
            self.send_response(200)
            self.send_header('Content-Type', 'audio/mpeg')
            self.send_header('Content-Length', len(audio_data))
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(audio_data)
            
        except subprocess.TimeoutExpired:
            self.send_json_response({'error': 'TTS timeout'}, 504)
        except Exception as e:
            self.send_json_response({'error': str(e)}, 500)
    
    def send_voices_list(self):
        voices = [
            {'name': 'zh-CN-XiaoxiaoNeural', 'desc': '晓晓 - 女声（活泼）'},
            {'name': 'zh-CN-XiaoyiNeural', 'desc': '晓伊 - 女声（温柔）'},
            {'name': 'zh-CN-YunjianNeural', 'desc': '云健 - 男声'},
            {'name': 'zh-CN-YunxiNeural', 'desc': '云希 - 男声（年轻）'},
        ]
        self.send_json_response({'voices': voices})
    
    def send_json_response(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())
    
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("0.0.0.0", PORT), TTSHandler) as httpd:
        import socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
        except:
            ip = "127.0.0.1"
        
        print(f"🎭 服务器已启动！")
        print(f"🌐 http://{ip}:8080")
        print(f"🛑 Ctrl+C 停止")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 已停止")
