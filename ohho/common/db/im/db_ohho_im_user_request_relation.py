from DB.mysql.models.ohho.im.ohho_im_user_request_relation import OHHOIMUserRequestRelation
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOIMUserRequestRelation(DBBase):
    def __init__(self):
        super(DBOHHOIMUserRequestRelation, self).__init__(OHHOIMUserRequestRelation)

    def get_great_than_equal_timestamp(self, query, timestamp):
        return Operation.great_than_equal(query, self.model.timestamp, timestamp)

    def get_less_than_timestamp(self, query, timestamp):
        return Operation.less_than(query, self.model.timestamp, timestamp)

    def get_less_than_id(self, query, id):
        return Operation.less_than(query, self.model.id, id)

    def get_by_account(self, query, account_id):
        return Operation.filter(query, self.model.account_id, account_id)

    def get_by_friend(self, query, friend_account_id):
        return Operation.filter(query, self.model.friend_account_id, friend_account_id)

    def get_by_meet_state(self, query, meet_state):
        return Operation.filter(query, self.model.meet_state, meet_state)

    def get_by_friend_state(self, query, friend_state):
        return Operation.filter(query, self.model.friend_state, friend_state)

    def update_meet_state(self, instance, meet_state):
        obj_dict = dict()
        obj_dict["meet_state"] = meet_state
        return Operation.update(instance, obj_dict)

    def update_friend_state(self, instance, friend_state):
        obj_dict = dict()
        obj_dict["friend_state"] = friend_state
        return Operation.update(instance, obj_dict)

    def delete(self, instance):
        return super(DBOHHOIMUserRequestRelation, self).delete(instance, True)

    def restore(self, instance):
        return super(DBOHHOIMUserRequestRelation, self).restore(instance, True)
