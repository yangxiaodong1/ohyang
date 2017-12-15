from ohho.common.logic.common.bluetooth import Bluetooth


class LogicAddDeviceSetting(object):
    def __init__(self):
        self.blue_tooth = Bluetooth()

    def add_device_setting(self, identity_id, password, name, power, periods):
        result = self.blue_tooth.add_setting(identity_id, password, name, power, periods)
        return result
