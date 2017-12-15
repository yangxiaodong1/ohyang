from ohho.common.db.ohho.db_ohho_user_token import DBOHHOUserToken


class Permission(object):
    @staticmethod
    def permission(user_id, token):
        token_object = DBOHHOUserToken.get_by_user_id(user_id)
        if token_object:
            if token_object.token == token:
                return True
        return False


if __name__ == "__main__":
    user_id = 2
    token = "1fczrxn58ylsgbpk3hutv96aow2id0ej"
    print(Permission.permission(user_id, token))
