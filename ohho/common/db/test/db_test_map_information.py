from DB.mysql.models.ohho.test.model_test_map_information import TestMapInformation as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBTestMapInformation(DBBase):
    def __init__(self):
        super(DBTestMapInformation, self).__init__(model)

    def get_by_user_id(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        query = self.order_by_id_desc(query)
        return self.first(query)
