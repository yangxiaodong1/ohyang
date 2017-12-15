from DB.mysql.models.model_test_device import TestDevice as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBTestDevice(DBBase):
    def __init__(self):
        super(DBTestDevice, self).__init__(model)
