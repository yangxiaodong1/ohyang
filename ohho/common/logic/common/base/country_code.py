from ohho.common.db.ohho.base.db_ohho_country_code import DBOHHOCountryCode
from ohho.common.logic.common.base.base_class import BaseClass


class CountryCode(BaseClass):
    def __init__(self):
        super(CountryCode, self).__init__(DBOHHOCountryCode)

    def get_by_country_name(self, country_name):
        query = self.instance.get_by_country_name(country_name)
        return query