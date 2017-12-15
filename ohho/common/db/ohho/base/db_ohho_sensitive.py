from DB.mysql.models.ohho.base.model_ohho_sensitive import OHHOSensitive
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOSensitive(DBBase):
    def __init__(self, index=0):
        super(DBOHHOSensitive, self).__init__(OHHOSensitive, index)

    def find_by_name(self, query, word):
        return Operation.ilike(query, self.model.word, word)

    if __name__ == "__main__":
        pass
