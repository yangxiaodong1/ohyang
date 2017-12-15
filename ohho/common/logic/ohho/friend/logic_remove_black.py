# from ohho.common.logic.common.im.friend import Friend
from ohho.common.logic.common.record.friend import Friend
from ohho.common.logic.common.result import Result


class LogicRemoveBlack(object):
    def __init__(self):
        self.friend = Friend()

    def remove_black(self, user_id, friend_user_id):
        # query = self.friend.get_relation_by_user_and_friend(user_id, friend_user_id)
        # query = self.friend.get_valid_relation(query)
        # relation = self.friend.first_relation(query)
        relation = self.friend.get_black_by_user_and_friend(user_id, friend_user_id)
        if relation:
            if relation.apply_id:
                success = self.friend.black2friend(relation)
            else:
                success = self.friend.friend.delete(relation)

            if success:
                result = Result.result_success()
            else:
                result = Result.result_failed()
        else:
            result = Result.result_not_exist()

        return result
