from DB.mysql.models.ohho.test.model_test_rssi_distance import TestRssiDistance as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBTestRssiDistance(DBBase):
    def __init__(self):
        super(DBTestRssiDistance, self).__init__(model)
