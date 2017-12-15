from ohho.common.logic.common.user import User
from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.detail_constant import RELATION_NOT_EXIST


class LogicGetUserInformation(object):
    def __init__(self):
        self.user = User()

    def get(self, friend_user_id, user_id, base_url):
        if friend_user_id:
            result = Result.result_success()
        else:
            result = Result.result_failed()
        data = self.user.get_user_information(friend_user_id, base_url)
        relation, apply_id, applied_id = self.user.get_friend_relation(user_id, friend_user_id)
        data["relation"] = relation
        data = self.user.set_map_by_exclude(data, user_id, friend_user_id)
        data = self.user.set_map_by_is_online(data, user_id, friend_user_id)
        result["data"] = data

        return result
