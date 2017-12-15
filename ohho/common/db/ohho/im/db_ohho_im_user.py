from DB.mysql.models.ohho.im.ohho_im_user import OHHOIMUser
from ohho.common.db.im.constant import *
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOIMUser(DBBase):
    def __init__(self, index=0):
        super(DBOHHOIMUser, self).__init__(OHHOIMUser, index)

    def get_by_account(self, query, account_id):
        return Operation.filter(query, self.model.account_id, account_id)

    def find_by_account(self, query, account_id_list):
        return Operation.in_(query, self.model.account_id, account_id_list)

    def get_by_friend(self, query, friend_account_id):
        return Operation.filter(query, self.model.friend_account_id, friend_account_id)

    def get_friends(self, query):
        return Operation.filter(query, self.model.type, TYPE_FRIEND)

    def get_blacks(self, query):
        return Operation.filter(query, self.model.type, TYPE_BLACK)

    def get_by_state(self, query, state):
        return Operation.filter(query, self.model.state, state)

    def update_type(self, instance, im_type):
        obj_dict = dict()
        obj_dict["type"] = im_type
        return Operation.update(instance, obj_dict)

    def update_to_friend(self, instance):
        return self.update_type(instance, TYPE_FRIEND)

    def update_to_black(self, instance):
        return self.update_type(instance, TYPE_BLACK)

    def delete(self, instance):
        obj_dict = {"state": 0}
        return Operation.update(instance, obj_dict)

    def restore(self, instance):
        obj_dict = {"state": 1}
        return Operation.update(instance, obj_dict)
