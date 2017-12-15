from DB.mysql.models.ohho.device.model_ohho_device_sensor import OHHODeviceSensor
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHODeviceSensor(DBBase):
    def __init__(self, index=0):
        super(DBOHHODeviceSensor, self).__init__(OHHODeviceSensor, index)

    def get_by_user(self, query, user_id):
        return Operation.filter(query, self.model.user_id, user_id)

    def get_by_device(self, query, device_id):
        return Operation.filter(query, self.model.device_id, device_id)


if __name__ == "__main__":
    identity_id = 123456789
    pass
