from DB.mysql.models.ohho.permission.group_and_user_relation import OHHOPermissionGroupAndUserRelation
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_operation import OHHOOperation


class DBOHHOPermissionGroupAndUserRelation(DBBase):
    def __init__(self, index=0):
        super(DBOHHOPermissionGroupAndUserRelation, self).__init__(OHHOPermissionGroupAndUserRelation, index)

    def get_by_username(self, query, username):
        return Operation.filter(query, self.model.username, username)

    def get_by_group_id(self, group_id):
        query = self.get_query()
        return Operation.filter(query, self.model.group_id, group_id)

    def get_by_group_id_new(self, query, group_id):
        return Operation.filter(query, self.model.group_id, group_id)

    def get_by_group_id_and_username(self, group_id, username):
        query = self.get_by_group_id(group_id)
        query = self.get_by_username(query, username)
        query = self.order_by_id_desc(query)
        query = self.first(query)
        return query


