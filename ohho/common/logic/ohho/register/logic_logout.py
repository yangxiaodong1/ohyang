from ohho.common.logic.common.result import Result
from ohho.common.logic.common.token import Token


class LogicLogout(object):
    def __init__(self):
        self.token = Token()

    def logout(self, user_id, token):
        result = dict()
        result["success"] = False
        token_object = self.token.get(user_id)
        if token_object and token_object.token == token:
            delete_token = self.token.delete(token_object)
            if delete_token:
                result = Result.result_success()
            else:
                result = Result.result_failed()
        else:
            result = Result.get_result(False, -2, -2, "you have no right to logout!")
        return result


if __name__ == "__main__":
    user_id = 2
    print(LogicLogout.logout(user_id))
