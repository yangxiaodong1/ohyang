from DB.mysql.models.ohho.record.model_ohho_record_match_met import OHHORecordMatchMet as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation
from sqlalchemy import or_


class DBOHHORecordMatchMet(DBBase):
    def __init__(self):
        super(DBOHHORecordMatchMet, self).__init__(model)

    def get_by_user(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        return query

    def get_by_another_user(self, another_user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.another_user_id, another_user_id)
        return query

    def get_met_list(self, user_id):
        query = self.get_query()
        query = query.filter(or_(self.model.user_id == user_id, self.model.another_user_id == user_id))
        return query

    def get_by_user_id(self, query, user_id):
        return Operation.filter(query, self.model.user_id, user_id)

    def get_by_another_user_id(self, query, another_user_id):
        return Operation.filter(query, self.model.another_user_id, another_user_id)

    def get_by_users(self, user_id, another_user_id):
        query = self.get_query()
        query = self.get_by_user_id(query, user_id)
        query = self.get_by_another_user_id(query, another_user_id)
        query = self.order_by_id_desc(query)
        return self.first(query)

    def get_by_apply(self, apply_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.apply_id, apply_id)
        query = self.order_by_id_desc(query)
        return Operation.first(query)

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
