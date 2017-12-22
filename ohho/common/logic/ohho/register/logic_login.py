from ohho.common.logic.common.user import User
from ohho.common.logic.common.imei import IMEI
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.cellphone import Cellphone
from Tools.ohho_log import OHHOLog


class LogicLogin(object):
    def __init__(self):
        self.user = User()
        self.cellphone = Cellphone()
        self.imei = IMEI()

    def authenticate(self, country_code, username, password, cellphone_dict, base_url, code):
        country_code_object = self.user.get_country_code(country_code)
        country_code_id = country_code_object.id if country_code_object else 0

        OHHOLog.print_log("check user")
        is_code_login = False
        if username and code:
            is_code_login = True
            user_check_result = self.user.check_user_only_by_user(username, code, country_code_id)
        else:
            user_check_result = self.user.check_user(username, password, country_code_id)
        OHHOLog.print_log(user_check_result)

        user = self.user.get_by_cellphone(username)
        cellphone_key = cellphone_dict.get("key", None)
        self.cellphone.set_key(cellphone_key)
        cellphone = self.cellphone.get()

        OHHOLog.print_log("check user and cellphone relation")

        cellphone_relation_result = Result.result_failed()
        code_cellphone_relation_result = Result.result_failed()

        if user and cellphone:
            is_bind = self.cellphone.is_bound_by_user(cellphone.id, user.id)
            if is_code_login:
                success = self.cellphone.bind_cellphone(cellphone.id, user.id)
                if not Result.is_success(success):
                    code_cellphone_relation_result = Result.result_failed("rebind cellphone failed!")
                else:
                    code_cellphone_relation_result = Result.result_success()
            else:
                if is_bind:
                    cellphone_relation_result = Result.result_success()
                else:
                    OHHOLog.print_log("user id:")
                    OHHOLog.print_log(user.id)
                    OHHOLog.print_log("cellphone id:")
                    OHHOLog.print_log(cellphone.id)
                    OHHOLog.print_log("unsafe cellphone!")
                    cellphone_relation_result = Result.result_failed()
        else:
            OHHOLog.print_log("user or cellphone not exist!")
            cellphone_relation_result = Result.result_failed()

            if not cellphone:
                OHHOLog.print_log("add cellphone!")
                add_cellphone_result = self.cellphone.add_cellphone(cellphone_dict)
                OHHOLog.print_log(add_cellphone_result)
        OHHOLog.print_log(cellphone_relation_result)

        if not is_code_login:
            if Result.is_success(user_check_result) and Result.is_success(cellphone_relation_result):
                result = Result.result_success()
            elif Result.is_password_incorrect(user_check_result) or Result.is_update_beyond_three_month(
                    user_check_result):
                result = user_check_result
            elif Result.is_success(user_check_result):
                result = Result.result_unsafe()
            elif Result.is_not_exist(user_check_result):
                result = Result.result_not_exist()
            else:
                result = Result.result_failed()
        else:
            if Result.is_success(user_check_result) and Result.is_success(code_cellphone_relation_result):
                result = Result.result_success()
            elif Result.is_update_beyond_three_month(user_check_result):
                result = user_check_result
            elif Result.is_not_exist(user_check_result):
                result = Result.result_not_exist()
            else:
                result = Result.result_failed()

        if user and Result.is_success(result):
            result["data"] = self.user.get_user_information(user.id, base_url)

        return result


if __name__ == "__main__":
    username = "zhangyunfei"
    password = "111111"
    print(LogicLogin.authenticate(username, password))
