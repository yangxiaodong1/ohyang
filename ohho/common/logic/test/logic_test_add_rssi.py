from Tools.ohho_operation import OHHOOperation
from ohho.common.db.test.db_test_rssi import DBTestRssi
from ohho.common.db.test.db_test_rssi_distance import DBTestRssiDistance
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog


class LogicTestAddRssi(object):
    def __init__(self):
        self.rssi = DBTestRssi()
        self.rssi_distance = DBTestRssiDistance()

    def add(self, data):
        # data_list = self.parse_rssi_parameters(data)
        # OHHOLog.print_log(data_list)
        if data:
            data = OHHOOperation.json2dict(data)
            success = self.add_rssi(data)
            if success:
                return Result.result_success()
            else:
                return Result.result_failed("failed!")
        else:
            return Result.result_failed("no data")

    def add_rssi(self, dict_list):
        return self.rssi.bulk_add(dict_list)

    def add_rssi_distance(self, rssi_distance_dict):
        return self.rssi_distance.add(rssi_distance_dict)

    def parse_rssi_parameters(self, rssi_parameters):
        """
        数据结构
        {
                    "phone": "leilei",
                    "mine": [{ "device": "12341234123", "timestamp": "1234123434213", "rssi": "30" }],
                    "others": [
                        { "device": "132413241234", "timestamp": 1234123421341, "rssi": 20 },
                        { "device": "1324132412asdf34", "timestamp": 1234123421342, "rssi": 30 },
                        { "device": "1324132412sdfs34", "timestamp": 1234123421343, "rssi": 40 }
                    ]
        }
        :param rssi_parameters:
        :return:
        """
        rssi_parameters_dict = OHHOOperation.json2dict(rssi_parameters)
        data = list()
        if rssi_parameters_dict:
            phone = rssi_parameters_dict["phone"]
            mine_type = 0
            others_type = 1
            mine = rssi_parameters_dict["mine"]
            others = rssi_parameters_dict["others"]
            if mine:
                for m in mine:
                    temp = dict()
                    temp["phone"] = phone
                    temp["type"] = mine_type
                    temp["device"] = m["device"]
                    temp["timestamp"] = m["timestamp"]
                    temp["rssi"] = m["rssi"]
                    temp["real_distance"] = m["real_distance"]
                    data.append(temp)
                for o in others:
                    temp = dict()
                    temp["phone"] = phone
                    temp["type"] = others_type
                    temp["device"] = o["device"]
                    temp["timestamp"] = o["timestamp"]
                    temp["rssi"] = o["rssi"]
                    temp["real_distance"] = o["real_distance"]
                    data.append(temp)
        return data
