from ohho.common.db.ohho.device.db_ohho_device import DBOHHODevice
from ohho.common.db.ohho.device.db_ohho_device_setting import DBOHHODeviceSetting
from ohho.common.db.ohho.device.db_ohho_device_version import DBOHHODeviceVersion
from ohho.common.db.ohho.device.db_ohho_device_sensor import DBOHHODeviceSensor

from ohho.common.logic.common.password import Password
from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.detail_constant import DEVICE_NOT_EXIST
from ohho.common.logic.ohho.detail_constant import DEVICE_SETTING_EXIST
from ohho.common.logic.ohho.detail_constant import DEVICE_SETTING_NOT_EXIST


class Bluetooth(object):
    def __init__(self):
        self.device = DBOHHODevice()
        self.setting = DBOHHODeviceSetting()
        self.version = DBOHHODeviceVersion()
        self.sensor = DBOHHODeviceSensor()

    def add_sensor(self, user_id, device_id, rssi, distance):
        data_dict = dict()
        data_dict["user_id"] = user_id
        data_dict["device_id"] = device_id
        data_dict["rssi"] = rssi
        data_dict["distance"] = distance

        return self.sensor.add(data_dict)

    def add_setting(self, identity_id, password, name, power, periods):
        self.device.set_identity(identity_id)
        device = self.device.get_by_identity()
        password_instance = Password(password)
        if device:
            instance = self.setting.get_by_device(device.id)
            if instance:
                result = Result.result_exist(DEVICE_SETTING_EXIST)
            else:
                data_dict = dict()
                data_dict["device_id"] = device.id
                data_dict["password"] = password_instance.aes_encryption()
                data_dict["name"] = name
                data_dict["power"] = power
                data_dict["periods"] = periods
                success = self.setting.add(data_dict)
                if success:
                    result = Result.result_success()
                else:
                    result = Result.result_failed()
        else:
            result = Result.result_not_exist(DEVICE_NOT_EXIST)
        return result

    def update_setting(self, identity_id, password, name, power):
        self.device.set_identity(identity_id)
        device = self.device.get_by_identity()
        if device:
            instance = self.setting.get_by_device(device.id)
            if instance:
                data_dict = dict()
                data_dict["password"] = Password.aes_encryption(password)
                data_dict["name"] = name
                data_dict["power"] = power
                success = self.setting.update(instance, data_dict)
                if success:
                    result = Result.result_success()
                else:
                    result = Result.result_failed()
            else:
                result = Result.result_not_exist(DEVICE_SETTING_NOT_EXIST)
        else:
            result = Result.result_not_exist(DEVICE_NOT_EXIST)

        return result

    def get_setting_information(self, identity_id):
        self.device.set_identity(identity_id)
        device = self.device.get_by_identity()
        data = dict()
        if device:
            instance = self.setting.get_by_device(device.id)
            if instance:
                data = self.setting.get_information(instance)
                data["source_password"] = Password.aes_decryption(data["password"])
                result = Result.result_success()
            else:
                result = Result.result_failed()
        else:
            result = Result.result_not_exist(DEVICE_NOT_EXIST)
        result["data"] = data
        return result

    def get_version_information(self):
        query = self.version.get_query()
        query = self.version.order_by_id_desc(query)
        version_object = self.version.first(query)
        data = dict()
        if version_object:
            data = self.version.get_information(version_object)
            result = Result.result_success()
        else:
            result = Result.result_failed()
        result["data"] = data
        return result

    def add_version(self, version, name, url):
        instance = self.version.get_by_version(version)
        if instance:
            return Result.result_failed("version exist!")
        data = dict()
        data["version"] = version
        data["name"] = name
        data["url"] = url
        success = self.version.add(data)
        if success:
            return Result.result_success()
        else:
            return Result.result_failed()
