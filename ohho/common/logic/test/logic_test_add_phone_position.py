from ohho.common.db.test.db_test_phone_position import DBTestPhonePosition


class LogicTestAddPhonePosition(object):
    def __init__(self):
        self.position = DBTestPhonePosition()

    def add(self, data_dict):
        return self.position.add(data_dict)
        # def __init__(self):
        #     self.rssi = DBTestRssi()
        #     self.rssi_distance = DBTestRssiDistance()

        # def add_rssi(self, rssi_dict):
        #     return self.rssi.add(rssi_dict)
        #
        # def add_rssi_distance(self, rssi_distance_dict):
        #     return self.rssi_distance.add(rssi_distance_dict)
