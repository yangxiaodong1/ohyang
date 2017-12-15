from DB.mysql.models.model_test_phone_position import TestPhonePosition as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBTestPhonePosition(DBBase):
    def __init__(self):
        super(DBTestPhonePosition, self).__init__(model)
