from DB.mysql.models.ohho.relation.model_ohho_user_and_cellphone_relation import OHHOUserAndCellphoneRelation
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOUserAndCellphoneRelation(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUserAndCellphoneRelation, self).__init__(OHHOUserAndCellphoneRelation, index)

    def find_by_cellphone(self, query, cellphone_id_list):
        return Operation.in_(query, self.model.cellphone_id, cellphone_id_list)

    def get_by_cellphone_and_user(self, cellphone_id, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.cellphone_id, cellphone_id)
        query = Operation.filter(query, self.model.user_id, user_id)
        query = self.order_by_id_desc(query)
        return Operation.first(query)

    def get_by_cellphone(self, cellphone_id):
        query = self.get_query()
        return Operation.filter(query, self.model.cellphone_id, cellphone_id)

    def get_by_user(self, user_id):
        query = self.get_query()
        return Operation.filter(query, self.model.user_id, user_id)

    def find_by_user(self, query, user_id_list):
        return Operation.in_(query, self.model.user_id, user_id_list)

    def get_valid(self, query):
        return super(DBOHHOUserAndCellphoneRelation, self).get_valid(query, True)

    def get_invalid(self, query):
        return super(DBOHHOUserAndCellphoneRelation, self).get_invalid(query, True)

    def delete(self, instance):
        return super(DBOHHOUserAndCellphoneRelation, self).delete(instance, True)

    def restore(self, instance):
        return super(DBOHHOUserAndCellphoneRelation, self).restore(instance, True)
