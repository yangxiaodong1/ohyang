from DB.mysql.models.ohho.match.model_ohho_match_condition import OHHOMatchCondition
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOMatchCondition(DBBase):
    def __init__(self, index=0):
        super(DBOHHOMatchCondition, self).__init__(OHHOMatchCondition, index)

    def get_by_user(self, user_id):
        query = DBOHHOMatchCondition.get_query()
        return Operation.filter(query, self.model.user_id, user_id)

    def get_by_name(self, query, name):
        return Operation.filter(query, self.model.name, name)


if __name__ == "__main__":
    identity_id = 123456789
