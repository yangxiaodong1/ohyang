from DB.common.operation import Operation

from ohho.common.db.ohho.relation.db_ohho_user_and_device_imei import DBOHHOUserAndDeviceIMEI
from ohho.common.db.ohho.device.db_ohho_device import DBOHHODevice
from ohho.common.logic.common.result import Result
from Tools.ohho_random import OHHORandom
from Tools.ohho_encryption import OHHOEncryption
from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_log import OHHOLog
from Tools.ohho_operation import OHHOOperation
from settings import TEST

AES_KEY = "95GPhWxiNJ1oktrR"


class IMEI(object):
    def __init__(self):
        self.imei = DBOHHOUserAndDeviceIMEI()
        self.encryption = OHHOEncryption(AES_KEY)

    def get_by_imei(self, imei):
        if imei:
            instance, information = self.imei.get_by_imei(imei)
            return instance
        else:
            return None

    def get_by_new_imei(self):
        random = OHHORandom.get_nonce(15)
        encryption_random = self.encryption.encrypt(random)
        instance, ex = self.imei.get_by_imei(random)
        return encryption_random, instance, ex, random

    def add_new_imei(self, imei):
        data = dict()
        data["imei"] = imei
        return self.imei.add(data)

    def update(self, instance, user_id, device_id):
        if instance and instance is not True:
            imei_by_device = self.imei.get_first_by_device_id(device_id)
            if not imei_by_device:
                data = dict()
                data["device_id"] = device_id
                data["user_id"] = user_id
                success = self.imei.update(instance, data)
                if success:
                    return Result.result_success()
                else:
                    return Result.result_failed()
            else:
                return Result.result_failed("device_id has been in imei!")

        else:
            return Result.result_parameters_are_invalid()

    def get_query(self):
        return self.imei.get_query()

    def get_by_user(self, query, user_id):
        return self.imei.get_by_user_id(query, user_id)

    def get_by_device_from_query(self, query, device_id):
        return self.imei.get_query_by_device_id(query, device_id)

    def get_by_device(self, device_id):
        query = self.imei.get_query()
        return self.imei.get_by_device_id(query, device_id)

    def delete_outdated(self):
        query = self.get_query()
        query = self.get_by_user(query, None)
        query = self.get_by_device_from_query(query, None)
        twenty_four_hours_before = OHHODatetime.several_hours_before_from_now()
        query = self.imei.get_less_than_created_at(query, twenty_four_hours_before)
        OHHOLog.print_log(self.imei.get_count(query))
        return self.delete_some(query)

    def delete_some(self, query):
        if query:
            OHHOLog.print_log("delete some")
            return Operation.delete_some(query)
        else:
            return None

    def get_by_user_and_device(self, user_id, device_id):
        query = self.get_query()
        query = self.get_by_user(query, user_id)
        query = self.get_by_device_from_query(query, device_id)
        return query

    def delete_by_user_and_device(self, user_id, device_id):
        query = self.get_by_user_and_device(user_id, device_id)
        OHHOLog.print_log(self.imei.get_count(query))
        return self.delete_some(query)

    def first(self, query):
        return Operation.first(query)

    def get_information(self, instance):
        result = dict()
        device = DBOHHODevice.get_by_id(instance.device_id)
        if device:
            result["identity_id"] = device.identity_id
            result["imei"] = instance.imei
        return result
