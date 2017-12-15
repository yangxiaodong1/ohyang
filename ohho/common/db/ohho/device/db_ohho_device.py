from DB.mysql.models.ohho.device.model_ohho_device import OHHODevice
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_log import OHHOLog
from settings import TEST


class DBOHHODevice(DBBase):
    def __init__(self, identity_id=None, mac_address=None, index=0):
        super(DBOHHODevice, self).__init__(OHHODevice, index)
        self.identity_id = identity_id
        self.mac_address = mac_address

    def set_identity(self, identity_id):
        self.identity_id = identity_id

    def get_identity(self):
        return self.identity_id

    def set_mac_address(self, mac_address):
        self.mac_address = mac_address

    def get_mac_address(self):
        return self.mac_address

    def get_by_identity(self):
        # query = self.get_query()
        # OHHOLog.print_log(self.identity_id)
        if self.identity_id:
            # OHHOLog.print_log(self.identity_id)
            query = self.get_query()
            # OHHOLog.print_log(self.get_count(query))
            query = Operation.filter(query, self.model.identity_id, self.identity_id)
            # OHHOLog.print_log(self.get_count(query))
            return Operation.first(query)
        else:
            # OHHOLog.print_log(self.identity_id)
            return None

    def check_by_mac(self):
        if TEST:
            return True
        else:
            instance = self.get_by_identity()
            if instance and instance.mac_address == self.mac_address:
                return True
            else:
                return False

    def find_by_identity(self, query):
        return Operation.ilike(query, self.model.identity_id, self.identity_id)

    def find_by_mac_address(self, query):
        return Operation.ilike(query, self.model.mac_address, self.mac_address)


if __name__ == "__main__":
    identity_id = 123456789
    device = DBOHHODevice.get_by_identity(identity_id)
    print(device.id)
