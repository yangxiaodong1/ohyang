from DB.mysql.models.ohho.base.model_ohho_profession import OHHOProfession
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOProfession(DBBase):
    def __init__(self, index=0):
        super(DBOHHOProfession, self).__init__(OHHOProfession, index)

    def find_by_name(self, query, name):
        return Operation.ilike(query, self.model.name, name)

    def delete(self, instance):
        return super(DBOHHOProfession, self).delete(instance, True)

    def restore(self, instance):
        return super(DBOHHOProfession, self).restore(instance, True)

    def get_valid(self, query):
        return super(DBOHHOProfession, self).get_valid(query, True)

    def get_invalid(self, query):
        return super(DBOHHOProfession, self).get_invalid(query, True)

    def get_information(self, instance):
        result = dict()
        result["name"] = instance.name
        result["id"] = instance.id
        return result


if __name__ == "__main__":
    pass
