from tornado.web import authenticated

from ohho.common.logic.common.base.drink import Drink
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.base.constant import *

from ohho.common.view.common.parameters import Post
from ohho.common.logic.common.base.country_code import CountryCode
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageCountryCodeAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        country_name = the_post.get_name(self)
        country_code = the_post.get_country_code(self)
        instance = CountryCode()
        if country_name and country_code:
            if not str(country_code).strip().startswith("+"):
                country_code = "+" + str(country_code).strip()
            data = dict()
            data["country_name"] = country_name
            data["country_code"] = country_code
            success = instance.add(data)
            if success:
                return self.redirect(BASE_COUNTRY_CODE_BACKSTAGE_LIST_URL)

        return self.redirect(BASE_COUNTRY_CODE_BACKSTAGE_ADD_URL)

    @permission
    @backstage_authenticate
    def get(self):
        return self.render(BASE_COUNTRY_CODE_BACKSTAGE_ADD_HTML,
                           add_url=BASE_COUNTRY_CODE_BACKSTAGE_ADD_URL,
                           list_url=BASE_COUNTRY_CODE_BACKSTAGE_LIST_URL
                           )
