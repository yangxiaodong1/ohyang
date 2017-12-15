from DB.mysql.models.ohho.meet.model_ohho_topic import OHHOTopic
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_encryption import OHHOEncryption
from Tools.ohho_operation import OHHOOperation


class DBOHHOTopic(DBBase):
    def __init__(self, index=0):
        super(DBOHHOTopic, self).__init__(OHHOTopic, index)
