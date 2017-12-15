from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.record.match_apply import MatchApply
from ohho.common.logic.common.record.match_condition import MatchCondition
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from settings import DEFAULT_IM_USER_ID
from Tools.ohho_log import OHHOLog


class LogicApplyMeet(object):
    def __init__(self):
        self.apply = MatchApply()
        self.condition = MatchCondition()
        self.meet = Meet()
        self.user = User()

    def apply_meet(self, user_id, friend_user_id, match_condition_id, base_url):
        """
        申请见面
        见过面的不能申请

        :param user_id: 用户ID
        :param friend_user_id: 另一用户ID
        :param match_condition_id: 配对条件ID
        :return:
        """
        result = dict()
        if self.meet.has_valid_apply(user_id, friend_user_id):
            return Result.result_has_valid_meet_apply()
        if self.meet.is_meet(user_id, friend_user_id):
            return Result.result_is_meet()

        condition = self.condition.get_by_id(match_condition_id)
        if condition:
            success = self.meet.add_apply(user_id, friend_user_id, match_condition_id)
            if success:
                log_string = "%d apply %d to meet" % (user_id, friend_user_id)
                OHHOLog.print_log(log_string)
                message = self.user.get_user_basic_information(user_id, base_url)
                self.user.push(log_string, friend_user_id, DEFAULT_IM_USER_ID)
                return Result.result_success()
            else:
                return Result.result_failed()
        else:
            return Result.result_failed("no such condition!")
            # relation = self.meet.create_or_get_relation(user_id, friend_user_id)
            # if relation:
            #     if self.meet.is_meet(relation):
            #         result = Result.get_result(False, -11, -11, "you have been met before!")
            #     else:
            #         result = self.meet.apply_meet(relation)
            # else:
            #     result = Result.get_result(False, -12, -12, "no such valid relation!")
            #
            # return result
