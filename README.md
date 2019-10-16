# youdao-py 基于有道翻译web python版SDK

###  安装
```
git clone https://github.com/iubzxin/youdao-py
python setup.py install
```
### 使用
```
>>> from youdao import Youdao
>>> yd = Youdao()
>>> yd.run(u'你好, 世界')
u'Hello world'
>>> yd.run(u'你好, 世界', _to='fr')
u'Bonjour monde'
>>> print yd.run(u'Hello world', _form='en')
你好，世界
```

### 语种代码对应表
语种 | 语种代码
---|---
中文|zh-CHS
英语|en
日语|ja
韩语|ko
法语|fr
德语|de
俄语|ru
西班牙语|es
葡萄牙语|pt
意大利语|it
越南语|vi
印尼语|id
阿拉伯语|ar

### 语种互译表
原文 | 译文
---|---
中文|英语
中文|日语
中文|韩语
中文|法语
中文|德语
中文|俄语
中文|西班牙语
中文|葡萄牙语
中文|意大利语
中文|越南语
中文|印尼语
中文|阿拉伯语
英语|中文
日语|中文
韩语|中文
法语|中文
德语|中文
俄语|中文
西班牙语|中文
葡萄牙语|中文
意大利语|中文
越南语|中文
印尼语|中文
阿拉伯语|中文
