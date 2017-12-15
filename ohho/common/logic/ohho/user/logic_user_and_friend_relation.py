
from Tools.ohho_log import OHHOLog
from ohho.common.logic.common.user import User


class LogicGetUserAndFriendRelation(object):
    @staticmethod
    def get_user_and_friend_relation(user_id, friend_id):
        """个人主页判断是不是朋友关系"""
        user = User()
        temp_relation = user.get_user_and_friend_relation(user_id, friend_id)
        if temp_relation:
            relation = 1
        else:
            relation = 0
        return relation



if __name__ == "__main__":
    pass
