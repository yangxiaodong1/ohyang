from Tools.ohho_random import OHHORandom
from ohho.common.db.ohho.user.db_ohho_user_token import DBOHHOUserToken


class Token(object):
    def __init__(self):
        self.token = DBOHHOUserToken()

    def add(self, user_id):
        token = OHHORandom.get_nonce()
        token_dict = dict()
        token_dict["user_id"] = user_id
        token_dict["token"] = token
        token_add = self.token.add(token_dict)
        if token_add:
            return self.token.get_by_user_id(user_id)
        else:
            return None

    def get(self, user_id):
        return self.token.get_by_user_id(user_id)

    def update(self, instance, data):
        return self.token.update(instance, data)

    def delete(self, instance):
        return self.token.delete(instance)
