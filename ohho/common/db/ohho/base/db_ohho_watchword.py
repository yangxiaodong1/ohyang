from DB.mysql.models.ohho.base.model_ohho_watchword import OHHOWatchword
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase

class DBOHHOWatchword(DBBase):
    def __init__(self, index=0):
        super(DBOHHOWatchword, self).__init__(OHHOWatchword, index)

    def find_by_first(self, query, first):
        return Operation.ilike(query, self.model.first, first)

    def find_by_second(self, query, second):
        return Operation.ilike(query, self.model.second, second)
