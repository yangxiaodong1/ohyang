from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User


class LogicGetMapPositions(object):
    def __init__(self):
        self.user = User()

    def get(self, user_id, base_url):
        result = Result.result_success()
        users = self.user.get_all()
        data = list()
        if self.user.user.is_empty(users):
            pass
        else:
            for user in users:
                if user_id == user.id:
                    continue
                temp = self.user.get_user_basic_information(user.id, base_url)
                if temp:
                    data.append(temp)
        if data:
            result["data"] = data

        return result
