from ohho.common.logic.common.bluetooth import Bluetooth


class LogicGetDeviceSetting(object):
    def __init__(self):
        self.blue_tooth = Bluetooth()

    def get_device_setting(self, identity_id):
        result = self.blue_tooth.get_setting_information(identity_id)
        return result
