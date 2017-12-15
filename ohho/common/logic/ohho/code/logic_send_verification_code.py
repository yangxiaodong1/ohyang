from ohho.common.logic.common.code import Code
from ohho.common.logic.common.result import Result


class LogicSendVerificationCode(object):
    @staticmethod
    def send_verification_code(cellphone_number):
        code = Code.create_code(length=4)
        Code.save_code(cellphone_number, code)
        params = "{'code':'%s'}" % (str(code))
        return_data = Code.send_code(cellphone_number, params)
        if return_data:
            if return_data['Code'] == 'OK':
                result = Result.result_success()
            else:
                result = Result.result_failed(return_data["Code"])
        else:
            result = Result.result_failed("send verification code failed!")
        return result


if __name__ == "__main__":
    phone = "13161916437"
    print(LogicSendVerificationCode.send_verification_code(phone))
