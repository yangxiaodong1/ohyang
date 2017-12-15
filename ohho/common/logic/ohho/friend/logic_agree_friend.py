# from ohho.common.logic.common.im.meet import Meet
from ohho.common.logic.common.record.friend import Friend
from ohho.common.logic.common.im.netease.friend import Friend as IMFriend
# from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog


class LogicAgreeFriend(object):
    def __init__(self):
        # self.meet = Meet()
        self.friend = Friend()
        self.im_friend = IMFriend()

    def agree_friend(self, user_id, friend_user_id):
        """
        同意添加好友
        用户已经申请,并且你们不是朋友/黑名单关系,可以同意
        :param user_id: 用户ID
        :param friend_user_id: 另一用户ID
        :return:
        """
        # if self.friend.has_valid_apply(friend_user_id, user_id):
        apply = self.friend.get_apply_by_user_and_friend(friend_user_id, user_id)
        if apply:
            if not self.friend.is_friend_or_black(user_id, friend_user_id):
                result = self.friend.add_friend(user_id, friend_user_id, apply.id)
                success = self.friend.add_agree(apply.id)
                if success:
                    log_string = "%d agree %d to be friend" % (user_id, friend_user_id)
                    OHHOLog.print_log(log_string)
                    self.im_friend.agree_friend(user_id, friend_user_id, "")
                    return result
                else:
                    return Result.result_failed()
        else:
            return Result.result_failed("no valid friend apply!")

            #
            # friend_meet_relation = self.meet.get_some_valid_relation(friend_user_id, user_id)
            # friend_relation = self.friend.get_some_valid_relation(user_id, friend_user_id)
            # if not friend_relation:
            #     if self.meet.is_apply_friend(friend_meet_relation):
            #         relation = self.meet.create_or_get_relation(user_id, friend_user_id)
            #         success = self.meet.agree_friend(relation)
            #         if success:
            #             success_one = self.friend.create_or_get_relation(user_id, friend_user_id)
            #             success_two = self.friend.create_or_get_relation(friend_user_id, user_id)
            #             if success_one and success_two:
            #                 result = Result.result_success()
            #             else:
            #                 result = Result.result_failed()
            #         else:
            #             result = Result.result_failed(RELATION_NOT_EXIST)
            #     else:
            #         result = Result.result_failed(RELATION_NOT_EXIST)
            # else:
            #     result = Result.result_success(EXIST)
            #
            # return result
