from ohho.common.logic.common.user import User
from ohho.common.view.common.constant import *
from ohho.common.logic.common.im.netease.update_user_info import UpdateUserInfo
from Tools.ohho_log import OHHOLog
from Tools.ohho_operation import OHHOOperation



class LogicAddUserAccuracyExtension(object):
    def __init__(self):
        self.user = User()

    def add_user_accuracy_extension(self, user_id, user_extension_dict):
        OHHOLog.print_log(user_extension_dict)
        result = self.user.add_user_extension(user_id, user_extension_dict)
        nickname = user_extension_dict.get(USER_EXTENSION_NICK_NAME, None)
        primary_interest = user_extension_dict.get(USER_EXTENSION_PRIMARY_INTEREST, "")
        primary_interest = OHHOOperation.dict2json(primary_interest)
        OHHOLog.print_log(user_extension_dict)
        OHHOLog.print_log(USER_EXTENSION_PRIMARY_INTEREST)
        OHHOLog.print_log(primary_interest)
        if nickname is not None:
            UpdateUserInfo.update_user_info(user_id, name=nickname)
        # create or update match condition
        relation = self.user.record_user_and_match_condition.get_nearest_by_user(user_id)
        if relation and relation.match_condition_id:
            condition = self.user.match_condition.get_by_id(relation.match_condition_id)
        else:
            condition = None
            condition_id = self.user.add_new_condition(user_id)
            if condition_id:
                condition = self.user.match_condition.get_by_id(condition_id)

        if condition:
            OHHOLog.print_log(condition.id)
            self.user.match_condition.update(condition, {"interest": primary_interest})
        return result

        # def parse_data(self, data):
        #     result = dict()
        #     if data:
        #         data_list = data.split("&")
        #         if data_list:
        #             for d in data_list:
        #                 key, value = d.split("=")
        #                 if key in ("sex", "marriage", "hometown_area", "current_area", "industry_id",
        #                            "body_type_id", "smoke_id", "drink_id", "work_domain_id", "profession_id"):
        #                     result[key] = int(value)
        #                 elif key in ("height", "weight"):
        #                     result[key] = float(value)
        #                 elif key in ("birthday"):
        #                     if value:
        #                         result[key] = OHHODatetime.string2date(value)
        #                     else:
        #                         result[key] = None
        #                 else:
        #                     result[key] = value
        #     return result


