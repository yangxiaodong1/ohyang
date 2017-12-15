# from ohho.common.logic.common.im.friend import Friend
from ohho.common.logic.common.record.friend import Friend
from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.detail_constant import RELATION_NOT_EXIST


class LogicAddBlack(object):
    def __init__(self):
        self.friend = Friend()

    def add_black(self, user_id, friend_user_id):
        relation = self.friend.get_friend_by_user_and_friend(user_id, friend_user_id)
        black_relation = self.friend.get_black_by_user_and_friend(user_id, friend_user_id)

        if relation or black_relation:
            relation = relation if relation else black_relation
            success = self.friend.add_black(relation)
            if success:
                result = Result.result_success()
            else:
                result = Result.result_failed()
        else:
            data = dict()
            data["account_id"] = user_id
            data["friend_account_id"] = friend_user_id
            data["type"] = 2

            success = self.friend.friend.add(data)
            if success:
                result = Result.result_success("add black successfully!")
            else:
                result = Result.result_failed("add black failed!")

        return result
