from ohho.common.db.ohho.im.db_ohho_im_user import DBOHHOIMUser
from ohho.common.db.ohho.user.db_ohho_user_configuration import DBOHHOUserConfiguration



class LogicGetUserConfiguration(object):
    def __init__(self):
        self.configuration = DBOHHOUserConfiguration()

    def is_on_online(self, user_id):
        conf_obj = self.configuration.get_by_user(user_id)
        if conf_obj:
            is_online = conf_obj.is_online
        else:
            is_online = 0
        return is_online

if __name__ == "__main__":
    pass
