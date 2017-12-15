from DB.mysql.models.ohho.record.model_ohho_record_match_meeting import OHHORecordMatchMeeting as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBOHHORecordMatchMeeting(DBBase):
    def __init__(self):
        super(DBOHHORecordMatchMeeting, self).__init__(model)

    def get_by_apply(self, apply_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.apply_id, apply_id)
        query = self.order_by_id_desc(query)
        return Operation.first(query)

    def filter_by_apply(self, query, apply_id):
        return Operation.filter(query, self.model.apply_id, apply_id)

    def filter_by_user(self, query, user_id):
        return Operation.filter(query, self.model.user_id, user_id)

    def get_valid_by_apply_and_user(self, apply_id, user_id):
        query = self.get_query()
        query = self.get_valid(query, True)
        query = self.filter_by_apply(query, apply_id)
        query = self.filter_by_user(query, user_id)
        query = self.order_by_id_desc(query)
        return self.first(query)

    def get_meeting_by_apply_and_user(self, apply_id, user_id):
        query = self.get_query()
        query = self.filter_by_apply(query, apply_id)
        query = self.filter_by_user(query, user_id)
        query = self.order_by_id_desc(query)
        return self.first(query)

    def get_apply_id_list_by_user(self, query, user_id):
        query = Operation.filter(query, self.model.user_id, user_id)
        apply_id_list = [meeting.apply_id for meeting in query]
        return apply_id_list

    def find_by_apply(self, apply_id_list):
        query = self.get_query()
        query = Operation.in_(query, self.model.apply_id, apply_id_list)
        return query

    def less_than(self, query, meet_id):
        query = Operation.less_than(query, self.model.id, meet_id)
        return query

    def get_by_address(self, address):
        query = self.get_query()
        return Operation.filter(query, self.model.address, address)

    def find_by_address(self, address):
        query = self.get_query()
        return Operation.ilike(query, self.model.address, address)
