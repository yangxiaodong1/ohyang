from Tools.ohho_operation import OHHOOperation
from ohho.common.db.test.db_test_map_information import DBTestMapInformation
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog


class LogicTestAddMapInformation(object):
    def __init__(self):
        self.map = DBTestMapInformation()

    def add(self, user_id, another_user_id, map_information, base_url, timestamp=None):
        if timestamp:
            map_information["timestamp"] = timestamp
        map_information["user_id"] = user_id
        map_information["another_user_id"] = another_user_id
        success = self.map.add(map_information)
        if success:
            result = Result.result_success()
        else:
            result = Result.result_failed()
        # return result
        map_instance = self.map.get_by_user_id(another_user_id)
        result["data"] = dict()
        if map_instance:
            OHHOLog.print_log("has map")
            OHHOLog.print_log(map_instance)
            OHHOLog.print_log(self.map.get_information(map_instance, base_url))
            result["data"]["information"] = self.map.get_information(map_instance, base_url)
        else:
            OHHOLog.print_log("not has map")
            result["data"]["information"] = dict()
        return result
