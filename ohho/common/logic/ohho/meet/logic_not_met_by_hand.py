from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.constant import *
from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
# from ohho.common.logic.ohho.detail_constant import RELATION_NOT_EXIST
from settings import DEFAULT_IM_USER_ID
from Tools.ohho_log import OHHOLog


class LogicNotMetByHand(object):
    def __init__(self):
        self.user = User()

    def not_met(self, user_id, friend_user_id, apply_id):
        data = dict()
        data["user_id"] = user_id
        data["is_meet"] = False
        data["apply_id"] = apply_id
        self.user.push(data, friend_user_id)
        return Result.result_success()
