from DB.mysql.models.ohho.map.model_ohho_map_information import OHHOMapInformation
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOMapInformation(DBBase):
    def __init__(self, index=0):
        super(DBOHHOMapInformation, self).__init__(OHHOMapInformation, index)

    def filter_by_geohash_code(self, query, code_list):
        return Operation.in_(query, self.model.geohash_code, code_list)

    def filter_by_user(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        return query

    def get_by_user(self, user_id):
        query = self.filter_by_user(user_id)
        query = self.order_by_id_desc(query)
        return self.first(query)

    def get_information(self, instance):
        try:
            data = super(DBOHHOMapInformation, self).get_information(instance)
            data["longitude"] = float(instance.longitude)
            data["latitude"] = float(instance.latitude)
        except:
            data = dict()
        return data


if __name__ == "__main__":
    pass
