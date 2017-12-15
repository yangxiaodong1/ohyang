from ohho.common.db.ohho.im.db_ohho_im_user import DBOHHOIMUser

from ohho.common.logic.common.user import User

from ohho.common.logic.ohho.detail_constant import *
from Tools.ohho_log import OHHOLog
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.logic.common.password import Password


class LogicBackstageRegister(object):
    def __init__(self):
        self.user = DBOHHOUser()
        self.password = Password()

    def register(self, username, password):
        if username and password:
            self.password.set_password(password)
            encryption_password = self.password.encryption()
            data = dict()
            data["username"] = username
            data["password"] = encryption_password
            success = self.user.add(data)
            if success:
                return True
        return False



if __name__ == "__main__":
    pass
