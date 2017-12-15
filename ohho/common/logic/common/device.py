from ohho.common.db.ohho.device.db_ohho_device import DBOHHODevice
from ohho.common.db.ohho.base.db_ohho_country_code import DBOHHOCountryCode
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.db.ohho.relation.db_ohho_user_and_device_relation import DBOHHOUserAndDeviceRelation
from ohho.common.db.ohho.relation.db_ohho_user_and_device_imei import DBOHHOUserAndDeviceIMEI

from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.detail_constant import *
from Tools.ohho_log import OHHOLog


class Device(object):
    def __init__(self, identity_id=None, mac_address=None):
        self.device = DBOHHODevice(identity_id, mac_address)
        self.relation = DBOHHOUserAndDeviceRelation()
        self.imei = DBOHHOUserAndDeviceIMEI()
        self.user = DBOHHOUser()
        self.countryCode = DBOHHOCountryCode()

    def set_identity(self, identity_id):
        self.device.set_identity(identity_id)

    def get_identity(self):
        return self.device.identity_id

    def set_mac_address(self, mac_address):
        self.device.set_mac_address(mac_address)

    def get_mac_address(self):
        return self.device.mac_address

    def get_by_identity(self):
        return self.device.get_by_identity()

    def bind_device(self, user_id, type=1):
        try:
            OHHOLog.print_log("bind device start")
            device = self.get_by_identity()
            if device and self.device.check_by_mac():
                relation = self.relation.get_by_device(device.id)
                if relation and self.relation.is_valid(relation, True):
                    if relation.user_id == int(user_id):
                        result = Result.result_exist(RELATION_EXIST)
                    else:
                        user = self.user.get_by_id(relation.user_id)
                        cellphone = user.cellphone
                        country_code_id = user.country_code_id
                        country_code_obj = self.countryCode.get_by_id(country_code_id)
                        if country_code_obj:
                            country_code = country_code_obj.country_code
                        else:
                            country_code = "+86"
                        result = Result.result_device_used_by_other()
                        result["country_code"] = country_code
                        result["cellphone_number"] = cellphone
                else:
                    success = self.relation.add_without_commit(
                        {"device_id": device.id, "user_id": user_id, "type": type})
                    if success:
                        self.relation.commit()
                        result = Result.result_success()
                    else:
                        self.relation.rollback()
                        result = Result.result_failed()
            else:
                result = Result.result_not_exist()
            OHHOLog.print_log("bind device end")
            return result
        except Exception as ex:
            OHHOLog.print_log(ex)
            return Result.result_failed(ex)

    def unbind_device(self, user_id):
        device = self.device.get_by_identity()
        if device and self.device.check_by_mac():
            OHHOLog.print_log(device.id)
            relation = self.relation.get_by_device(device.id)
            if not relation:
                return Result.result_success(RELATION_NOT_EXIST)
            elif relation.user_id == int(user_id):
                if not self.relation.is_valid(relation, True):
                    return Result.result_success(RELATION_EXIST)
                else:
                    success = self.relation.delete(relation)
                    if success:
                        return Result.result_success()
                    else:
                        return Result.result_failed()
            else:
                return Result.result_failed(USED_BY_OTHER)
        else:
            return Result.result_failed(INVALID_DEVICE)

    def is_device_valid(self):
        device = self.device.get_by_identity()
        # OHHOLog.print_log(self.device.get_identity())
        # OHHOLog.print_log(device)
        if device and self.device.check_by_mac():
            relation = self.relation.get_by_device(device.id)
            if relation and self.relation.is_valid(relation, True):
                result = Result.result_device_used_by_other()
                user = DBOHHOUser()
                user_instance = user.get_by_id(relation.user_id)
                if user_instance:
                    result["cellphone_number"] = user_instance.cellphone
                    code = DBOHHOCountryCode.get_by_id(user_instance.country_code_id)
                    if code:
                        result["country_code"] = code.country_code
                    else:
                        result["country_code"] = "+86"
                return result
            else:
                return Result.result_success()
        else:
            return Result.result_failed(INVALID_DEVICE)

    def get_relation_by_device(self):
        device = self.device.get_by_identity()
        if device:
            relation = self.relation.get_by_device(device.id)
            if self.relation.is_valid(relation, True):
                return relation
            else:
                return None
        return None

    def get_primary_relation_by_user(self, user_id):
        query = self.relation.get_query()
        query = self.relation.get_valid(query)
        relations = self.relation.get_by_user(query, user_id)
        relations = self.relation.get_primary(relations)
        return relations

    def relation_update(self, instance, data_dict):
        return self.relation.update(instance, data_dict)

    def get_all_device(self):
        return self.device.get_query()

    def find_by_identity(self, query):
        return self.device.find_by_identity(query)

    def find_by_mac_address(self, query):
        return self.device.find_by_mac_address(query)

    def get_some_devices(self, query, offset, limit):
        return self.device.get_some(query, offset, limit)

    def get_by_id(self, device_id):
        return self.device.get_by_id(device_id)

    def update(self, instance, data):
        return self.device.update(instance, data)

    def add(self, data):
        return self.device.add(data)

    def delete(self, instance):
        return self.device.delete(instance)

    def is_empty(self, query):
        count = query.count()
        if count > 0:
            return False
        return True

    def set_lost(self, user_id, identity_id):
        self.device.set_identity(identity_id)
        device = self.device.get_by_identity()
        if device:
            query = self.relation.get_valid_by_device(device.id)
            if query:
                query = self.relation.get_by_user(query, user_id)
                query = self.relation.get_not_lost(query)
                OHHOLog.print_log(query.count())
            if query:
                success = self.relation.set_lost(query)
                if success:
                    return Result.result_success()
                else:
                    return Result.result_failed()
            else:
                return Result.result_failed("this device is not yours!")
        else:
            return Result.result_failed("this device is invalid")

    def cancel_lost(self, user_id, identity_id):
        self.device.set_identity(identity_id)
        device = self.device.get_by_identity()
        if device:
            query = self.relation.get_valid_by_device(device.id)
            if query:
                query = self.relation.get_by_user(query, user_id)
                OHHOLog.print_log(query.count())
                # query = self.relation.get_valid(query)
                # OHHOLog.print_log(query.count())
                query = self.relation.get_lost(query)
                OHHOLog.print_log(query.count())
            if query:
                success = self.relation.cancel_lost(query)
                if success:
                    return Result.result_success()
                else:
                    return Result.result_failed()
            else:
                return Result.result_failed("this device is not yours!")
        else:
            return Result.result_failed("this device is invalid")

    def get_valid_relation_by_user(self, user_id):
        query = self.relation.get_query()
        query = self.relation.get_valid(query)
        query = self.relation.get_by_user(query, user_id)
        return query

    def get_device_information(self, device_id):
        device = self.device.get_by_id(device_id)
        result = self.device.get_information(device)
        imei = self.get_imei_by_deivce(device_id)
        if imei:
            result["imei"] = imei.imei
        else:
            result["imei"] = ""
        return result

    def get_imei_by_deivce(self, device_id):
        query = self.imei.get_query()
        instance = self.imei.get_by_device_id(query, device_id)
        # query = self.imei.order_by_id_desc(query)
        # instance = self.imei.first(query)
        return instance
