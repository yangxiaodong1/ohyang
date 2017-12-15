from DB.mysql.models.ohho.record.model_ohho_record_match_label import OHHORecordMatchLabel
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBOHHORecordMatchLabel(DBBase):
    def __init__(self, index=0):
        super(DBOHHORecordMatchLabel, self).__init__(OHHORecordMatchLabel, index)

    def get_by_name(self, query, name):
        return Operation.filter(query, self.model.name, name)

    def get_by_parent_id(self, query, parent_id):
        return Operation.filter(query, self.model.parent_id, parent_id)
