from DB.mysql.models.ohho.user.model_ohho_user_token import OHHOUserToken
from DB.common.operation import Operation
from Tools.ohho_random import OHHORandom
from Tools.ohho_operation import OHHOOperation
from ohho.common.db.db_base import DBBase


class DBOHHOUserToken(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUserToken, self).__init__(OHHOUserToken, index)

    def get_by_user_id(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        return Operation.first(query)
