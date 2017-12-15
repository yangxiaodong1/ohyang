import hashlib
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from Tools.ohho_operation import OHHOOperation


class OHHOEncryption(object):
    @staticmethod
    def sha1(bytes_or_str):
        unicode_string = OHHOOperation.to_bytes(bytes_or_str)
        return hashlib.sha1(unicode_string).hexdigest()

    def __init__(self, key):
        self.key = OHHOOperation.to_bytes(key)
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        # 加密文本必须是bytes(utf8或ascii)，而不能是unicode(str)
        text = OHHOOperation.to_bytes(text)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + (b'\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        # 以unicode存储文件信息
        return OHHOOperation.to_str(b2a_hex(self.ciphertext))

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        # 解密文本必须是必须是bytes(utf8或ascii)，而不能是unicode(str)
        utf8_text = OHHOOperation.to_bytes(text)
        plain_text = cryptor.decrypt(a2b_hex(utf8_text))
        return OHHOOperation.to_str(plain_text.rstrip(b'\0'))


if __name__ == '__main__':
    pc = OHHOEncryption(OHHOOperation.to_bytes('keyskeyskeyskeys'))  # 初始化密钥
    e = pc.encrypt("00000")
    print(len(e))
    d = pc.decrypt(e)
    print(d)

    from Tools.ohho_random import OHHORandom

    test = OHHORandom.get_nonce(15)
    test_password = OHHOEncryption(OHHOOperation.to_str("ztr7vnwg4jiaeqh8"))
    print(test_password.encrypt(test))
    b = "e332f36055acd3e0272ab1b5a58b14fb"
    print(len(b))
