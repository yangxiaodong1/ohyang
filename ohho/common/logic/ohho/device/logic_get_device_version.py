from ohho.common.logic.common.bluetooth import Bluetooth


class LogicGetDeviceVersion(object):
    def __init__(self):
        self.blue_tooth = Bluetooth()

    def get_device_version(self):
        result = self.blue_tooth.get_version_information()
        return result
