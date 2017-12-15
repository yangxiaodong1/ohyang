from ohho.common.logic.common.user import User
from ohho.common.logic.common.result import Result


class LogicGetUserPersonalInformation(object):
    def __init__(self):
        self.user = User()

    def get(self, user_id, base_url=None):
        user = self.user.get_by_id(user_id)
        if user:
            result = Result.result_success()
            result["data"] = self.user.get_user_information(user_id, base_url)
        else:
            result = Result.result_failed("no such user!")
        return result
