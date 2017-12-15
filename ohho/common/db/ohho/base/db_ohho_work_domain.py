from DB.mysql.models.ohho.base.model_ohho_work_domain import OHHOWorkDomain
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOWorkDomain(DBBase):
    def __init__(self, index=0):
        super(DBOHHOWorkDomain, self).__init__(OHHOWorkDomain, index)

    def get_by_parent_id(self, parent_id):
        query = self.get_query()
        query = self.get_valid(query)
        return Operation.filter(query, self.model.parent_id, parent_id)

    def get_level_1(self):
        return self.get_by_parent_id(1)

    def find_by_name(self, query, name):
        return Operation.ilike(query, self.model.name, name)

    def delete(self, instance):
        return super(DBOHHOWorkDomain, self).delete(instance, True)

    def restore(self, instance):
        return super(DBOHHOWorkDomain, self).restore(instance, True)

    def get_valid(self, query):
        return super(DBOHHOWorkDomain, self).get_valid(query, True)

    def get_invalid(self, query):
        return super(DBOHHOWorkDomain, self).get_invalid(query, True)

    def get_information(self, instance):
        result = dict()
        result["name"] = instance.name
        result["id"] = instance.id
        return result


if __name__ == "__main__":
    domain = DBOHHOWorkDomain()
    result = domain.get_by_parent_id(None)
    print(result.count())
