from ohho.common.logic.common.device import Device
from ohho.common.logic.common.code import Code
from ohho.common.logic.common.user import User
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.imei import IMEI
from ohho.common.logic.ohho.detail_constant import PASSWORD_IS_INCORRECT
from ohho.common.logic.ohho.detail_constant import USER_NOT_EXIST
from Tools.ohho_log import OHHOLog


class LogicCellphoneUnbindDevice(object):
    def __init__(self):
        self.user = User()
        self.device = Device()
        self.imei = IMEI()

    def unbind_device(self, cellphone, code, identity, mac_address, country_code):
        # OHHOLog.print_log(cellphone)
        # OHHOLog.print_log(identity)
        # OHHOLog.print_log(mac_address)
        if country_code and cellphone:
            the_cellphone = country_code + cellphone
        else:
            return Result.result_parameters_are_invalid("country_code or cellphone is empty!")
        success = Code.check_code(the_cellphone, code)
        if success:
            country_code_object = self.user.get_country_code(country_code)
            country_code_id = country_code_object.id if country_code_object else 0
            user = self.user.get_by_country_code_and_cellphone(country_code_id, cellphone)
            if user:
                self.device.set_mac_address(mac_address)
                self.device.set_identity(identity)
                device = self.device.get_by_identity()
                if device:
                    # OHHOLog.print_log("before delete imei")
                    self.imei.delete_by_user_and_device(user.id, device.id)
                    # OHHOLog.print_log("after delete imei")
                    # query = self.imei.get_by_user_and_device(user.id, device.id)
                    # self.imei.delete_some(query)
                return self.device.unbind_device(user.id)
            else:
                return Result.result_not_exist(USER_NOT_EXIST)
        else:
            return Result.result_failed(PASSWORD_IS_INCORRECT)


if __name__ == "__main__":
    pass
