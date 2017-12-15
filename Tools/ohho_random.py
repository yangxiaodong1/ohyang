import random

SAMPLE_STRING = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
NUMBER_STRING = '1234567890'


class OHHORandom(object):
    @staticmethod
    def get_nonce(length=32):
        return ''.join(random.sample(SAMPLE_STRING, length))

    @staticmethod
    def get_numbers(length):
        return ''.join(random.sample(NUMBER_STRING, length))

    @staticmethod
    def get_some_number(max_number):
        return int(random.random() * max_number)


if __name__ == "__main__":
    print(OHHORandom.get_nonce())
    print(OHHORandom.get_numbers(4))
    print(OHHORandom.get_nonce(16))
