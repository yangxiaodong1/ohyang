from tornado.web import authenticated

from ohho.common.db.ohho.user.db_ohho_user_accuracy_extension import DBOHHOUserAccuracyExtension
from ohho.common.logic.common.staff import Staff
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.constant import *
from ohho.common.view.common.parameters import Get, Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageStaffDetailHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        staff_id = the_post.get_staff_id(self)
        username = the_post.get_username(self)
        country_code = the_post.get_country_code(self)
        cellphone = the_post.get_cellphone_number(self)
        submit = the_post.get_submit(self)

        instance = Staff()
        staff = instance.get_by_id(staff_id)
        detail_url = MANAGEMENT_STAFF_DETAIL_HTML + "?staff_id=" + str(staff_id)
        if submit:
            data = dict()
            data["username"] = username
            data["country_code_id"] = country_code
            data["cellphone"] = cellphone
            success = instance.update_staff(staff, data)
            if success:
                return self.redirect(MANAGEMENT_STAFF_LIST_URL)

        return self.redirect(detail_url)

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        staff_id = the_get.get_staff_id(self)
        instance = Staff()
        staff = instance.get_by_id(staff_id)
        country_code = instance.country_code.get_query()

        return self.render(MANAGEMENT_STAFF_DETAIL_HTML,
                           staff=staff,
                           country_code_list=country_code)
