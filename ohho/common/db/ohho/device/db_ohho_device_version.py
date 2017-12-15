from DB.mysql.models.ohho.device.model_ohho_device_version import OHHODeviceVersion
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHODeviceVersion(DBBase):
    def __init__(self, index=0):
        super(DBOHHODeviceVersion, self).__init__(OHHODeviceVersion, index)

    def get_by_version(self, version):
        query = self.get_query()
        query = Operation.filter(query, self.model.version, version)
        return Operation.first(query)


if __name__ == "__main__":
    pass
