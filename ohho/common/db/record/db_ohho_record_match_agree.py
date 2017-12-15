from DB.mysql.models.ohho.record.model_ohho_record_match_agree import OHHORecordMatchAgree as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation
from Tools.ohho_datetime import OHHODatetime
from ohho.common.logic.common.record.constant import *


class DBOHHORecordMatchAgree(DBBase):
    def __init__(self):
        super(DBOHHORecordMatchAgree, self).__init__(model)

    def filter_by_apply(self, apply_id):
        query = self.get_query()
        return Operation.filter(query, self.model.apply_id, apply_id)

    def filter_by_user(self, query, user_id):
        return Operation.filter(query, self.model.user_id, user_id)

    def get_nearest(self, query):
        query = self.order_by_id_desc(query)
        return self.first(query)

    def get_nearest_agree(self, apply_id):
        query = self.filter_by_apply(apply_id)
        query = self.order_by_id_desc(query)
        return self.first(query)

    def find_by_apply(self, apply_id_list):
        query = self.get_query()
        return Operation.in_(query, self.model.apply_id, apply_id_list)

    def is_valid_instance(self, instance):
        if instance:
            timestamp = OHHODatetime.get_current_timestamp()
            if instance.timestamp + VALID_INTERVAL_MILLISECOND < timestamp:
                return False
            return True
        else:
            return False
