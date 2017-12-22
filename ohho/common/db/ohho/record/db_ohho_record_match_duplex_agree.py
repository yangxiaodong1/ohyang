from DB.mysql.models.ohho.record.model_ohho_record_match_duplex_agree import OHHORecordMatchDuplexAgree as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBOHHORecordMatchDuplexAgree(DBBase):
    def __init__(self, index=0):
        super(DBOHHORecordMatchDuplexAgree, self).__init__(model, index)

    def get_by_apply(self, apply_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.apply_id, apply_id)
        query = self.order_by_id_desc(query)
        return self.first(query)
