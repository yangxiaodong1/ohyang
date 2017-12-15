from sqlalchemy import desc
from Test.models import TestPhonePosition
from DB.common.operation import Operation
from Test.common.db.constant import TIMESTAMP_DIFF


class DBPhonePosition(object):
    @staticmethod
    def get_none():
        return Operation.get_none()

    @staticmethod
    def get_query():
        return Operation.get_query(TestPhonePosition)

    @staticmethod
    def get_query_list(query):
        return query.all()

    @staticmethod
    def get_query_first(query):
        return query.first()

    @staticmethod
    def add(obj_dict):
        return Operation.add(TestPhonePosition, obj_dict)

    @staticmethod
    def order_by_id_desc(objs):
        return objs.order_by(desc(TestPhonePosition.id))

    @staticmethod
    def order_by_timestamp_desc(objs):
        return objs.order_by(desc(TestPhonePosition.timestamp))

    @staticmethod
    def limit(objs, number):
        if objs:
            return objs[:number]
        else:
            return objs

    @staticmethod
    def get_by_name(name):
        query = DBPhonePosition.get_query()
        objs = query.filter(TestPhonePosition.name == name)
        objs = DBPhonePosition.order_by_id_desc(objs)
        return objs

    @staticmethod
    def get_by_timestamp(objs, timestamp):
        small_timestamp = timestamp - TIMESTAMP_DIFF
        big_timestamp = timestamp + TIMESTAMP_DIFF
        objs = objs.filter(TestPhonePosition.timestamp >= small_timestamp,
                           TestPhonePosition.timestamp <= big_timestamp)
        objs = DBPhonePosition.order_by_timestamp_desc(objs)
        return objs

    @staticmethod
    def get_info(obj):
        return Operation.get_instance_info(obj)
