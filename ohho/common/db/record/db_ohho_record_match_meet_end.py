from DB.mysql.models.ohho.record.model_ohho_record_match_meet_end import OHHORecordMatchMeetEnd as model
from ohho.common.logic.common.record.constant import *
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBOHHORecordMatchMeetEnd(DBBase):
    def __init__(self):
        super(DBOHHORecordMatchMeetEnd, self).__init__(model)

    def get_by_apply(self, apply_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.apply_id, apply_id)
        query = self.order_by_id_desc(query)
        return Operation.first(query)

    def get_by_apply_and_user(self, apply_id, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.apply_id, apply_id)
        query = Operation.filter(query, self.model.user_id, user_id)
        query = self.order_by_id_desc(query)
        return Operation.first(query)

    def add_meet_end_by_type(self, apply_id, type):
        data = dict()
        data["apply_id"] = apply_id
        data["type"] = type
        return self.add(data)

    def add_normal(self, apply_id):
        return self.add_meet_end_by_type(apply_id, MEET_END_TYPE_NORMAL)

    def add_apply_timeout(self, apply_id):
        return self.add_meet_end_by_type(apply_id, MEET_END_TYPE_APPLY_TIMEOUT)

    def add_agree_timeout(self, apply_id):
        return self.add_meet_end_by_type(apply_id, MEET_END_TYPE_AGREE_TIMEOUT)

    def add_refuse(self, apply_id):
        return self.add_meet_end_by_type(apply_id, MEET_END_TYPE_REFUSE)

    def add_cancel(self, apply_id):
        return self.add_meet_end_by_type(apply_id, MEET_END_TYPE_CANCEL)
