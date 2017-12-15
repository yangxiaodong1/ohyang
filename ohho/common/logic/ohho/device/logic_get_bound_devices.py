from ohho.common.logic.common.device import Device
from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.detail_constant import RELATION_NOT_EXIST


class LogicGetBoundDevices(object):
    def __init__(self):
        self.device = Device()

    def get(self, user_id):
        relations = self.device.get_valid_relation_by_user(user_id)
        result = Result.result_success()
        data = list()
        if relations:
            for relation in relations:
                temp = self.device.get_device_information(relation.device_id)
                if temp:
                    temp["type"] = relation.type
                    temp["name"] = relation.name
                    temp["is_lost"] = relation.is_lost
                    data.append(temp)
        if data:
            result["data"] = data
        return result
