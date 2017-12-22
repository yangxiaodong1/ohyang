from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.staff import Staff
from ohho.common.view.backstage.constant import *
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageStaffAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        username = the_post.get_username(self)
        password = the_post.get_password(self)
        cellphone = the_post.get_cellphone_number(self)
        country_code = the_post.get_country_code(self)
        instance = Staff(username)

        result = instance.add_staff(password, cellphone, country_code)
        if result:
            return self.redirect(MANAGEMENT_STAFF_LIST_URL)
        return self.redirect(MANAGEMENT_STAFF_ADD_HTML)

    @permission
    @backstage_authenticate
    def get(self):
        instance = Staff()
        country_code = instance.country_code.get_query()
        return self.render(MANAGEMENT_STAFF_ADD_HTML,
                           country_code_list=country_code,
                           )
