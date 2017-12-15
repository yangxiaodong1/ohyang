from Tools.ohho_random import OHHORandom
from Tools.ohho_operation import OHHOOperation
from DB.redis.operation import RedisDB
from ohho.common.logic.common.constant import CODE
from ohho.common.logic.common.alidayu.alidayu_main import execute_python2
from settings import TEST


class Code(object):
    @staticmethod
    def get_code(username):
        return RedisDB.hash_get(username, CODE)

    @staticmethod
    def create_code(length=4):
        code = OHHORandom.get_numbers(length)
        while code.startswith('0'):
            code = OHHORandom.get_numbers(length)
        return code

    @staticmethod
    def save_code(username, code):
        RedisDB.hash_set(username, CODE, code)
        RedisDB.set_expire(username)

    @staticmethod
    def delete_code(username):
        RedisDB.hash_del(username, CODE)

    @staticmethod
    def send_code(cellphone_number, params):
        return execute_python2(cellphone_number, params)

    @staticmethod
    def check_code(username, code):
        if TEST:
            return True
        else:
            the_code = Code.get_code(username)
            if the_code:
                the_code_str = OHHOOperation.utf82unicode(the_code)
                if the_code_str == code:
                    Code.delete_code(username)
                    return True
            return False


if __name__ == "__main__":
    username = "lileliang"
    print("start")
    code = Code.create_code()
    print(code)
    # Code.save_code(username, code)
    # # bytes 转化为 str 用decode; 反之用encode
    # # code_from_redis = Code.get_code(username).decode("ascii")
    # code_from_redis = Code.get_code(username)
    # code_from_redis_unicode = OHHOOperation.utf82unicode(code_from_redis)
    # print(code_from_redis)
    # print(code == code_from_redis_unicode)
    #
    # # Code.delete_code(username)
    # # print(Code.get_code(username))
    # print("end")
