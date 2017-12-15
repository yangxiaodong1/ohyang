from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.drink import Drink
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from ohho.common.logic.common.base.country_code import CountryCode
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate

class BackstageCountryCodeDetailHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        country_code_id = the_post.get_id(self)
        country_name = the_post.get_name(self)
        country_code = the_post.get_country_code(self)
        instance = CountryCode()
        country_code_obj = instance.get(country_code_id)
        submit = the_post.get_submit(self)
        delete_or_restore = the_post.get_delete_or_restore(self)
        success = False
        if submit:
            data = dict()
            data["country_name"] = country_name
            data["country_code"] = country_code
            success = instance.update(country_code_obj, data)
        if delete_or_restore:
            success = instance.delete(country_code_obj)

        if success:
            return self.redirect(BASE_COUNTRY_CODE_BACKSTAGE_LIST_URL)
        return self.redirect(BASE_COUNTRY_CODE_BACKSTAGE_DETAIL_HTML + "?id=" + str(country_code_id))

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

        return self.render(BASE_COUNTRY_CODE_BACKSTAGE_DETAIL_HTML,
                           country_name=country_name,
                           country_code=country_code,
                           country_code_id=country_code_id,
                           detail_url=BASE_COUNTRY_CODE_BACKSTAGE_DETAIL_URL,
                           list_url=BASE_COUNTRY_CODE_BACKSTAGE_LIST_URL
                           )
