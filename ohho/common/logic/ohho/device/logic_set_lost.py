from ohho.common.logic.common.device import Device
from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.detail_constant import RELATION_NOT_EXIST


class LogicSetLost(object):
    def __init__(self):
        self.device = Device()

    def set_lost(self, user_id, identity_id):
        return self.device.set_lost(user_id, identity_id)
