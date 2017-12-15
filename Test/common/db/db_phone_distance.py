from Test.models import PhoneDistance
from DB.common.operation import Operation


class DBPhoneDistance(object):
    @staticmethod
    def get_none():
        return Operation.get_none()

    @staticmethod
    def get_query():
        return Operation.get_query(PhoneDistance)

    @staticmethod
    def add(obj_dict):
        return Operation.add(PhoneDistance, obj_dict)

    @staticmethod
    def get_info(obj):
        return Operation.get_instance_info(obj)
