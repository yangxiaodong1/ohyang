from DB.mysql.models.ohho.permission.group import OHHOPermissionGroup
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_encryption import OHHOEncryption
from Tools.ohho_operation import OHHOOperation


class DBOHHOPermissionGroup(DBBase):
    def __init__(self, index=0):
        super(DBOHHOPermissionGroup, self).__init__(OHHOPermissionGroup, index)

    def get_group_by_ids(self, query, group_id_list):
        return Operation.in_(query, self.model.id, group_id_list)

    def get_by_name(self, query, name):
        return Operation.ilike(query,self.model.name, name)

    def get_all(self):
        query = self.get_query()
        query = self.order_by_id_desc(query)
        return query