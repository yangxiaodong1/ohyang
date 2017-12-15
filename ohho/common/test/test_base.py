import tornado.web
from ohho.common.test.constant import *
from ohho.common.db.ohho.base.db_ohho_country_code import DBOHHOCountryCode


class TestBase(tornado.web.RequestHandler):
    def initialize(self,
                   html_path,
                   action_url,
                   home_url=HOME_URL,
                   action_method="POST",
                   enctype="application/x-www-form-urlencoded"):
        self.html_path = html_path
        self.home_url = home_url
        self.action_url = action_url
        self.action_method = action_method
        self.enctype = enctype

    def post(self):
        pass

    def get(self):
        instance = DBOHHOCountryCode()
        country_codes = instance.get_query()
        country_codes = instance.order_by_id_asc(country_codes)
        self.render(self.html_path,
                    home_url=self.home_url,
                    action_url=self.action_url,
                    action_method=self.action_method,
                    enctype=self.enctype,
                    country_codes=country_codes
                    )
