# from ohho.common.db.ohho.db_ohho_user import DBOHHOUser
# from ohho.common.logic.common.im.friend import Friend
from ohho.common.logic.common.record.friend import Friend
from ohho.common.logic.common.user import User
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog


class LogicListBlacks(object):
    def __init__(self):
        self.user = User()
        self.friend = Friend()

    def list_blacks(self, user_id, base_url):
        # OHHOLog.print_log("here is black")
        # OHHOLog.print_log(user_id)
        friend_relations = self.friend.get_blacks(user_id)
        # OHHOLog.print_log(self.friend.friend.get_count(friend_relations))
        data = list()
        for relation in friend_relations:
            # OHHOLog.print_log(relation.id)
            # user = self.user.get_by_id(relation.friend_account_id)
            # if user:
            temp = self.user.get_user_information(relation.friend_account_id, base_url)
            if temp:
                data.append(temp)

        result = Result.result_success()
        if data:
            result["data"] = data
        return result
