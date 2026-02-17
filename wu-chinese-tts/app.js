// 文字转吴语应用主程序

class WuChineseConverter {
    constructor() {
        this.currentDialect = 'shanghai';
        this.pinyinResult = [];
        this.init();
    }

    init() {
        this.bindEvents();
        this.loadVoices();
    }

    bindEvents() {
        // 转换按钮
        document.getElementById('convertBtn').addEventListener('click', () => {
            this.convertText();
        });

        // 播放按钮
        document.getElementById('playBtn').addEventListener('click', () => {
            this.playAudio();
        });

        // 方言选择
        document.getElementById('dialectSelect').addEventListener('change', (e) => {
            this.currentDialect = e.target.value;
            // 如果有内容，自动重新转换
            const input = document.getElementById('inputText').value.trim();
            if (input) {
                this.convertText();
            }
        });

        // 回车转换
        document.getElementById('inputText').addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && e.ctrlKey) {
                this.convertText();
            }
        });
    }

    convertText() {
        const input = document.getElementById('inputText').value.trim();
        if (!input) {
            alert('请输入要转换的文字');
            return;
        }

        const btn = document.getElementById('convertBtn');
        btn.classList.add('loading');
        btn.innerHTML = '<span>⏳</span> 转换中...';

        // 模拟异步处理
        setTimeout(() => {
            this.pinyinResult = getWuPinyin(input, this.currentDialect);
            this.displayResult();
            
            btn.classList.remove('loading');
            btn.innerHTML = '<span>🔄</span> 转换为吴语拼音';
        }, 300);
    }

    displayResult() {
        const outputSection = document.getElementById('outputSection');
        const pinyinOutput = document.getElementById('pinyinOutput');
        
        // 生成HTML
        const html = this.pinyinResult.map(item => {
            return `
                <div class="pinyin-word">
                    <span class="char">${item.char}</span>
                    <span class="pinyin">${item.pinyin}</span>
                </div>
            `;
        }).join('');

        pinyinOutput.innerHTML = html || '<p style="color: #999;">暂无转换结果</p>';
        outputSection.style.display = 'block';

        // 滚动到结果区域
        outputSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    loadVoices() {
        // 检查浏览器是否支持语音合成
        if (!('speechSynthesis' in window)) {
            console.warn('浏览器不支持语音合成');
            document.getElementById('playBtn').style.display = 'none';
            return;
        }

        // 加载语音列表
        this.voices = speechSynthesis.getVoices();
        
        speechSynthesis.onvoiceschanged = () => {
            this.voices = speechSynthesis.getVoices();
            console.log('可用语音:', this.voices.map(v => v.name));
        };
    }

    async playAudio() {
        if (!this.pinyinResult.length) return;

        const btn = document.getElementById('playBtn');
        const voiceSelect = document.getElementById('voiceSelect');
        const voiceType = voiceSelect.value;

        btn.classList.add('loading');
        btn.innerHTML = '<span>🔊</span> 播放中...';

        try {
            // 方案1: 使用Edge-TTS后端API
            await this.playWithEdgeTTS(voiceType);
        } catch (e) {
            console.warn('Edge-TTS失败，回退到浏览器TTS:', e);
            // 方案2: 使用浏览器内置TTS
            this.playWithBrowserTTS(voiceType);
        }

        btn.classList.remove('loading');
        btn.innerHTML = '<span>🔊</span> 播放发音';
    }

    async playWithEdgeTTS(voiceType = 'female') {
        const text = this.pinyinResult.map(item => item.char).join('');
        
        // 选择语音
        const voiceMap = {
            'female': 'zh-CN-XiaoxiaoNeural',  // 晓晓 - 活泼女声
            'female2': 'zh-CN-XiaoyiNeural',    // 晓伊 - 温柔女声
            'male': 'zh-CN-YunjianNeural',      // 云健 - 男声
            'male2': 'zh-CN-YunxiNeural'        // 云希 - 年轻男声
        };
        
        const voice = voiceMap[voiceType] || voiceMap['female'];
        
        // 调用后端API
        const response = await fetch('/api/tts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text: text,
                voice: voice
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'TTS request failed');
        }

        // 获取音频数据
        const audioBlob = await response.blob();
        const audioUrl = URL.createObjectURL(audioBlob);
        
        // 播放音频
        const audio = new Audio(audioUrl);
        audio.playbackRate = 0.9; // 稍慢一点
        
        return new Promise((resolve, reject) => {
            audio.onended = () => {
                URL.revokeObjectURL(audioUrl);
                resolve();
            };
            audio.onerror = (e) => {
                URL.revokeObjectURL(audioUrl);
                reject(e);
            };
            audio.play().catch(reject);
        });
    }

    playWithBrowserTTS(voiceType) {
        const text = this.pinyinResult.map(item => item.char).join('');
        
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'zh-CN';
        utterance.rate = 0.85; // 稍慢一点，更接近方言节奏
        utterance.pitch = 1.0;

        // 选择语音
        if (this.voices && this.voices.length > 0) {
            // 优先选择中文女声
            const preferredVoice = this.voices.find(v => {
                if (voiceType === 'female') {
                    return v.lang.includes('zh') && 
                           (v.name.includes('Xiaoxiao') || 
                            v.name.includes('Female') ||
                            v.name.includes('女'));
                } else {
                    return v.lang.includes('zh') && 
                           (v.name.includes('Yunyang') || 
                            v.name.includes('Male') ||
                            v.name.includes('男'));
                }
            });

            if (preferredVoice) {
                utterance.voice = preferredVoice;
            }
        }

        speechSynthesis.speak(utterance);
    }

    // 导出拼音文本
    exportPinyin() {
        if (!this.pinyinResult.length) return '';
        
        return this.pinyinResult.map(item => {
            return `${item.char}[${item.pinyin}]`;
        }).join(' ');
    }

    // 复制到剪贴板
    async copyToClipboard() {
        const text = this.exportPinyin();
        try {
            await navigator.clipboard.writeText(text);
            alert('已复制到剪贴板！');
        } catch (err) {
            console.error('复制失败:', err);
        }
    }
}

// 初始化应用
document.addEventListener('DOMContentLoaded', () => {
    window.wuConverter = new WuChineseConverter();
});

// 添加一些实用的快捷功能

// 语音播放控制
let currentUtterance = null;

function stopSpeaking() {
    if ('speechSynthesis' in window) {
        speechSynthesis.cancel();
    }
}

// 暂停/继续
function pauseSpeaking() {
    if ('speechSynthesis' in window) {
        if (speechSynthesis.paused) {
            speechSynthesis.resume();
        } else {
            speechSynthesis.pause();
        }
    }
}

// 页面卸载时停止播放
window.addEventListener('beforeunload', stopSpeaking);

// 键盘快捷键
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + Enter = 转换
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        document.getElementById('convertBtn').click();
    }
    
    // Escape = 停止播放
    if (e.key === 'Escape') {
        stopSpeaking();
    }
});

console.log('🎭 文字转吴语 - 已加载完成');
console.log('快捷键：Ctrl+Enter 转换 | Esc 停止播放');
