from ohho.common.logic.common.cellphone import Cellphone
from ohho.common.logic.common.code import Code
from ohho.common.logic.common.user import User
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog


class LogicRebindCellphone(object):
    def __init__(self):
        self.user = User()
        self.cellphone = Cellphone()

    def rebind_cellphone(self, cellphone_key, cellphone_number, code, base_url, cellphone_dict, country_code):
        the_cellphone = country_code + cellphone_number
        check = Code.check_code(the_cellphone, code)
        if check:
            country_code_object = self.user.country_code.get_by_country_code(country_code)
            country_code_id = country_code_object.id if country_code_object else 0
            # self.user.get_by_country_code_and_cellphone(country_code, cellphone_number)
            # user = self.user.get(cellphone_number)
            user = self.user.get_by_country_code_and_cellphone(country_code_id, cellphone_number)
            self.cellphone.set_key(cellphone_key)
            cellphone = self.cellphone.get()
            if not cellphone:
                success = self.cellphone.add_cellphone(cellphone_dict)
                if success:
                    cellphone = self.cellphone.get()
                else:
                    cellphone = None
            if cellphone:
                if not user:
                    OHHOLog.print_log(country_code)
                    OHHOLog.print_log(cellphone_number)
                    result = Result.result_failed("user doest not exist")
                else:
                    result = self.cellphone.bind_cellphone(cellphone.id, user.id)
                    data = self.user.get_user_information(user.id, base_url)
                    result["data"] = data
            else:
                result = Result.result_failed("cellphone does not exist!")
        else:
            result = Result.result_failed("code is incorrect!")
        return result


if __name__ == "__main__":
    pass
