from DB.mysql.models.ohho.relation.model_ohho_user_and_device_imei import OHHOUserAndDeviceIMEI
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_log import OHHOLog


class DBOHHOUserAndDeviceIMEI(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUserAndDeviceIMEI, self).__init__(OHHOUserAndDeviceIMEI, index)

    def get_by_imei(self, imei):
        try:
            query = self.get_query()
            query = Operation.filter(query, self.model.imei, imei)
            return Operation.first(query), None
        except Exception as ex:
            OHHOLog.print_log(ex)
            return True, ex

    def get_by_user_id(self, query, user_id):
        return Operation.filter(query, self.model.user_id, user_id)

    def get_first_by_device_id(self, device_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.device_id, device_id)
        query = self.order_by_id_asc(query)
        return self.first(query)

    def get_by_device_id(self, query, device_id):
        query = Operation.filter(query, self.model.device_id, device_id)
        query = self.order_by_id_asc(query)
        return self.first(query)

    def get_query_by_device_id(self, query, device_id):
        query = Operation.filter(query, self.model.device_id, device_id)
        query = self.order_by_id_asc(query)
        return query
