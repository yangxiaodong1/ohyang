from sqlalchemy import desc
from Test.models import DeviceInformation
from DB.common.operation import Operation
from Test.common.db.constant import TIMESTAMP_DIFF


class DBDeviceInformation(object):
    @staticmethod
    def get_none():
        return Operation.get_none()

    @staticmethod
    def get_query():
        return Operation.get_query(DeviceInformation)

    @staticmethod
    def get_all():
        return DeviceInformation.objects.all()

    @staticmethod
    def add(obj_dict):
        return Operation.add(DeviceInformation, obj_dict)

    @staticmethod
    def order_by_timestamp_desc(objs):
        return objs.order_by(desc(DeviceInformation.timestamp))

    @staticmethod
    def get_by_name(name):
        objs = DBDeviceInformation.get_query()
        return DBDeviceInformation.get_by_name(objs, name)

    @staticmethod
    def get_by_phone_name(phone_name):
        objs = DBDeviceInformation.get_query()
        return DBDeviceInformation.get_by_phone_name(objs, phone_name)

    @staticmethod
    def get_by_name(objs, name):
        return objs.filter(DeviceInformation.name == name)

    @staticmethod
    def get_by_phone_name(objs, phone_name):
        return objs.filter(DeviceInformation.phone_name == phone_name)

    @staticmethod
    def get_by_timestamp(timestamp):
        objs = DBDeviceInformation.get_query()
        return DBDeviceInformation.get_by_timestamp(objs, timestamp)

    @staticmethod
    def get_by_timestamp(objs, timestamp):
        small_timestamp = timestamp - TIMESTAMP_DIFF
        big_timestamp = timestamp + TIMESTAMP_DIFF
        objs = objs.filter(DeviceInformation.timestamp >= small_timestamp,
                           DeviceInformation.timestamp <= big_timestamp)
        objs = DBDeviceInformation.order_by_timestamp_desc(objs)
        return objs

    @staticmethod
    def get_info(obj):
        return Operation.get_instance_info(obj)
