from DB.mysql.models.model_test_timestamp import TestTimestamp as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBTestTimestamp(DBBase):
    def __init__(self):
        super(DBTestTimestamp, self).__init__(model)
