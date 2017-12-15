from Tools.ohho_operation import OHHOOperation
from Test.common.db.db_phone_distance import DBPhoneDistance
from Test.common.logic.logic_phone_position import LogicPhonePosition


class LogicPhoneDistance(object):
    @staticmethod
    def add(kwargs):
        result = dict()
        result["success"] = False
        if kwargs:
            obj = DBPhoneDistance.add(kwargs)
        else:
            obj = DBPhoneDistance.get_none()
        if obj:
            result["success"] = True
        return result

    @staticmethod
    def add_by_names(name1, name2):
        data = dict()
        data["phone_one"] = 0
        data["phone_another"] = 0
        data["timestamp"] = 0
        data["distance"] = 0
        phone1 = LogicPhonePosition.get_latest_position(name1)
        if phone1:
            phone2 = LogicPhonePosition.get_another_nearest_position(phone1, name2)
            if phone2:
                data["phone_one"] = phone1.id
                data["phone_another"] = phone2.id
                data["timestamp"] = phone1.timestamp
                data["distance"] = OHHOOperation.calc_distance(
                    phone1.latitude, phone1.longitude,
                    phone2.latitude, phone2.longitude) * 1000
                data["unit"] = "m"
                data["input_distance"] = phone1.input_distance if phone1.input_distance else phone2.input_distance
                DBPhoneDistance.add(data)
                del data["created_at"]
                del data["changed_at"]
        return data
