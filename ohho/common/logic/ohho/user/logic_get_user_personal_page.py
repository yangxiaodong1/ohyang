from ohho.common.logic.common.user import User
from ohho.common.logic.common.result import Result


class LogicGetUserPersonalPage(object):
    def __init__(self):
        self.user = User()

    def get(self, user_id, friend_id, base_url=None):
        friend = self.user.user.get_by_id(friend_id)
        if friend_id and user_id:
            if friend and friend.state:
                result = Result.result_success()
                result["data"] = self.user.get_user_information(friend_id, base_url)
                temp_relation = self.user.get_user_and_friend_relation(user_id, friend_id)
                if temp_relation:
                    relation = 1
                else:
                    relation = 0
                result["relation"] = relation
                result["state"] = 1
            else:
                result = Result.result_failed("friend not exit")
                result["state"] = 0
        else:
            result = Result.result_parameters_are_invalid()
            result["state"] = 0

        return result


