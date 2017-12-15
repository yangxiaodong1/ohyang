from DB.mysql.models.ohho.cellphone.model_ohho_country_code import OHHOCountryCode
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_log import OHHOLog


class DBOHHOCountryCode(DBBase):
    def __init__(self, index=0):
        super(DBOHHOCountryCode, self).__init__(OHHOCountryCode, index)

    def get_by_country_code(self, country_code):
        query = self.get_query()
        query = Operation.filter(query, self.model.country_code, country_code)
        query = self.order_by_id_asc(query)
        return self.first(query)

    def get_by_country_name(self, country_name):
        query = self.get_query()
        query = Operation.ilike(query, self.model.country_name, country_name)
        return query

    def get_country_code_by_id(self, country_code_id):
        country_code = self.get_by_id(country_code_id)
        return country_code.country_code if country_code else "+86"
