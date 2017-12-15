from DB.mysql.models.ohho.im.ohho_im_user_relation import OHHOIMUserRelation
from ohho.common.db.im.constant import *
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from sqlalchemy import or_


class DBOHHOIMUserRelation(DBBase):
    def __init__(self):
        super(DBOHHOIMUserRelation, self).__init__(OHHOIMUserRelation)

    def get_by_apply(self, apply_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.apply_id, apply_id)
        query = self.order_by_id_desc(query)
        return self.first(query)

    def get_by_account(self, query, account_id):
        return Operation.filter(query, self.model.account_id, account_id)

    def get_by_friend(self, query, friend_account_id):
        return Operation.filter(query, self.model.friend_account_id, friend_account_id)

    def get_friends(self, query):
        return Operation.filter(query, self.model.type, TYPE_FRIEND)

    def get_by_user(self, query, user_id):
        return query.filter(or_(self.model.account_id == user_id, self.model.friend_account_id == user_id))

    def get_blacks(self, query):
        return Operation.filter(query, self.model.type, TYPE_BLACK)

    def is_friend(self, instance):
        if instance:
            return instance.type == TYPE_FRIEND
        else:
            return False

    def is_black(self, instance):
        if instance:
            return instance.type == TYPE_BLACK
        else:
            return False

    def update_type(self, instance, type):
        obj_dict = dict()
        obj_dict["type"] = type
        return Operation.update(instance, obj_dict)

    def update_to_friend(self, instance):
        return self.update_type(instance, TYPE_FRIEND)

    def update_to_black(self, instance):
        return self.update_type(instance, TYPE_BLACK)

    def get_less_than_id(self, query, id):
        return Operation.less_than(query, self.model.id, id)

    def delete(self, instance):
        return super(DBOHHOIMUserRelation, self).delete(instance, True)

    def restore(self, instance):
        return super(DBOHHOIMUserRelation, self).restore(instance, True)
