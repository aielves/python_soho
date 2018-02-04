from Crypto.Cipher import AES

key = b'abcdefgh'

def pad(text):
    while len(text) % 16 != 0:
        text += b' '
    print(text)
    return text


# 加密秘钥需要长达16位字符，所以进行空格拼接
def pad_key(key):
    while len(key) % 16 != 0:
        key += b' '
    print(key)
    return key


aes = AES.new(pad_key(key), AES.MODE_ECB)
text = b'woshijiamineirong'
encrypted_text = aes.encrypt(pad(text))
print(encrypted_text)
encrypted_text = str(aes.decrypt(encrypted_text))
print(encrypted_text)
