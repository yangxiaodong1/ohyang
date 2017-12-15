from ohho.common.logic.common.bluetooth import Bluetooth
from ohho.common.logic.common.result import Result


class LogicUpdateDeviceSetting(object):
    def __init__(self):
        self.blue_tooth = Bluetooth()

    def update_device_setting(self, identity_id, password, name, power):
        result = self.blue_tooth.update_setting(identity_id, password, name, power)
        return result
