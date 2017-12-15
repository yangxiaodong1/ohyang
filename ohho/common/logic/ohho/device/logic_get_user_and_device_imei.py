from ohho.common.logic.common.result import Result
from ohho.common.logic.common.imei import IMEI
from Tools.ohho_log import OHHOLog


class LogicGetUserAndDeviceIMEI(object):
    def __init__(self):
        self.imei = IMEI()

    def get(self):
        self.imei.delete_outdated()
        while True:
            imei, instance, ex, random = self.imei.get_by_new_imei()
            if not instance:
                self.imei.add_new_imei(random)
                OHHOLog.print_log("add empty imei!")
                result = Result.result_success()
                result["data"] = random
                # result["imei"] = random
                return result
