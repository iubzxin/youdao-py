# -*- coding:utf-8 -*-

import hashlib
import random
import requests
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

__version__ = '0.0.1'

language = "zh-CHS"
language_array = ["zh-CHS", "en", "ja", "ko", "fr", "de", "ru", "es", "pt", "it", "vi", "id", "ar"]


def _md5(string): return (hashlib.md5(string)).hexdigest()


class YoudaoException(Exception):
    pass


class Youdao(object):
    """
    支持中文翻译以下语种以及其他语种翻译中文, 不支持其他语种互译
        zh-CHS: 中文
        en: 英语
        ja: 日语
        ko: 韩语
        fr: 法语
        de: 德语
        ru: 俄语
        es: 西班牙语
        pt: 葡萄牙语
        it: 意大利语
        vi: 越南语
        id: 印尼语
        ar: 阿拉伯语
    """
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    headers = {
        "Host": "fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
    }

    cookies = {"OUTFOX_SEARCH_USER_ID": "-1010247688@10.169.0.83"}

    def do_request(self, data):
        try:
            response = requests.post(self.url, data=data, headers=self.headers, cookies=self.cookies)
            result = response.json()
        except TypeError:
            raise YoudaoException("Invalid JSON.")
        except Exception, e:
            raise YoudaoException("Sending request failed:{0}".format(e))

        return result

    @staticmethod
    def _filter(_from, _to):
        if _from is None or _from not in language_array:
            _from = 'AUTO'
        if _to is None or _to not in language_array:
            _to = 'AUTO'
        if (_from != language and _from != 'AUTO') and (_to != language and _to != 'AUTO'):
            _from = 'AUTO'
            _to = 'AUTO'
        if _to == _from == language:
            _from = 'AUTO'
            _to = 'AUTO'

        return _from, _to

    def run(self, string, _form=None, _to=None):
        salt = str((int(time.time()) * 1000)) + str(random.randint(0, 9))
        _form, _to = self._filter(_form, _to)

        params = {
            "i": string,
            "from": _form,
            "to": _to,
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": _md5("fanyideskweb{0}{1}n%A-rKaT5fb[Gy?;N5@Tj".format(string, salt)),
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
        }

        result = self.do_request(data=params)
        if result['errorCode'] != 0:
            raise YoudaoException("Access denied")

        try:
            return result['translateResult'][0][0]['tgt']
        except TypeError:
            raise YoudaoException("Invalid format.")
        except Exception:
            raise YoudaoException("Unknown error.")
