from ohho.common.logic.common.user import User
from ohho.common.logic.common.record.friend import Friend
# from ohho.common.logic.common.record.meet import Meet
# from ohho.common.logic.common.im.friend import Friend
# from ohho.common.logic.common.im.meet import Meet
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog


class LogicListApplyFriend(object):
    def __init__(self):
        # self.meet = Meet()
        self.friend = Friend()
        self.user = User()

    def list_apply_friend(self, user_id, base_url):
        """
        最近24小时内申请你为好友的用户

        :param user_id: 用户ID
        :param friend_user_id: 另一用户ID
        :return:
        """
        applies = self.friend.get_apply_by_friend(user_id)
        friend_user_ids = [(apply.id, apply.one_user_id) for apply in applies]
        data = list()
        if friend_user_ids:
            for apply_id, uid in friend_user_ids:
                information = self.user.get_friend_information(user_id, uid, apply_id, base_url)
                if information:
                    data.append(information)
        result = Result.result_success()
        if data:
            result["data"] = data

        return result

        # applies = self.meet.get_apply_friend_list(user_id)
        # friend_user_ids = [(apply.id, apply.one_user_id) for apply in applies]
        # data = list()
        # if friend_user_ids:
        #     for apply_id, uid in friend_user_ids:
        #         information = self.user.get_friend_information(user_id, uid, apply_id, base_url)
        #         if information:
        #             data.append(information)
        # result = Result.result_success()
        # if data:
        #     result["data"] = data
        #
        # return result
