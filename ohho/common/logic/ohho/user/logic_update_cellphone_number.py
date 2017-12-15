from ohho.common.logic.common.user import User
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.code import Code
from Tools.ohho_datetime import OHHODatetime
from ohho.common.db.ohho.base.db_ohho_country_code import DBOHHOCountryCode


class LogicUpdateCellphoneNumber(object):
    def __init__(self):
        self.user = User()
        self.country_code = DBOHHOCountryCode()

    def change(self, user_id, cellphone_number, code, country_code):
        country_code_obj = self.country_code.get_by_country_code(country_code)
        if country_code_obj:
            code_cellphone_number = country_code + cellphone_number
        else:
            return Result.result_failed("the country_code not exist")
        is_correct = Code.check_code(code_cellphone_number, code)
        if is_correct:
            the_user = self.user.get_by_id(user_id)
            if the_user:
                if self.user.user.exist_valid_cellphone_country_code_id(country_code_obj.id, cellphone_number):
                    return Result.result_failed("the cellphone number has been registered!")
                else:
                    last_cellphone = the_user.cellphone
                    cellphone = cellphone_number
                    data = dict()
                    data["last_cellphone"] = last_cellphone
                    data["cellphone"] = cellphone
                    data["country_code_id"] = country_code_obj.id
                    success = self.user.update_user(the_user, data)
                    if success:
                        return Result.result_success()
                    else:
                        return Result.result_failed()
            else:
                return Result.result_failed("the user %d does not exist" % (int(user_id)))
        else:
            return Result.result_failed("cellphone code is incorrect!")
