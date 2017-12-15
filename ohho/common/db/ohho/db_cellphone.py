from DB.mysql.models.model_cellphone import Cellphone
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_encryption import OHHOEncryption
from Tools.ohho_operation import OHHOOperation


class DBCellphone(DBBase):
    def __init__(self, key=None, index=0):
        super(DBCellphone, self).__init__(Cellphone, index)
        self.key = key

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def find_by_key(self, query, key):
        return Operation.ilike(query, self.model.key, key)

    def find_by_manufacturer(self, query, manufacturer):
        return Operation.ilike(query, self.model.manufaturer, manufacturer)

    def find_by_platform(self, query, platform_type):
        return Operation.ilike(query, self.model.platform_type, platform_type)

    def find_by_mac_address(self, query, mac_address):
        return Operation.ilike(query, self.model.mac_address, mac_address)

    def get_by_key(self):
        if self.key:
            query = self.get_query()
            query = Operation.filter(query, self.model.key, self.key)
            return Operation.first(query)
        else:
            return None
