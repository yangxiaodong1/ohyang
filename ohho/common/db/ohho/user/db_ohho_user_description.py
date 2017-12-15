from DB.mysql.models.ohho.user.model_ohho_user_description import OHHOUserDescription
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOUserDescription(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUserDescription, self).__init__(OHHOUserDescription, index)

    def get_by_user(self, query, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        return query

    def get_user_description_by_user_id(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        query = self.order_by_id_desc(query)
        return query

    def get_I_am(self, query):
        query = Operation.filter(query, self.model.type, 1)
        return query

    def get_I_am_by_user_id(self, user_id):
        query = self.get_user_description_by_user_id(user_id)
        query = self.get_I_am(query)
        query = self.first(query)
        return query

    def exist_description(self, description_object):
        if description_object and (description_object.first
                                   or description_object.second
                                   or description_object.third):
            return True
        else:
            return False

    def get_I_like(self, query):
        query = Operation.filter(query, self.model.type, 2)
        return query

    def get_I_like_by_user_id(self, user_id):
        query = self.get_user_description_by_user_id(user_id)
        query = self.get_I_like(query)
        query = self.first(query)
        return query

    def get_I_unlike(self, query):
        query = Operation.filter(query, self.model.type, 3)
        return query

    def get_I_unlike_by_user_id(self, user_id):
        query = self.get_user_description_by_user_id(user_id)
        query = self.get_I_unlike(query)
        query = self.first(query)
        return query

    def get_I_hope(self, query):
        query = Operation.filter(query, self.model.type, 4)
        return query

    def get_I_hope_by_user_id(self, user_id):
        query = self.get_user_description_by_user_id(user_id)
        query = self.get_I_hope(query)
        query = self.first(query)
        return query

    def add_I_am(self, data):
        data["type"] = 1
        return self.add(data)

    def add_I_like(self, data):
        data["type"] = 2
        return self.add(data)

    def add_I_unlike(self, data):
        data["type"] = 3
        return self.add(data)

    def add_I_hope_she_is(self, data):
        data["type"] = 4
        return self.add(data)


if __name__ == "__main__":
    pass
