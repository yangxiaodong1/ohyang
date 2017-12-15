from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser

from ohho.common.logic.common.device import Device
from ohho.common.logic.common.result import Result


class LogicTestGetUserByDevice(object):
    def __init__(self):
        self.device = Device()
        self.user = DBOHHOUser()

    def get(self, identity_list):
        data = list()
        relation_list = list()
        for identity in identity_list:
            self.device.set_identity(identity)
            relation = self.device.get_relation_by_device()
            if relation:
                temp = dict()
                temp["identity"] = identity
                temp["relation"] = relation
                relation_list.append(temp)

        for item in relation_list:
            temp = item
            relation = item["relation"]
            user = self.user.get_by_id(relation.user_id)
            if user:
                temp["username"] = user.username
                del temp["relation"]
                data.append(temp)
        if data:
            result = Result.get_result(True, 1, 1, "OK!")
        else:
            result = Result.get_result(False, -1, -1, "no data!")
        result["data"] = data
        return result
