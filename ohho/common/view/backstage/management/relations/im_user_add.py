from tornado.web import authenticated

from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.logic.common.im.user import User
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.relations.constant import *
from ohho.common.view.common.parameters import Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageIMUserAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        username = the_post.get_username(self)

        im_user_instance = User()
        user_instance = DBOHHOUser()

        user = user_instance.get_by_username(username)

        if user:
            success = im_user_instance.add_im(user.id)
            if success:
                return self.redirect(IM_USER_LIST_URL)

        return self.redirect(IM_USER_ADD_URL)

    @permission
    @backstage_authenticate
    def get(self):
        user_instance = DBOHHOUser()
        users_query = user_instance.get_query()
        users_query = user_instance.get_valid(users_query)
        return self.render(IM_USER_ADD_HTML,
                           add_url=IM_USER_ADD_URL,
                           list_url=IM_USER_LIST_URL,
                           users_query=users_query,
                           )
