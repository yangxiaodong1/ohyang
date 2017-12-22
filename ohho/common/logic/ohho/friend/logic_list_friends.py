from ohho.common.logic.common.user import User
# from ohho.common.logic.common.im.friend import Friend
from ohho.common.logic.common.record.friend import Friend
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog


class LogicListFriends(object):
    def __init__(self):
        self.user = User()
        self.friend = Friend()

    def list_friends(self, user_id, base_url):
        # friend_relations = self.friend.get_friends(user_id)
        friend_relations = self.friend.get_friend_by_user(user_id)
        data = list()
        for relation in friend_relations:
            # user = self.user.get_by_id(relation.friend_account_id)
            # if user:
            if relation.apply_id:
                OHHOLog.print_log(relation.friend_account_id)
                temp = self.user.get_user_information4friend(relation.friend_account_id, base_url)
                OHHOLog.print_log(temp)
                if temp:
                    temp = self.user.set_map_by_exclude(temp, relation.friend_account_id, user_id)
                    temp = self.user.set_map_by_is_online(temp, relation.friend_account_id, user_id)
                    data.append(temp)

        result = Result.result_success()
        result["data"] = data
        return result
