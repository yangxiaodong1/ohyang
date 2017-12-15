from DB.mysql.models.ohho.relation.model_ohho_user_and_device_relation import OHHOUserAndDeviceRelation
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOUserAndDeviceRelation(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUserAndDeviceRelation, self).__init__(OHHOUserAndDeviceRelation, index)

    def get_by_device(self, device_id):
        query = self.get_query()
        query = self.get_valid(query)
        query = Operation.filter(query, self.model.device_id, device_id)
        query = self.order_by_id_desc(query)
        return Operation.first(query)

    def get_valid_by_device(self, device_id):
        query = self.get_query()
        query = self.get_valid(query)
        query = Operation.filter(query, self.model.device_id, device_id)
        query = self.order_by_id_desc(query)
        return query

    def find_by_device(self, query, device_id_list):
        return Operation.filter(query, self.model.device_id, device_id_list)

    def get_valid(self, query):
        return super(DBOHHOUserAndDeviceRelation, self).get_valid(query, True)

    def get_invalid(self, query):
        return super(DBOHHOUserAndDeviceRelation, self).get_invalid(query, True)

    def get_by_user(self, query, user_id):
        return Operation.filter(query, self.model.user_id, user_id)

    def get_primary(self, query, primary_type=1):
        return self.get_by_type(query, primary_type)

    def get_by_type(self, query, type):
        return Operation.filter(query, self.model.type, type)

    def get_by_is_lost(self, query, is_lost):
        return Operation.filter(query, self.model.is_lost, is_lost)

    def get_lost(self, query):
        return Operation.filter(query, self.model.is_lost, True)

    def get_not_lost(self, query):
        return Operation.filter(query, self.model.is_lost, False)

    def set_lost(self, query):
        if query:
            for instance in query:
                Operation.update(instance, {"is_lost": True})
            return True
        return False

    def cancel_lost(self, query):
        if query:
            for instance in query:
                Operation.update(instance, {"is_lost": False})
            return True
        return False
        # return Operation.update_all(query, {"is_lost": True})

    def set_find(self, query):
        return Operation.update(query, {"is_lost": False})

    def find_by_user(self, query, user_id_list):
        return Operation.in_(query, self.model.user_id, user_id_list)

    def delete(self, instance):
        return super(DBOHHOUserAndDeviceRelation, self).delete(instance, True)

    def delete_some(self, query):
        for instance in query:
            self.delete(instance)

    def restore(self, instance):
        return super(DBOHHOUserAndDeviceRelation, self).restore(instance, True)
