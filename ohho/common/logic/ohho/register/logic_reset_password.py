from ohho.common.logic.common.code import Code
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.cellphone import Cellphone
from Tools.ohho_log import OHHOLog
from ohho.common.db.ohho.base.db_ohho_country_code import DBOHHOCountryCode


# from ohho.common.db.ohho.db_cellphone import Cellphone


class LogicResetPassword(object):
    def __init__(self):
        self.user = User()
        self.country_code = DBOHHOCountryCode()
        self.cellphone = Cellphone()

    def reset_password(self, cellphone_number, password, code, country_code, cellphone_dict=dict(), base_url=None):
        country_code_obj = self.user.get_country_code(country_code)
        if country_code_obj:
            user = self.user.user.get_by_country_code_and_cellphone(country_code_obj.id, cellphone_number)
            if user:
                cellphone_number_check = country_code + cellphone_number
                if self.user.check_threemonth_isvalid(user):
                    if Code.check_code(cellphone_number_check, code):
                        result = self.user.reset_password(cellphone_number, password, country_code)
                        if Result.is_success(result):
                            if not self.bind_cellphone(cellphone_dict, user.id):
                                return Result.result_failed("bind cellphone failed")
                            self.user.set_username(user.username)
                            if not Result.is_success(self.user.add_token()):
                                result = Result.result_failed("login failed!")
                            else:
                                information = self.user.get_user_information(user.id, base_url)
                                result["data"] = information
                        else:
                            result = Result.result_failed("change password failed!")
                    else:
                        result = Result.result_failed("verification code is incorrect!")
                else:
                    result = Result.result_update_beyond_three_month()
            else:
                result = Result.result_failed("user not exist!")
        else:
            result = Result.result_failed("country_code not exist")

        return result

    def bind_cellphone(self, cellphone_dict, user_id):
        OHHOLog.print_log(cellphone_dict)
        OHHOLog.print_log(user_id)
        if cellphone_dict and cellphone_dict.get("key", ""):
            key = cellphone_dict.get("key")
            OHHOLog.print_log(key)
            self.cellphone.set_key(key)
            cellphone_object = self.cellphone.get()
            if not cellphone_object:
                OHHOLog.print_log("no cellphone object")
                self.cellphone.add_cellphone(cellphone_dict)
                cellphone_object = self.cellphone.get()

            if cellphone_object:
                OHHOLog.print_log("no cellphone object at all")
                if not self.cellphone.is_bound_by_user(cellphone_object.id, user_id):
                    OHHOLog.print_log("begin to bind user")
                    success = self.cellphone.bind_cellphone(cellphone_object.id, user_id)
                    OHHOLog.print_log(success)
                    return Result.is_success(success)
                else:
                    return True
            else:
                return False
        else:
            return True
