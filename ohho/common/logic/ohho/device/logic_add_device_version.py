from ohho.common.logic.common.bluetooth import Bluetooth


class LogicAddDeviceVersion(object):
    def __init__(self):
        self.blue_tooth = Bluetooth()

    def add_device_version(self, version, name, url):
        result = self.blue_tooth.add_version(version, name, url)
        return result
