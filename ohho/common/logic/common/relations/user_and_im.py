from ohho.common.db.im.db_ohho_im_user import DBOHHOIMUser


class UserAndIMRelation(object):
    @staticmethod
    def add(data):
        return DBOHHOIMUser.add(data)
