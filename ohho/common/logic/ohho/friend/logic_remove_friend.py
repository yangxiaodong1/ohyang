# from ohho.common.logic.common.im.meet import Meet
# from ohho.common.logic.common.im.friend import Friend
# from ohho.common.logic.common.record.friend import Friend
from ohho.common.logic.common.record.friend import Friend as RecordFriend
from ohho.common.logic.common.im.netease.friend import Friend as IMFriend
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog


class LogicRemoveFriend(object):
    def __init__(self):
        self.record_friend = RecordFriend()

    def remove_friend(self, user_id, friend_user_id):
        """
        是好友，可以移除好友
        :param user_id: 用户ID
        :param friend_user_id: 另一用户ID
        :return:
        """
        # query = self.friend.get_relation_by_user_and_friend(user_id, friend_user_id)
        # query = self.friend.get_valid_relation(query)
        # relation = self.friend.first_relation(query)

        relation = self.record_friend.get_friend_by_user_and_friend(user_id, friend_user_id)
        if relation:
            success = self.record_friend.remove_friend(relation)
            if success:
                im_success = IMFriend.remove_friend(user_id, friend_user_id)
                OHHOLog.print_log(im_success)
                return Result.result_success()
            else:
                return Result.result_failed()
        else:
            return Result.result_failed("he is not your friend or black!")

            # if self.friend.is_friend(user_id, friend_user_id):
            #     instance = self.friend.get_friend_by_user_and_friend(user_id, friend_user_id)
            #     success = self.friend.remove_friend(instance)
            #     if success:
            #         return Result.result_success()
            #     else:
            #         return Result.result_failed()
            # else:
            #     return Result.result_failed("he is not your friend!")
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
