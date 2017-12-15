from DB.mysql.models.ohho.permission.page import OHHOPermissionPage
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_encryption import OHHOEncryption
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog


class DBOHHOPermissionPage(DBBase):
    def __init__(self, index=0):
        super(DBOHHOPermissionPage, self).__init__(OHHOPermissionPage, index)

    def get_by_name(self, query, name):
        return Operation.filter(query, self.model.name, name)

    def add(self, name, description=None):
        if description:
            data_index = {"name": name, "description": description}
        else:
            data_index = {"name": name}
        return Operation.add(self.model, data_index)

    def get_all(self):
        query = self.get_query()
        query = self.order_by_id_desc(query)
        return query