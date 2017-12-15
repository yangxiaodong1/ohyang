from DB.mysql.models.ohho.user.model_ohho_user_display_configuration import OHHOUserDisplayConfiguration
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOUserDisplayConfiguration(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUserDisplayConfiguration, self).__init__(OHHOUserDisplayConfiguration, index)

    def find_by_distance(self, query, distance):
        return Operation.filter(query, self.model.distance, distance)

    def get_nearest_distance(self, distance):
        query = self.get_query()
        query = Operation.great_than_equal(query, self.model.distance, distance)
        query = self.order_by_id_asc(query)
        return Operation.first(query)

