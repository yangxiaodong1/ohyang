from DB.mysql.models.ohho.meet.model_ohho_temp_meet_address import OHHOTempMeetAddress
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_encryption import OHHOEncryption
from Tools.ohho_operation import OHHOOperation


class DBOHHOTempMeetAddress(DBBase):
    def __init__(self, index=0):
        super(DBOHHOTempMeetAddress, self).__init__(OHHOTempMeetAddress, index)

    def get_by_apply(self, apply_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.apply_id, apply_id)
        return self.first(query)
