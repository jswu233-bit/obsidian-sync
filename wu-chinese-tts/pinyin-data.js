// 吴语拼音数据库 - 上海话（基于吴语学堂拼音方案）
const wuDictionary = {
    shanghai: {
        // 声母对应关系简化版
        initials: {
            'b': 'p', 'p': 'ph', 'm': 'm', 'f': 'f', 'v': 'v',
            'd': 't', 't': 'th', 'n': 'n', 'l': 'l',
            'g': 'k', 'k': 'kh', 'h': 'h', 'ng': 'ng',
            'j': 'c', 'q': 'ch', 'x': 'sh',
            'zh': 'ts', 'ch': 'tsh', 'sh': 's', 'r': 'z',
            'z': 'ts', 'c': 'tsh', 's': 's'
        },
        // 常用字拼音映射（简化版）
        chars: {
            '你': 'non', '我': 'ngu', '他': 'tha', '她': 'tha', '它': 'tha',
            '好': 'hau', '是': 'zy', '不': 'veh', '在': 'ze', '有': 'yeu',
            '人': 'gnin', '这': 'leq', '那': 'eq', '来': 'le', '去': 'chi',
            '上': 'zaon', '下': 'gho', '大': 'du', '小': 'siau', '多': 'tu',
            '少': 'sau', '天': 'thi', '地': 'di', '水': 'sy', '火': 'hu',
            '山': 'se', '风': 'fon', '雨': 'yu', '雪': 'sih', '云': 'yuen',
            '日': 'gnih', '月': 'yuq', '星': 'shin', '东': 'ton', '西': 'shi',
            '南': 'ne', '北': 'poq', '中': 'tson', '国': 'koq', '家': 'ka',
            '学': 'ghoq', '生': 'san', '先': 'shi', '老': 'lau', '师': 'sy',
            '朋': 'bon', '友': 'yeu', '爱': 'e', '喜': 'shi', '欢': 'hoe',
            '吃': 'chih', '喝': 'heh', '看': 'kheu', '听': 'thin', '说': 'seh',
            '走': 'tseu', '跑': 'bau', '睡': 'zo', '醒': 'shin', '坐': 'zu',
            '站': 'ze', '开': 'khe', '关': 'kue', '给': 'keh', '拿': 'ne',
            '买': 'ma', '卖': 'ma', '钱': 'dzi', '年': 'gni', '月': 'yuq',
            '日': 'gnih', '时': 'zy', '分': 'fen', '秒': 'miau', '点': 'ti',
            '个': 'goq', '了': 'leq', '吗': 'va', '呢': 'neq', '吧': 'pa',
            '很': 'hen', '太': 'tha', '真': 'tsen', '假': 'ka', '新': 'shin',
            '旧': 'dziu', '长': 'dzan', '短': 'toe', '高': 'kau', '低': 'ti',
            '快': 'khua', '慢': 'me', '早': 'tsau', '晚': 've', '明': 'min',
            '暗': 'oe', '红': 'ghon', '黄': 'waon', '蓝': 'le', '绿': 'loq',
            '白': 'bah', '黑': 'heh', '一': 'ih', '二': 'gni', '三': 'se',
            '四': 'sy', '五': 'ng', '六': 'loq', '七': 'tshih', '八': 'pah',
            '九': 'cieu', '十': 'zeh', '百': 'pah', '千': 'tshi', '万': 've',
            '零': 'lin', '的': 'geq', '得': 'teq', '着': 'zah', '过': 'ku',
            '到': 'tau', '向': 'shian', '从': 'dzon', '把': 'po', '被': 'bi',
            '让': 'gnian', '叫': 'ciau', '请': 'tshin', '谢': 'zia', '对': 'te',
            '错': 'tshou', '能': 'nen', '会': 'we', '要': 'iau', '想': 'shian',
            '知': 'tsy', '道': 'dau', '认': 'gnin', '识': 'seq', '记': 'ci',
            '忘': 'waon', '找': 'tsau', '等': 'ten', '当': 'taon', '应该': 'in-ke',
            '可以': 'khu-i', '上海': 'zaon-he', '北京': 'poq-cin', '中国': 'tson-koq',
            '欢迎': 'hue-gnin', '谢谢': 'zia-zia', '再见': 'tse-zi', '对不起': 'te-ve-chi',
            '没关系': 've-kue-shi', '请问': 'tshin-ven', '你好': 'non-hau',
            '早上好': 'tsau-zaon-hau', '晚上好': 've-zaon-hau', '晚安': 've-oe'
        },
        // 声调标记（上海话简化版）
        tones: {
            '1': '⁵³', '2': '¹³', '3': '³⁵', '4': '¹¹', '5': '³³'
        }
    },
    
    suzhou: {
        // 苏州话简化映射
        chars: {
            '你': 'ne', '我': 'ngu', '他': 'thi', '她': 'thi', '它': 'thi',
            '好': 'hau', '是': 'zy', '不': 'feh', '在': 'ze', '有': 'yeu',
            '人': 'gnin', '这': 'leq', '那': 'eq', '来': 'le', '去': 'chi',
            '上': 'zaon', '下': 'gho', '大': 'du', '小': 'siae', '多': 'tu',
            '天': 'thi', '地': 'di', '水': 'sy', '山': 'se',
            '风': 'fon', '雨': 'yu', '日': 'gnih', '月': 'yuq',
            '东': 'ton', '西': 'shi', '南': 'ne', '北': 'poq',
            '国': 'koq', '家': 'ka', '学': 'ghoq', '生': 'san',
            '爱': 'e', '吃': 'chih', '喝': 'heh', '看': 'kheu',
            '走': 'tseu', '睡': 'zo', '坐': 'zu',
            '买': 'ma', '钱': 'dzi', '年': 'gni',
            '一': 'ih', '二': 'gni', '三': 'se', '四': 'sy',
            '五': 'ng', '六': 'loq', '七': 'tshih', '八': 'pah',
            '九': 'cieu', '十': 'zeh', '的': 'geq',
            '上海': 'zaon-he', '你好': 'ne-hau'
        }
    },
    
    shaoxing: {
        // 绍兴话简化映射
        chars: {
            '你': 'nyi', '我': 'ngou', '他': 'gha', '她': 'gha', '它': 'gha',
            '好': 'hau', '是': 'zy', '不': 'feh', '有': 'yeu',
            '人': 'gnin', '这': 'ciq', '那': 'na', '来': 'le', '去': 'chi',
            '上': 'zaon', '下': 'gho', '大': 'du', '小': 'siau',
            '天': 'thi', '水': 'sy', '山': 'sae',
            '东': 'ton', '西': 'shi', '国': 'koq', '家': 'ko',
            '学': 'ghoq', '爱': 'ae', '吃': 'chih', '看': 'khoe',
            '走': 'tseu', '买': 'ma', '钱': 'dzi',
            '一': 'ih', '二': 'gni', '三': 'sae', '四': 'sy',
            '五': 'ng', '六': 'loq', '七': 'tshih', '八': 'paeh',
            '九': 'cieu', '十': 'zeh',
            '绍兴': 'sau-chin', '你好': 'nyi-hau'
        }
    }
};

