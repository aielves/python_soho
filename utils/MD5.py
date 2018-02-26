"""
@created by shadow on 2018.01.02
@resume MD5加密工具类实现
"""

# -*- coding: UTF-8 -*-

import hashlib


def encrypt(*args):
    # 创建md5对象
    md5 = hashlib.md5()
    text = args[0]
    if (args.__len__() >= 2):
        text += args[1]
    md5.update(text.encode(encoding='utf-8'))
    return str(md5.hexdigest()).lower()


if (__name__ == "__main__"):
    s = "test"
    print('MD5加密前为 ：' + s)
    print('MD5加密后为 ：' + encrypt(s))
    print('MD5加密后为 ：' + encrypt(s, "cP1of$@T"))
