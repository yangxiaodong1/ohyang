from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.constant import *
from Tools.ohho_log import OHHOLog


class LogicRefuseMeet(object):
    def __init__(self):
        self.meet = Meet()
        self.user = User()

    def push_information(self, to_user_id, user_id, apply_id, type, base_url):
        information = self.user.get_refuse_meet_user_information(user_id, apply_id, base_url)
        information["function"] = "refuse meet"
        return self.user.push_user_information(to_user_id, type, information)

    def refuse_meet(self, user_id, friend_user_id, apply_id, base_url):
        """
        拒绝见面
        只要对方有申请见面,就可以拒绝见面
        :param user_id: 用户ID
        :param friend_user_id: 另一用户ID
        :param meet_state: 见面状态 0未见，1见面，2 请求相见，3同意相见，4不同意相见，5 取消见面，默认为0
        :return:
        """
        # 向对方发送拒绝的推送
        type = PUSH_STATE_TYPE_REFUSE_MEET
        if not self.meet.is_meet_end(apply_id, friend_user_id):
            result = self.push_information(friend_user_id, user_id, apply_id, type, base_url)
            OHHOLog.print_log(result)
        # information = self.user.get_push_user_information(user_id, apply_id, base_url)
        # information["function"] = "refuse meet"
        # self.user.push_user_information(friend_user_id, PUSH_STATE_TYPE_REFUSE_MEET, information)
        self.meet.add_exclude(user_id, friend_user_id)
        self.meet.add_refuse(apply_id, user_id)
        return Result.result_success()


        # has_valid_apply = self.meet.has_valid_apply(friend_user_id, user_id)
        # if has_valid_apply:
        #     apply = self.meet.get_apply_by_user_and_friend(friend_user_id, user_id)
        #     success = self.meet.add_refuse(apply.id, user_id)
        #     if success:
        #
        #         log_string = "%d refuse %d to meet" % (user_id, friend_user_id)
        #         OHHOLog.print_log(log_string)
        #
        #         message = self.user.get_user_basic_information(user_id, base_url)
        #         self.user.push(log_string, friend_user_id, DEFAULT_IM_USER_ID)
        #         return Result.result_success()
        #     else:
        #         return Result.result_failed()
        # else:
        #     return Result.result_failed("no valid apply!")
