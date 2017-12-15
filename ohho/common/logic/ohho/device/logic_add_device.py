from ohho.common.db.ohho.device.db_ohho_device import DBOHHODevice
from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.detail_constant import DEVICE_EXIST


class LogicAddDevice(object):
    def __init__(self):
        self.device = DBOHHODevice()

    def add_device(self, application_id, identity_id, mac_address, tx_power):

        data_dict = dict()
        data_dict["application_id"] = application_id
        data_dict["identity_id"] = identity_id
        data_dict["mac_address"] = mac_address
        data_dict["tx_power"] = tx_power

        self.device.set_identity(identity_id)
        device = self.device.get_by_identity()
        if not device:
            add = self.device.add(data_dict)
            if add:
                result = Result.result_success()
                device = self.device.get_by_identity()
                result["device_id"] = device.id
            else:
                result = Result.result_failed()
        else:
            result = Result.result_exist(DEVICE_EXIST)
            result["device_id"] = device.id
        return result
