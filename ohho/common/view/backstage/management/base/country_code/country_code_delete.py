from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.drink import Drink
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from ohho.common.logic.common.base.country_code import CountryCode
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate

class BackstageCountryCodeDeleteHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        country_code_id = the_post.get_id(self)
        instance = CountryCode()
        country_code_obj = instance.get(country_code_id)
        delete_or_restore = the_post.get_delete_or_restore(self)
        success = False
        if delete_or_restore:
            success = instance.delete(country_code_obj)
        if success:
            return self.redirect(BASE_COUNTRY_CODE_BACKSTAGE_LIST_URL)
        return self.redirect(BASE_COUNTRY_CODE_BACKSTAGE_DELETE_HTML + "?id=" + str(country_code_id))

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        country_code_id = the_get.get_id(self)
        name = ""
        instance = CountryCode()
        if country_code_id:
            country_code = instance.get(country_code_id)
            country_name = country_code.country_name
            country_code = country_code.country_code

        return self.render(BASE_COUNTRY_CODE_BACKSTAGE_DELETE_HTML,
                           country_name=country_name,
                           country_code=country_code,
                           country_code_id=country_code_id,
                           detail_url=BASE_COUNTRY_CODE_BACKSTAGE_DETAIL_URL,
                           list_url=BASE_COUNTRY_CODE_BACKSTAGE_LIST_URL,
                           delete_url=BASE_COUNTRY_CODE_BACKSTAGE_DELETE_URL,
                           )
