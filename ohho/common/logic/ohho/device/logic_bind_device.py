from ohho.common.logic.common.device import Device
from ohho.common.logic.common.imei import IMEI
from ohho.common.logic.common.user import User
from Tools.ohho_log import OHHOLog


class LogicBindDevice(object):
    def __init__(self):
        self.device = Device()
        self.imei = IMEI()
        self.user = User()

    def bind_device(self, user_id, identity, mac_address, imei=None):
        primary_device = self.user.get_primary_device_by_user(int(user_id))
        if primary_device:
            type = 0
        else:
            type = 1

        self.device.set_identity(identity)
        self.device.set_mac_address(mac_address)
        device = self.device.get_by_identity()
        if device:
            imei_instance = self.imei.get_by_imei(imei)
            result = self.imei.update(imei_instance, user_id, device.id)
            # OHHOLog.print_log(imei_instance)
            # OHHOLog.print_log(user_id)
            # OHHOLog.print_log(device.id)
            # OHHOLog.print_log("update user and device imei")

        return self.device.bind_device(user_id, type)


if __name__ == "__main__":
    pass
