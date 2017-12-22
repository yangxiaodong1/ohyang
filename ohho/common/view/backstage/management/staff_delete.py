from tornado.web import authenticated

from ohho.common.db.ohho.user.db_ohho_user_accuracy_extension import DBOHHOUserAccuracyExtension
from ohho.common.logic.common.staff import Staff
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.constant import *
from ohho.common.view.common.parameters import Get, Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageStaffDeleteHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        staff_id = the_post.get_staff_id(self)
        delete_or_restore = the_post.get_delete_or_restore(self)

        instance = Staff()
        staff = instance.get_by_id(staff_id)

        delete_url = MANAGEMENT_STAFF_DELETE_URL + "?staff_id=" + str(staff_id)
        if delete_or_restore and staff:
            if staff.state:
                success = instance.delete(staff)
            else:
                success = instance.restore(staff)
            if success:
                return self.redirect(MANAGEMENT_STAFF_LIST_URL)
            else:
                return self.redirect(delete_url)

        return self.redirect(delete_url)

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        staff_id = the_get.get_staff_id(self)
        instance = Staff()
        staff = instance.get_by_id(staff_id)
        country_code = instance.country_code.get_query()

        return self.render(MANAGEMENT_STAFF_DELETE_HTML,
                           staff=staff,
                           country_code_list=country_code)
