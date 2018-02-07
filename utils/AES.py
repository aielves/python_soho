from Crypto.Cipher import AES

UTF8 = "UTF-8";

key = "N6(lWQGN#O+OQ5ev"


def pad_text(encrypted_text):
    while len(encrypted_text) % 16 != 0:
        encrypted_text += "\0"
    print(encrypted_text)
    return encrypted_text


# 加密秘钥需要长达16位字符，所以进行空格拼接
def pad_key(key):
    while len(key) % 16 != 0:
        key += "\0"
    print(key)
    return key


def decrypt(encrypted_text, encrypted_key):
    # 加密后hex字符串转成字节
    encrypted_text = bytes.fromhex(encrypted_text)
    # 密钥字符串转成字节并按16位补全
    encrypted_key = bytes(pad_key(encrypted_key), encoding=UTF8)
    aes = AES.new(encrypted_key, AES.MODE_ECB)
    encrypted_text = aes.decrypt(encrypted_text)
    encrypted_text = str(encrypted_text, encoding=UTF8).replace("\0", "")
    return encrypted_text


def encrypt(encrypted_text, encrypted_key):
    # 加密字符串转成字节并按16位补全
    encrypted_text = bytes(pad_text(encrypted_text), encoding=UTF8)
    # 密钥字符串转成字节并按16位补全
    encrypted_key = bytes(pad_key(encrypted_key), encoding=UTF8)
    aes = AES.new(encrypted_key, AES.MODE_ECB)
    encrypted_text = aes.encrypt(encrypted_text)
    # 加密后字节转成hex字符串
    encrypted_text = ''.join(["%02X" % x for x in encrypted_text]).strip().lower()
    return encrypted_text


if __name__ == "__main__":
    s = encrypt("123_hello world!", key)
    print(s)
    s = decrypt(s, key)
    print(s)
