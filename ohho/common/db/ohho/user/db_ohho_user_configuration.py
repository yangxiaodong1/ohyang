from DB.mysql.models.ohho.user.model_ohho_user_configuration import OHHOUserConfiguration
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOUserConfiguration(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUserConfiguration, self).__init__(OHHOUserConfiguration, index)

    def get_by_user(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        return Operation.first(query)

    def set_match(self, instance, is_match):
        obj_dict = {"is_match": is_match}
        return Operation.update(instance, obj_dict)

    def open_match(self, instance):
        return self.set_match(instance, True)

    def close_match(self, instance):
        return self.set_match(instance, False)

    def set_online(self, instance, is_online):
        obj_dict = {"is_online": is_online}
        return Operation.update(instance, obj_dict)

    def open_online(self, instance):
        return self.set_online(instance, True)

    def close_online(self, instance):
        return self.set_online(instance, False)
