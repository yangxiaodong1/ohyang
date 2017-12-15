from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog
from ohho.common.logic.common.code import Code
from ohho.common.logic.common.result import Result


class LogicCheckVerificationCode(object):
    @staticmethod
    def check_verification_code(cellphone_number, code):
        code_in_redis = Code.get_code(cellphone_number)
        if code_in_redis:
            code_in_redis_unicode = OHHOOperation.to_str(code_in_redis)
            OHHOLog.print_log(code_in_redis_unicode)
            OHHOLog.print_log(code)
            if code_in_redis_unicode == code:
                Code.delete_code(cellphone_number)
                result = Result.result_success()
            else:
                result = Result.result_failed()
        else:
            result = Result.result_not_exist()

        return result


if __name__ == "__main__":
    code = "6789"
    print(LogicCheckVerificationCode.check_verification_code("lileliang", code))
