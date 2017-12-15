from ohho.common.logic.common.device import Device
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog
from ohho.common.logic.ohho.detail_constant import RELATION_NOT_EXIST


class LogicSetDeviceUse(object):
    def __init__(self):
        self.device = Device()

    def set_device_use(self, user_id, identity_id, data_dict):
        user_id = int(user_id)
        # OHHOLog.print_log(user_id)
        # OHHOLog.print_log(identity_id)
        # OHHOLog.print_log(data_dict)
        self.device.set_identity(identity_id)
        relation = self.device.get_relation_by_device()
        # OHHOLog.print_log(relation.user_id)
        if relation and relation.user_id == user_id:
            type = data_dict.get("type", 0)
            type = int(type)
            OHHOLog.print_log(type)
            if type == 1:
                primary = self.device.get_primary_relation_by_user(user_id)
                if primary:
                    for p in primary:
                        OHHOLog.print_log("reset")
                        result = self.device.relation_update(p, {"type": 0})
                        OHHOLog.print_log(result)
            success = self.device.relation_update(relation, data_dict)
            if success:
                return Result.result_success()
            else:
                return Result.result_failed()
        elif relation:
            return Result.result_device_used_by_other()
        else:
            return Result.result_failed("this is not your device!")
