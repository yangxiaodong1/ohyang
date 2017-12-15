from Test.common.db.db_phone_position import DBPhonePosition
from Tools.ohho_log import OHHOLog


class LogicPhonePosition(object):
    @staticmethod
    def add(kwargs):
        result = dict()
        result["success"] = False
        if kwargs:
            obj = DBPhonePosition.add(kwargs)
            OHHOLog.print_log(obj)
        else:
            obj = DBPhonePosition.get_none()
        if obj:
            result["success"] = True
        return result

    @staticmethod
    def get_latest_position(name):
        objs = DBPhonePosition.get_by_name(name)
        return DBPhonePosition.get_query_first(objs)

    @staticmethod
    def get_another_nearest_position(obj, name):
        objs = DBPhonePosition.get_by_name(name)
        objs = DBPhonePosition.get_by_timestamp(objs, obj.timestamp)
        return DBPhonePosition.get_query_first(objs)

    @staticmethod
    def get_phones_inforamtion(name1, name2):
        result = dict()
        result["longitude1"] = 0
        result["latitude1"] = 0
        result["longitude2"] = 0
        result["latitude2"] = 0
        phone1 = LogicPhonePosition.get_latest_position(name1)
        if phone1:
            result["longitude1"] = phone1.longitude
            result["latitude1"] = phone1.latitude
            phone2 = LogicPhonePosition.get_another_nearest_position(phone1, name2)
            if phone2:
                result["longitude2"] = phone2.longitude
                result["latitude2"] = phone2.latitude
        return result
