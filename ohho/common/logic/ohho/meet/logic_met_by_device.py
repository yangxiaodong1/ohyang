from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.constant import *
from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
from settings import DEFAULT_IM_USER_ID
from Tools.ohho_log import OHHOLog


class LogicMetByDevice(object):
    def __init__(self):
        self.meet = Meet()
        self.user = User()
        self.map = DBOHHOMapInformation()

    def push_information(self, to_user_id, user_id, apply_id, type, base_url):
        information = self.user.get_met_user_information(user_id, apply_id, base_url)
        information["function"] = "met by device"
        return self.user.push_user_information(to_user_id, type, information)

    def met(self, user_id, friend_user_id, apply_id, base_url):
        user_id = int(user_id)
        friend_user_id = int(friend_user_id)
        apply_id = int(apply_id)
        type = PUSH_STATE_TYPE_MET
        result = self.push_information(friend_user_id, user_id, apply_id, type, base_url)
        OHHOLog.print_log(result)
        # information = self.user.get_push_user_information(user_id, apply_id, base_url)
        # information["function"] = "met by device"
        # self.user.push_user_information(friend_user_id, PUSH_STATE_TYPE_MET, information)

        user_map = self.map.get_by_user(user_id)
        if user_map:
            user_address = user_map.address
        else:
            user_address = ""
        friend_user_map = self.map.get_by_user(friend_user_id)

        if friend_user_map:
            friend_user_address = friend_user_map.address
        else:
            friend_user_address = ""

        data = dict()
        data["user_id"] = user_id
        data["another_user_id"] = friend_user_id
        data["apply_id"] = apply_id
        data["user_address"] = user_address
        data["friend_user_map"] = friend_user_address
        data["type"] = 0
        self.meet.add_met(data)
        return Result.result_success()
