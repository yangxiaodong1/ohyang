from DB.mysql.models.ohho.test.model_test_interest_point import TestInterestPoint as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBTestInterestPoint(DBBase):
    def __init__(self):
        super(DBTestInterestPoint, self).__init__(model)
