from DB.mysql.models.ohho.record.model_ohho_record_user_and_match_condition import OHHORecordUserAndMatchCondition
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHORecordUserAndMatchCondition(DBBase):
    def __init__(self, index=0):
        super(DBOHHORecordUserAndMatchCondition, self).__init__(OHHORecordUserAndMatchCondition, index=0)

    def get_nearest_by_user(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        query = self.order_by_id_desc(query)
        return Operation.first(query)

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


if __name__ == "__main__":
    pass
