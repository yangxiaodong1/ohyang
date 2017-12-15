from Tools.ohho_encryption import OHHOEncryption
from Tools.ohho_operation import OHHOOperation

AES_KEY = "ztr7vnwg4jiaeqh8"


class Password(object):
    def __init__(self, password=None):
        self.password = password

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def encryption(self):
        # unicode_string = OHHOOperation.to_str(self.password)
        return OHHOEncryption.sha1(self.password)

    def aes_encryption(self):
        pc = OHHOEncryption(AES_KEY)
        return pc.encrypt(self.password)

    def aes_decryption(self):
        pc = OHHOEncryption(AES_KEY)
        return pc.decrypt(self.password)


if __name__ == "__main__":
    from Tools.ohho_random import OHHORandom

    test = OHHORandom.get_nonce(15)
    test_password = Password(test)
    print(test_password.aes_encryption())
