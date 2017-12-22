from DB.mysql.models.ohho.base.model_ohho_hint import OHHOHint
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_log import OHHOLog


class DBOHHOHint(DBBase):
    def __init__(self, index=0):
        super(DBOHHOHint, self).__init__(OHHOHint, index)

    def get_by_key(self, key):
        query = self.get_query()
        query = Operation.filter(query, self.model.key, key)
        query = self.order_by_id_desc(query)
        return self.first(query)

    def get_by_parent_id(self, parent_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.parent_id, parent_id)
        return query

    def find_by_name(self, query, name):
        return Operation.ilike(query, self.model.name, name)

    def get_root(self):
        query = self.get_query()
        query = Operation.filter(query, self.model.parent_id, None)
        return query


if __name__ == "__main__":
    pass
