from DB.common.operation import Operation
from IM.netease.models import OHHOIMUser


class DBOHHOIMUser(object):
    @staticmethod
    def get_none():
        return Operation.get_none()

    @staticmethod
    def add(data_dict):
        return Operation.add(OHHOIMUser, data_dict)

    @staticmethod
    def get_query():
        return Operation.get_query(OHHOIMUser)

    @staticmethod
    def get_by_account_id(account_id):
        query = DBOHHOIMUser.get_query()
        data = query.filter(OHHOIMUser.account_id == account_id)
        count = data.count()
        if count:
            return data[0]
        else:
            return DBOHHOIMUser.get_none()

    @staticmethod
    def update(obj, data_dict):
        return Operation.update(obj, data_dict)
