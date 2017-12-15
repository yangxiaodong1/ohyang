from DB.mysql.models.ohho.record.model_ohho_record_match_duplex_agree import OHHORecordMatchDuplexAgree as model
from ohho.common.db.db_base import DBBase


class DBOHHORecordMatchDuplexAgree(DBBase):
    def __init__(self, index=0):
        super(DBOHHORecordMatchDuplexAgree, self).__init__(model, index)
