from ohho.common.logic.common.device import Device
from ohho.common.logic.common.imei import IMEI


class LogicUnbindDevice(object):
    def __init__(self):
        self.device = Device()
        self.imei = IMEI()

    def unbind_device(self, user_id, identity, mac_address):
        self.device.set_identity(identity)
        self.device.set_mac_address(mac_address)
        device = self.device.get_by_identity()
        if device:
            self.imei.delete_by_user_and_device(user_id, device.id)
            # query = self.imei.get_by_user_and_device(user_id, device.id)
            # self.imei.delete_some(query)
        return self.device.unbind_device(user_id)


if __name__ == "__main__":
    pass
