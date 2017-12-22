from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.constant import *
from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
# from ohho.common.logic.ohho.detail_constant import RELATION_NOT_EXIST
from settings import DEFAULT_IM_USER_ID
from Tools.ohho_log import OHHOLog


class LogicMetByHand(object):
    def __init__(self):
        self.meet = Meet()
        self.user = User()
        self.map = DBOHHOMapInformation()

    def met(self, user_id, friend_user_id, apply_id, base_url):
        map = self.map.get_by_user(user_id)
        if map:
            address = map.address
        else:
            address = ""
        one_user_map = self.user.get_user_map_information(user_id)
        if one_user_map:
            self.meet.add_meet(one_user_map, apply_id)
            self.meet.delete_meeting(apply_id, user_id)

        single_meet = self.meet.get_user_meet(apply_id, friend_user_id)
        if single_meet:
            OHHOLog.print_log("single meet")
            the_met = self.meet.get_met_by_users(user_id, friend_user_id)
            OHHOLog.print_log(the_met)
            if not the_met:
                OHHOLog.print_log("add met")
                data = dict()
                another_user_map = self.user.get_user_map_information(friend_user_id)
                data["apply_id"] = apply_id
                data["type"] = 1
                data["user_id"] = user_id
                data["user_longitude"] = one_user_map["longitude"]
                data["user_latitude"] = one_user_map["latitude"]
                data["user_address"] = one_user_map["address"]

                data["another_user_id"] = friend_user_id
                data["another_user_longitude"] = another_user_map["longitude"]
                data["another_user_latitude"] = another_user_map["latitude"]
                data["another_user_address"] = another_user_map["address"]
                OHHOLog.print_log("before add met")
                self.meet.add_met(data)
                OHHOLog.print_log("after add met")
        else:
            data = dict()
            data["is_meet"] = True
            data["user_id"] = user_id
            data["apply_id"] = apply_id
            self.user.push(data, friend_user_id)
        return Result.result_success()
