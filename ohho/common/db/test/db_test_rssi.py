from DB.mysql.models.ohho.test.model_test_rssi import TestRssi as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBTestRssi(DBBase):
    def __init__(self):
        super(DBTestRssi, self).__init__(model)

    def get_by_phone(self, query, phone_list):
        return Operation.in_(query, self.model.phone, phone_list)
