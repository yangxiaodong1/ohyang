from ohho.common.logic.common.device import Device


class LogicIsDeviceValid(object):
    def __init__(self):
        self.device = Device()

    def is_device_valid(self, identity_id, mac_address):
        self.device.set_identity(identity_id)
        self.device.set_mac_address(mac_address)
        result = self.device.is_device_valid()
        return result
