// 吴语拼音字典 - 基于吴语学堂拼音方案
// 包含上海话、苏州话、绍兴话的常用字拼音

const wugniuDict = {
    // 上海话拼音 (基于吴语学堂式拼音)
    shanghai: {
        // 常用字
        '我': 'ngu', '你': 'non', '他': 'tha', '她': 'tha', '它': 'tha',
        '们': 'men', '的': 'geq', '是': 'zy', '了': 'leq', '在': 'ze',
        '有': 'yeu', '和': 'ghu', '与': 'yu', '或': 'huq', '但': 'de',
        '而': 'el', '为': 'we', '因': 'in', '果': 'ku', '以': 'i',
        '也': 'ya', '就': 'dzieu', '都': 'tu', '还': 'we', '又': 'yeu',
        '不': 'peq', '没': 'meq', '无': 'vu', '来': 'le', '去': 'chi',
        '上': 'zaon', '下': 'gho', '中': 'tson', '里': 'li', '外': 'nga',
        '前': 'dzi', '后': 'heu', '左': 'tsu', '右': 'yeu', '东': 'ton',
        '西': 'shi', '南': 'neu', '北': 'poq', '这': 'geq', '那': 'na',
        
        // 人称
        '人': 'gnin', '家': 'ka', '大': 'du', '小': 'siau', '多': 'tu',
        '少': 'sau', '好': 'hau', '坏': 'wa', '老': 'lau', '少': 'sau',
        '男': 'neu', '女': 'nyu', '父': 'vu', '母': 'mo', '爸': 'pa',
        '妈': 'ma', '爷': 'ya', '娘': 'nyian', '哥': 'ku', '姐': 'cia',
        '弟': 'di', '妹': 'me', '子': 'tsy', '儿': 'el', '孙': 'sen',
        
        // 时间
        '日': 'gniq', '月': 'yuq', '年': 'gni', '时': 'zy', '分': 'fen',
        '秒': 'miau', '天': 'thi', '今': 'cin', '明': 'min', '昨': 'zoq',
        '前': 'dzi', '后': 'heu', '早': 'tsau', '晚': 'we', '上': 'zaon',
        '下': 'gho', '午': 'ng', '夜': 'ya', '点': 'ti', '钟': 'tson',
        '刻': 'kheq', '现': 'yi', '从': 'dzon', '到': 'tau', '等': 'ten',
        
        // 地点
        '地': 'di', '方': 'faon', '国': 'koq', '城': 'zen', '市': 'zy',
        '县': 'yi', '区': 'chiu', '街': 'ka', '路': 'lu', '门': 'men',
        '户': 'wu', '房': 'vaon', '屋': 'oq', '室': 'seq', '楼': 'leu',
        '店': 'ti', '厂': 'tsaon', '园': 'yuoe', '场': 'zan', '所': 'su',
        '校': 'ghau', '学': 'ghoq', 
        
        // 上海相关
        '上': 'zaon', '海': 'he', '沪': 'wu', '申': 'sen', '浦': 'phu',
        '江': 'cian', '黄': 'waon', '浦': 'phu', '浦': 'phu', '东': 'ton',
        '新': 'cin', '区': 'chiu', '滩': 'the', '桥': 'dzhiau', '山': 'se',
        '水': 'sy', '河': 'wu', '湖': 'wu', '洋': 'yan', '港': 'kaon',
        
        // 数字
        '一': 'iq', '二': 'gni', '两': 'lian', '三': 'se', '四': 'sy',
        '五': 'ng', '六': 'loq', '七': 'chiq', '八': 'paq', '九': 'cieu',
        '十': 'zeq', '百': 'paq', '千': 'chi', '万': 've', '零': 'lin',
        '第': 'di', '个': 'goq', '只': 'tsaq', '些': 'xia',
        
        // 动词
        '说': 'seq', '话': 'wo', '讲': 'cian', '谈': 'de', '看': 'khe',
        '见': 'ci', '听': 'thin', '想': 'xian', '要': 'iau', '爱': 'e',
        '喜': 'xi', '欢': 'huoe', '知': 'tsy', '道': 'dau', '认': 'gnin',
        '识': 'seq', '记': 'ci', '得': 'teq', '忘': 'maon', '觉': 'ciuq',
        '感': 'keu', '觉': 'ciuq', '做': 'tsu', '作': 'tsoq', '干': 'keu',
        '办': 'be', '理': 'li', '处': 'tshy', '理': 'li', '打': 'tan',
        '开': 'khe', '关': 'kuoe', '给': 'ci', '送': 'son', '拿': 'ne',
        '放': 'faon', '站': 'ze', '坐': 'zu', '走': 'tseu', '跑': 'bau',
        '跳': 'thiau', '吃': 'chiq', '喝': 'heq', '睡': 'ze', '醒': 'cin',
        '死': 'sy', '活': 'weq', '生': 'san', '长': 'tsan', '出': 'tsheq',
        '进': 'cin', '入': 'zeq', '回': 'we', '过': 'ku', '起': 'chi',
        
        // 形容词
        '高': 'kau', '低': 'ti', '长': 'zan', '短': 'toe', '快': 'khua',
        '慢': 'me', '早': 'tsau', '迟': 'zy', '新': 'cin', '旧': 'dzieu',
        '轻': 'chin', '重': 'dzon', '热': 'gniq', '冷': 'lan', '暖': 'noe',
        '凉': 'lian', '干': 'keu', '湿': 'seq', '干': 'keu', '净': 'dzin',
        '脏': 'tsaon', '美': 'me', '丑': 'tsheu', '香': 'xian', '臭': 'tsheu',
        '甜': 'di', '苦': 'khu', '酸': 'soe', '辣': 'laq', '咸': 'we',
        '淡': 'de', '对': 'te', '错': 'tshu', '真': 'tsen', '假': 'ka',
        '实': 'zeq', '虚': 'xy', '难': 'ne', '易': 'yi', '快': 'khua',
        '慢': 'me',
        
        // 名词
        '心': 'cin', '身': 'sen', '体': 'thi', '头': 'deu', '脸': 'li',
        '眼': 'nge', '耳': 'el', '鼻': 'biq', '口': 'kheu', '手': 'seu',
        '脚': 'ciaq', '血': 'xyuq', '肉': 'gnioq', '骨': 'koq', '皮': 'bi',
        '毛': 'mau', '发': 'faq', '衣': 'i', '服': 'voq', '裤': 'khu',
        '裙': 'djyn', '鞋': 'ya', '帽': 'mau', '伞': 'se', '包': 'pau',
        '钱': 'dzi', '饭': 've', '菜': 'tshe', '肉': 'gnioq', '鱼': 'ng',
        '蛋': 'de', '米': 'mi', '面': 'mi', '饭': 've', '水': 'sy',
        '茶': 'zo', '酒': 'cieu', '烟': 'i', '糖': 'daon', '盐': 'yi',
        '油': 'yeu', '书': 'sy', '纸': 'tsy', '笔': 'piq', '画': 'wo',
        '图': 'du', '车': 'tsho', '船': 'ze', '机': 'ci', '器': 'chi',
        '灯': 'ten', '电话': 'di-wo', '电脑': 'di-nau', '电视': 'di-zy',
        '电影': 'di-yin', '音乐': 'yin-ghaq', '歌': 'ku', '声': 'san',
        '色': 'seq', '花': 'ho', '草': 'tshau', '树': 'zy', '木': 'moq',
        '林': 'lin', '森': 'sen', '天': 'thi', '空': 'khon', '地': 'di',
        '太阳': 'tha-yan', '月亮': 'yuq-lian', '星': 'cin', '云': 'yn',
        '风': 'fon', '雨': 'yu', '雪': 'siq', '冰': 'pin', '雾': 'vu',
        '气': 'chi', '火': 'hu', '烟': 'i', '光': 'kuaon', '影': 'yin',
        
        // 代词
        '什么': 'sa', '谁': 'za', '哪': 'na', '怎么': 'tsa', '为什么': 'we-sa',
        '几': 'ci', '多少': 'tu-sau',
        
        // 连词介词
        '把': 'pa', '被': 'be', '让': 'gnian', '给': 'ci', '向': 'xian',
        '对': 'te', '从': 'dzon', '到': 'tau', '在': 'ze', '当': 'taon',
        '于': 'yu', '比': 'pi', '用': 'yon', '按照': 'oe-dze',
        
        // 语气词
        '吗': 'va', '呢': 'neq', '吧': 'pa', '啊': 'a', '呀': 'ya',
        '哇': 'wa', '哪': 'na', '啦': 'la', '咯': 'loq', '唉': 'e',
        '哦': 'voq', '嗯': 'ng', '嘿': 'heq', '哼': 'hen', '唉': 'e',
        
        // 常见词组
        '谢谢': 'xia-xia', '对不起': 'te-fi-chi', '没关系': 've-ku-xi',
        '你好': 'non-hau', '再见': 'tse-zi', '欢迎': 'hua-nen',
        '请': 'chin', '问': 'men', '回答': 'we-taq', '知道': 'tsy-dau',
        '明白': 'min-baq', '理解': 'li-cia', '认识': 'gnin-seq', '觉得': 'ciuq-teq',
        '认为': 'gnin-we', '希望': 'xi-maon', '愿意': 'yu-yi', '喜欢': 'xi-huoe',
        '爱': 'e', '想': 'xian', '要': 'iau', '需要': 'si-iau', '应该': 'in-kaen',
        '可能': 'khe-nen', '一定': 'iq-din', '必须': 'pi-sy', '一定': 'iq-din',
        
        // 食物
        '小笼包': 'siau-lon-pau', '生煎': 'san-ci', '馄饨': 'wen-den',
        '饺子': 'ciau-tsy', '面条': 'mi-diau', '米饭': 'mi-ve',
        '包子': 'pau-tsy', '馒头': 'me-deu', '油条': 'yeu-diau',
        '豆浆': 'deu-cian', '豆腐': 'deu-vu', '红烧肉': 'hon-shau-gnioq',
        '糖醋排骨': 'tan-dzu-ba-geq', '清蒸鱼': 'chin-tshin-ng',
        '炒青菜': 'tshau-chin-tshe', '番茄炒蛋': 'fa-ze-tshau-de',
        '可乐': 'khu-loq', '雪碧': 'siq-piq', '果汁': 'ko-tsy',
        '牛奶': 'gnieu-naen', '咖啡': 'ka-fi', '茶': 'zo',
        
        // 常用动词短语
        '起床': 'chi-zaon', '睡觉': 'khun-ciau', '吃饭': 'chiq-ve',
        '喝水': 'heq-sy', '走路': 'tseu-lu', '坐车': 'zu-tsho',
        '上班': 'zaon-pe', '下班': 'gho-pe', '休息': 'xieu-siq',
        '学习': 'ghoq-zhiq', '工作': 'kon-tsoq', '打电话': 'tan-di-wo',
        '看书': 'khe-sy', '写字': 'xia-tsy', '买东西': 'ma-ton-sy',
        '卖东西': 'ma-ton-sy', '付钱': 'fu-dzi', '找钱': 'tsau-dzi',
        '生病': 'san-bin', '看病': 'khe-bin', '吃药': 'chiq-yaq',
        '锻炼身体': 'tse-li-deu-ghi', '洗澡': 'si-tsau', '刷牙': 'sau-ngaq',
        '洗脸': 'si-li', '化妆': 'hua-tsaon', '穿衣服': 'tshon-i-foq',
        '脱衣服': 'theq-i-foq', '做饭': 'tsu-ve', '烧菜': 'sau-tshe',
        '洗碗': 'si-woe', '打扫': 'tau-sau', '整理': 'tsen-li',
        '买东西': 'ma-ton-sy', '逛街': 'kuaon-ka', '旅游': 'ly-yeu',
        '拍照': 'phau-tsaq', '看电影': 'khe-di-yin', '听音乐': 'thin-yin-ghaq',
        '玩游戏': 'we-gniq-ghiu', '上网': 'zaon-maon', '发邮件': 'faq-ci-kyu'
    },

    // 苏州话拼音
    suzhou: {
        '我': 'ngu', '你': 'ne', '他': 'li', '她': 'li', '它': 'li',
        '的': 'keq', '是': 'zy', '了': 'leq', '在': 'ze', '有': 'yeu',
        '不': 'peq', '来': 'le', '去': 'chi', '上': 'zaon', '下': 'gho',
        '大': 'dou', '小': 'siau', '人': 'gnin', '好': 'hau', '家': 'ka',
        '国': 'koq', '学': 'ghoq', '生': 'san', '年': 'gni', '天': 'thi',
        '说': 'seq', '看': 'khe', '吃': 'chiq', '喝': 'heq', '走': 'tseu',
        '一': 'iq', '二': 'gni', '三': 'se', '四': 'sy', '五': 'ng',
        '六': 'loq', '七': 'chiq', '八': 'paq', '九': 'cieu', '十': 'zeq',
        '请': 'chin', '问': 'men', '早': 'tsau', '晚': 'we', '多': 'tu',
        '少': 'sau', '谢谢': 'zia-zia', '再见': 'tse-zi', '欢迎': 'hua-nen',
        '苏州': 'sou-tseu', '江南': 'cian-noe', '园林': 'yu-lin'
    },

    // 绍兴话拼音 (基于吴语协会方案)
    shaoxing: {
        '我': 'ngo', '你': 'non', '他': 'tha', '她': 'tha', '它': 'tha',
        '的': 'keh', '是': 'zy', '了': 'leh', '在': 'ze', '有': 'yeu',
        '不': 'peh', '来': 'le', '去': 'chi', '上': 'zaon', '下': 'gho',
        '大': 'du', '小': 'siau', '人': 'gnin', '好': 'hau', '家': 'ka',
        '国': 'koh', '学': 'ghoh', '生': 'san', '年': 'gni', '天': 'thi',
        '说': 'seh', '看': 'khe', '吃': 'chih', '喝': 'heh', '走': 'tseu',
        '一': 'ih', '二': 'gni', '三': 'se', '四': 'sy', '五': 'ng',
        '六': 'loh', '七': 'chih', '八': 'pah', '九': 'cieu', '十': 'zeh',
        '请': 'chin', '问': 'men', '早': 'tsau', '晚': 'we', '多': 'tu',
        '少': 'sau', '谢谢': 'xia-xia', '再见': 'tse-zi', '欢迎': 'hua-nen',
        '绍兴': 'sau-hin', '越剧': 'yiu-cioh', '黄酒': 'waon-cieu'
    }
};

// 导出字典
if (typeof module !== 'undefined' && module.exports) {
    module.exports = wugniuDict;
}
