from DB.mysql.models.ohho.permission.group_and_page_relation import OHHOPermissionGroupAndPageRelation
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_operation import OHHOOperation


class DBOHHOPermissionGroupAndPageRelation(DBBase):
    def __init__(self, index=0):
        super(DBOHHOPermissionGroupAndPageRelation, self).__init__(OHHOPermissionGroupAndPageRelation, index)

    def get_by_page_permission_ids(self, query, page_permission_id_list):
        return Operation.in_(query, self.model.page_permission_id, page_permission_id_list)

    def get_by_group_ids(self, query, group_id_list):
        return Operation.in_(query, self.model.group_id, group_id_list)

    def get_by_group_id(self, query, group_id):
        return Operation.filter(query, self.model.group_id, group_id)

    def get_by_page_permission_id(self, query, page_permission_id):
        return Operation.filter(query, self.model.page_permission_id, page_permission_id)
