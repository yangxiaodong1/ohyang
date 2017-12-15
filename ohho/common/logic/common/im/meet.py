from ohho.common.db.ohho.im.db_ohho_im_user_request_relation import DBOHHOIMUserRequestRelation
from ohho.common.db.ohho.record.db_ohho_record_friend_apply import DBOHHORecordFriendApply
from ohho.common.logic.common.result import Result
from Tools.ohho_datetime import OHHODatetime

MEET_STATE_NOT_MEET = 0
MEET_STATE_MEET = 1
MEET_STATE_APPLY = 2
MEET_STATE_AGREE = 3
MEET_STATE_REFUSE = 4
MEET_STATE_CANCEL = 5

FRIEND_STATE_DEFAULT = 0
FRIEND_STATE_APPLY = 2
FRIEND_STATE_AGREE = 3
FRIEND_STATE_REFUSE = 4

ONE_DAY_MICRO_SECONDS = 60 * 60 * 24 * 1000


class Meet(object):
    def __init__(self):
        self.apply = DBOHHORecordFriendApply()
        self.relation = DBOHHOIMUserRequestRelation()

    def get_relation_by_user(self, user_id):
        query = self.relation.get_query()
        return self.relation.get_by_account(query, user_id)

    def get_relation_by_friend(self, friend_user_id):
        query = self.relation.get_query()
        return self.relation.get_by_friend(query, friend_user_id)

    def get_relation_by_user_and_friend(self, user_id, friend_user_id):
        query = self.get_relation_by_user(user_id)
        return self.relation.get_by_friend(query, friend_user_id)

    def get_valid_relation(self, query):
        return self.relation.get_by_state(query, True)

    def friend_get_apply_list(self, query):
        return self.relation.get_by_friend_state(query, FRIEND_STATE_APPLY)

    def meet_get_apply_list(self, query):
        return self.relation.get_by_meet_state(query, MEET_STATE_APPLY)

    def get_apply_friend_list(self, user_id):
        timestamp = int(OHHODatetime.get_current_timestamp())
        query = self.apply.get_query()
        query = self.apply.get_by_another_user(query, user_id)
        # query = self.friend_get_apply_list(query)
        query = self.apply.get_great_than_equal_timestamp(query, timestamp - ONE_DAY_MICRO_SECONDS)
        # query = self.get_valid_relation(query)
        return query

    def get_apply_meet_list(self, user_id):
        query = self.get_relation_by_friend(user_id)
        query = self.meet_get_apply_list(query)
        query = self.get_valid_relation(query)
        return query

    def get_invalid_relation(self, query):
        return self.relation.get_by_state(query, False)

    def order_relation_by_id_asc(self, query):
        return self.relation.order_by_id_asc(query)

    def order_relation_by_id_desc(self, query):
        return self.relation.order_by_id_desc(query)

    def first_relation(self, query):
        return self.relation.first(query)

    def get_some_valid_relation(self, user_id, friend_user_id):
        query = self.get_relation_by_user_and_friend(user_id, friend_user_id)
        valid_query = self.get_valid_relation(query)
        sorted_valid_query = self.order_relation_by_id_asc(valid_query)
        relation = self.first_relation(sorted_valid_query)
        return relation

    def get_some_invalid_relation(self, user_id, friend_user_id):
        query = self.get_relation_by_user_and_friend(user_id, friend_user_id)
        invalid_query = self.get_invalid_relation(query)
        sorted_invalid_query = self.order_relation_by_id_asc(invalid_query)
        relation = self.first_relation(sorted_invalid_query)
        return relation

    def restore_relation(self, relation):
        return self.relation.restore(relation)

    def add_relation(self, user_id, friend_user_id):
        data = dict()
        data["account_id"] = user_id
        data["friend_account_id"] = friend_user_id
        self.relation.add(data)
        return self.get_some_valid_relation(user_id, friend_user_id)

    def create_or_get_relation(self, user_id, friend_user_id):
        relation = None
        if user_id and friend_user_id:
            relation = self.get_some_valid_relation(user_id, friend_user_id)
            if not relation:
                invalid_relation = self.get_some_invalid_relation(user_id, friend_user_id)
                if invalid_relation:
                    success = self.relation.restore(invalid_relation)
                    if success:
                        relation = self.get_some_valid_relation(user_id, friend_user_id)
                    else:
                        print("restore relation failed!")
                else:
                    relation = self.add_relation(user_id, friend_user_id)
        else:
            print("user_id or friend_user_id is invalid! user_id: %d, friend_user_id: %d" % (
                int(user_id), int(friend_user_id)
            ))
        return relation

    def basic_meet(self, relation, meet_state):
        if relation:
            success = self.relation.update_meet_state(relation, meet_state)
            if success:
                result = Result.result_success()
            else:
                result = Result.result_failed()
        else:
            result = Result.result_not_exist("no relation!")
        return result

    def apply_meet(self, relation):
        return self.basic_meet(relation, MEET_STATE_APPLY)

    def agree_meet(self, relation):
        return self.basic_meet(relation, MEET_STATE_AGREE)

    def refuse_meet(self, relation):
        return self.basic_meet(relation, MEET_STATE_REFUSE)

    def cancel_meet(self, relation):
        return self.basic_meet(relation, MEET_STATE_CANCEL)

    def meet(self, relation):
        return self.basic_meet(relation, MEET_STATE_MEET)

    def is_apply_meet(self, relation):
        return relation.meet_state == MEET_STATE_APPLY

    def is_agree_meet(self, relation):
        return relation.meet_state == MEET_STATE_AGREE

    def is_meet(self, relation):
        return relation.meet_state == MEET_STATE_MEET

    def basic_friend(self, relation, friend_state):
        if relation:
            print(relation)
            success = self.relation.update_friend_state(relation, friend_state)
            if success:
                result = Result.result_success()
            else:
                result = Result.result_failed()
        else:
            result = Result.result_not_exist()
        return result

    def apply_friend(self, relation):
        return self.basic_friend(relation, FRIEND_STATE_APPLY)

    def agree_friend(self, relation):
        return self.basic_friend(relation, FRIEND_STATE_AGREE)

    def refuse_friend(self, relation):
        return self.basic_friend(relation, FRIEND_STATE_REFUSE)

    def reset_friend(self, relation):
        return self.basic_friend(relation, FRIEND_STATE_DEFAULT)

    def is_apply_friend(self, relation):
        return relation.friend_state == FRIEND_STATE_APPLY

    def is_refuse_friend(self, relation):
        return relation.friend_state == FRIEND_STATE_REFUSE

    def get_by_meet(self, query):
        return self.relation.get_by_state(query, MEET_STATE_MEET)

    def get_meet(self, user_id, last_id):
        last_id = int(last_id)
        query = self.get_relation_by_user(user_id)
        query = self.get_by_meet(query)
        if last_id > 0:
            query = self.relation.get_less_than_id(query, last_id)
        query = self.order_relation_by_id_desc(query)
        # if int(limit) > 0:
        #     query = self.relation.limit(query, limit)
        query = self.relation.get_all(query)
        return query
