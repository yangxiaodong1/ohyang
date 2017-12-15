from DB.mysql.models.ohho.record.model_ohho_record_user_and_match_condition import \
    OHHORecordUserAndMatchCondition as model
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHORecordUserAndMatchCondition(DBBase):
    def __init__(self):
        super(DBOHHORecordUserAndMatchCondition, self).__init__(model)

    def filter_by_user(self, query, user_id):
        return Operation.filter(query, self.model.user_id, user_id)

    def find_by_user(self, query, user_id_list):
        return Operation.in_(query, self.model.user_id, user_id_list)

    def filter_by_name(self, query, name):
        return Operation.filter(query, self.model.name, name)

    def find_by_name(self, query, name):
        return Operation.ilike(query, self.model.name, name)

    def filter_by_match_condition(self, query, match_condition_id):
        return Operation.filter(query, self.model.match_condition_id, match_condition_id)

    def find_by_match_condition(self, query, match_condition_id_list):
        return Operation.in_(query, self.model.match_condition_id, match_condition_id_list)
