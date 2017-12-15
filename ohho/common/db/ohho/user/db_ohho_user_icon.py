from DB.mysql.models.ohho.user.model_ohho_user_icon import OHHOUserIcon
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOUserIcon(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUserIcon, self).__init__(OHHOUserIcon, index)

    # def get_by_user(self, user_id):
    #     query = self.get_query()
    #     query = Operation.filter(query, self.model.user_id, user_id)
    #     query = self.order_by_id_desc(query)
    #     return self.first(query)

    def get_by_user(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        query = self.order_by_id_asc(query)
        query = self.get_all(query)
        return query

    def get_user_head_sculpture(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        query = Operation.filter(query, self.model.is_head_sculpture, 1)
        return self.first(query)


if __name__ == "__main__":
    pass
