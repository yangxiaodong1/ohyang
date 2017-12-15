from DB.mysql.models.ohho.permission.page_permission import OHHOPermissionPagePermission
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_encryption import OHHOEncryption
from Tools.ohho_operation import OHHOOperation


class DBOHHOPermissionPagePermission(DBBase):
    def __init__(self, index=0):
        super(DBOHHOPermissionPagePermission, self).__init__(OHHOPermissionPagePermission, index)

    def get_by_page(self, query, page_id):
        if query and page_id:
            return Operation.filter(query, self.model.page_id, page_id)
        else:
            return None

    def get_by_page_permission_ids(self, query, page_permission_id_list):
        if query and page_permission_id_list:
            return Operation.in_(query, self.model.id, page_permission_id_list)
        else:
            return None

    def get_by_timestamp(self, timestamp):
        query = self.get_query()
        query = Operation.filter(query, self.model.timestamp, timestamp)
        query = self.order_by_id_asc(query)
        return self.first(query)
