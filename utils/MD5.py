import hashlib
from binascii import b2a_hex, a2b_hex

from Crypto.Cipher import AES


def md5(*args):
    # 创建md5对象
    md5 = hashlib.md5()
    text = args[0]
    if (args.__len__() >= 2):
        text += args[1]
    md5.update(text.encode(encoding='utf-8'))
    return str(md5.hexdigest()).lower()


# 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
def aes_in(text, key):
    cryptor = AES.new(key, AES.MODE_CBC, key)
    # 密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
    length = 16
    count = len(text)
    if (count % length != 0):
        add = length - (count % length)
    else:
        add = 0
        text = text + ('\0' * add)
        text = cryptor.encrypt(text)
        return b2a_hex(text)


def decrypt(self, text):
    cryptor = AES.new(self.key, self.mode, self.key)
    plain_text = cryptor.decrypt(a2b_hex(text))
    return plain_text.rstrip('\0')


if (__name__ == "__main__"):
    s = "test"
    print('MD5加密前为 ：' + s)
    print('MD5加密后为 ：' + md5(s))
    print('MD5加密后为 ：' + md5(s, "cP1of$@T"))
    print(aes_in("test", "nAjECibDL2vfTsoI"))
