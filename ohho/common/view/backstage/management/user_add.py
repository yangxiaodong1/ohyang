from ohho.common.db.ohho.base.db_ohho_interest import DBOHHOInterest
from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.user import User
from tornado.web import authenticated
from ohho.common.view.backstage.constant import *
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate
from math import ceil
from ohho.common.view.common.pagination import Pagination


class BackstageUserAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        username = the_post.get_username(self)
        password = the_post.get_password(self)
        instance = User(username)

        result = instance.add_user(password)
        if result.get("code", 0) > 0:
            user_extension_dict = the_post.get_user_extension(self)
            user = instance.get_user()
            success = instance.add_user_extension(user.id, user_extension_dict)
            if success:
                return self.redirect(MANAGEMENT_USER_LIST_URL)
        return self.redirect(MANAGEMENT_USER_ADD_URL)

    @permission
    @backstage_authenticate
    def get(self):
        interest = DBOHHOInterest()
        work_content = interest.get_work_content()
        occupation = interest.get_occupation()
        return self.render(MANAGEMENT_USER_ADD_HTML,
                           work_content_list=work_content,
                           occupation_list=occupation)
