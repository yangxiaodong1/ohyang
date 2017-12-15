from ohho.common.db.test.db_test_rssi import DBTestRssi
from ohho.common.db.test.db_test_rssi_distance import DBTestRssiDistance


class LogicTestCommon(object):
    def __init__(self):
        self.rssi = DBTestRssi()
        self.rssi_distance = DBTestRssiDistance()

    def add_rssi(self, rssi_dict):
        return self.rssi.add(rssi_dict)

    def add_rssi_distance(self, rssi_distance_dict):
        return self.rssi_distance.add(rssi_distance_dict)

    def update_rssi_distance(self, rssi_distance_instance, rssi_distance_dict):
        return self.rssi_distance.update(rssi_distance_instance, rssi_distance_dict)

    def get_rssi_by_timestamp(self, query, timestamp):
        return self.rssi.get_less_than_changed_at()

    # def get_by_type(self, type):
    #     query = self.rssi.get_query()
    #     return self.rssi.get_by_type(query, type)
