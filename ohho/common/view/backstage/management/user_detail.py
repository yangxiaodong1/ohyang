from tornado.web import authenticated

from ohho.common.db.ohho.user.db_ohho_user_accuracy_extension import DBOHHOUserAccuracyExtension
from ohho.common.logic.common.user import User
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.constant import *
from ohho.common.view.common.parameters import Get, Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageUserDetailHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        user_id = the_post.get_user_id(self)
        submit = the_post.get_submit(self)
        delete_or_restore = the_post.get_delete_or_restore(self)

        instance = User()
        user = instance.get_by_id(user_id)

        detail_url = MANAGEMENT_USER_DETAIL_URL + "?user_id=" + str(user_id)
        if delete_or_restore and user:
            if user.state:
                success = instance.delete(user)
            else:
                success = instance.restore(user)
            if success:
                return self.redirect(MANAGEMENT_USER_LIST_URL)
            else:
                return self.redirect(detail_url)
        if submit:
            user_extension = the_post.get_user_extension(self)
            user_extension_instance = DBOHHOUserAccuracyExtension()
            user_extension_object = user_extension_instance.get_by_user(user_id)
            success = user_extension_instance.update(user_extension_object, user_extension)
            if success:
                return self.redirect(MANAGEMENT_USER_LIST_URL)
            else:
                return self.redirect(detail_url)
        return self.redirect(detail_url)

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        user_id = the_get.get_user_id(self)
        instance = User()
        user = instance.get_by_id(user_id)
        country_code = instance.country_code.get_query()
        user_extension = instance.get_user_extension_by_user(user_id)
        if not user_extension:
            user_extension = instance.init_user_extension(user_id)

        return self.render(MANAGEMENT_USER_DETAIL_HTML,
                           user=user, user_extension=user_extension, country_code_list=country_code)