// 多音字处理
const polyphonicChars = {
    '了': ['leq', 'lau'],
    '地': ['di', 'di'],
    '得': ['teq', 'teq', 'teq'],
    '着': ['zah', 'tsaq', 'tsaq'],
    '过': ['ku', 'ku'],
    '的': ['geq', 'di', 'di']
};

// 常用词组
const phrases = {
    shanghai: {
        '你好': 'non-hau',
        '谢谢': 'zia-zia',
        '再见': 'tse-zi',
        '对不起': 'te-ve-chi',
        '没关系': 've-kue-shi',
        '早上好': 'tsau-zaon-hau',
        '晚上好': 've-zaon-hau',
        '晚安': 've-oe',
        '请问': 'tshin-ven',
        '欢迎': 'hue-gnin'
    }
};

// 获取拼音函数
function getWuPinyin(text, dialect = 'shanghai') {
    const dict = wuDictionary[dialect] || wuDictionary.shanghai;
    const result = [];
    
    // 先匹配词组
    let remaining = text;
    while (remaining.length > 0) {
        let matched = false;
        
        // 尝试匹配2-4字词组
        for (let len = Math.min(4, remaining.length); len >= 1; len--) {
            const substr = remaining.substring(0, len);
            if (dict.chars[substr]) {
                result.push({
                    char: substr,
                    pinyin: dict.chars[substr]
                });
                remaining = remaining.substring(len);
                matched = true;
                break;
            }
        }
        
        if (!matched) {
            // 单字匹配
            const char = remaining[0];
            result.push({
                char: char,
                pinyin: dict.chars[char] || `[${char}]`
            });
            remaining = remaining.substring(1);
        }
    }
    
    return result;
}

// 导出
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { wuDictionary, getWuPinyin, polyphonicChars, phrases };
}
