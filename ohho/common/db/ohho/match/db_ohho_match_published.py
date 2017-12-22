from DB.mysql.models.ohho.match.model_ohho_match_published import OHHOMatchPublished
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOMatchPublished(DBBase):
    def __init__(self, index=0):
        super(DBOHHOMatchPublished, self).__init__(OHHOMatchPublished, index)

    def get_by_user(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        return query

    def get_the_last_by_user(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        query = self.order_by_id_desc(query)
        return self.first(query)


if __name__ == "__main__":
    identity_id = 123456789
