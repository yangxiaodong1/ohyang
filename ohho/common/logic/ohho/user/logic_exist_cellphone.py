import os

from Tools.ohho_datetime import OHHODatetime
from ohho.common.logic.common.result import Result
from ohho.common.db.ohho.base.db_ohho_country_code import DBOHHOCountryCode
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.logic.common.im.netease.update_user_info import UpdateUserInfo
from Tools.ohho_log import OHHOLog


class LogicExistCellphone(object):
    def __init__(self):
        self.country_code = DBOHHOCountryCode()
        self.user = DBOHHOUser()

    def exist(self, country_code, cellphone):
        OHHOLog.print_log(country_code)
        OHHOLog.print_log(cellphone)
        country_code_object = self.country_code.get_by_country_code(country_code)
        if country_code_object:
            success = self.user.get_by_country_code_and_cellphone(country_code_object.id, cellphone)
            if success:
                return Result.result_success()
            else:
                return Result.result_failed("no such cellphone")
        else:
            return Result.result_failed("country code is invalid")
