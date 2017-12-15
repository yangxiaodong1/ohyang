from DB.mysql.models.ohho.device.model_ohho_device_setting import OHHODeviceSetting
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHODeviceSetting(DBBase):
    def __init__(self, index=0):
        super(DBOHHODeviceSetting, self).__init__(OHHODeviceSetting, index)

    def get_by_device(self, device_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.device_id, device_id)
        return Operation.first(query)


if __name__ == "__main__":
    pass
