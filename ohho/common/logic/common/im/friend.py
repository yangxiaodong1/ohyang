from ohho.common.db.ohho.im.db_ohho_im_user_relation import DBOHHOIMUserRelation


class Friend(object):
    def __init__(self):
        self.relation = DBOHHOIMUserRelation()

    def get_valid_relation(self, query):
        return self.relation.get_by_state(query, True)

    def get_invalid_relation(self, query):
        return self.relation.get_by_state(query, False)

    def get_relation_by_user(self, user_id):
        query = self.relation.get_query()
        query = self.relation.get_valid(query, True)
        return self.relation.get_by_account(query, user_id)

    def get_relation_by_user_and_friend(self, user_id, friend_user_id):
        query = self.get_relation_by_user(user_id)
        return self.relation.get_by_friend(query, friend_user_id)

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

    def add_friend(self, relation):
        return self.relation.update_to_friend(relation)

    def add_black(self, relation):
        return self.relation.update_to_black(relation)

    def get_friends(self, user_id):
        query = self.get_relation_by_user(user_id)
        query = self.relation.get_friends(query)
        query = self.get_valid_relation(query)
        return query

    def get_blacks(self, user_id):
        query = self.get_relation_by_user(user_id)
        query = self.relation.get_blacks(query)
        query = self.get_valid_relation(query)
        return query
