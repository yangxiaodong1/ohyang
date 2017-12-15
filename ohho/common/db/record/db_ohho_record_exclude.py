from DB.mysql.models.ohho.record.model_ohho_record_exclude import OHHORecordExclude
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBOHHORecordExclude(DBBase):
    def __init__(self):
        super(DBOHHORecordExclude, self).__init__(OHHORecordExclude)

    def get_by_user(self, query, user_id):
        return Operation.filter(query, self.model.user_id, user_id)

    def get_by_exclude_user(self, query, exclude_user_id):
        return Operation.filter(query, self.model.exclude_user_id, exclude_user_id)

    def get_by_condition(self, query, match_condition_id):
        return Operation.filter(query, self.model.match_condition_id, match_condition_id)

    def get_by_user_and_condition(self, query, user_id, match_condition_id):
        query = self.get_by_user(query, user_id)
        query = self.get_by_condition(query, match_condition_id)
        return query
