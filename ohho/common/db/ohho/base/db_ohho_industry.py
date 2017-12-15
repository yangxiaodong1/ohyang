from DB.mysql.models.ohho.base.model_ohho_industry import OHHOIndustry
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOIndustry(DBBase):
    def __init__(self, index=0):
        super(DBOHHOIndustry, self).__init__(OHHOIndustry, index)

    def find_by_name(self, query, name):
        return Operation.ilike(query, self.model.name, name)

    def delete(self, instance):
        return super(DBOHHOIndustry, self).delete(instance, True)

    def restore(self, instance):
        return super(DBOHHOIndustry, self).restore(instance, True)

    def get_valid(self, query):
        return super(DBOHHOIndustry, self).get_valid(query, True)

    def get_invalid(self, query):
        return super(DBOHHOIndustry, self).get_invalid(query, True)


if __name__ == "__main__":
    pass
