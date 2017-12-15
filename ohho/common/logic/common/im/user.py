from ohho.common.db.im.db_ohho_im_user import DBOHHOIMUser
from ohho.common.logic.common.im.netease.create import Create
from ohho.common.logic.common.im.netease.refresh_token import RefreshToken


class User(object):
    def __init__(self):
        self.im_user = DBOHHOIMUser()

    def delete(self, im_user):
        return self.im_user.delete(im_user)

    def restore(self, im_user):
        return self.im_user.restore(im_user)

    def get_by_id(self, im_user_id):
        return self.im_user.get_by_id(im_user_id)

    def get_all(self):
        return self.im_user.get_query()

    def find_by_account(self, query, account_id_list):
        return self.im_user.find_by_account(query, account_id_list)

    def get_some(self, query, offset, limit):
        return self.im_user.get_some(query, offset, limit)

    def add_im(self, user_id):
        query = self.im_user.get_query()
        im_user = self.im_user.get_by_account(query, user_id)
        im_user = self.im_user.first(im_user)
        if im_user:
            if not im_user.state:
                success = self.im_user.restore(im_user)
                if success:
                    return True
                else:
                    return False
            else:
                return True
        else:
            success = Create.add(user_id)
            if success:
                return True
            else:
                return RefreshToken.create_or_update(user_id)

    def update(self, instance, data):
        return self.im_user.update(instance, data)
