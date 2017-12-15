from tornado.web import authenticated

from ohho.common.logic.common.im.user import User as IMUser
from ohho.common.logic.common.user import User as OHHOUser
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.relations.constant import *
from ohho.common.view.common.parameters import Get, Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageIMUserDetailHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        username = the_post.get_username(self)
        token = the_post.get_token(self)
        name = the_post.get_name(self)
        im_user_id = the_post.get_id(self)
        submit = the_post.get_submit(self)
        # delete_or_restore = the_post.get_delete_or_restore(self)

        detail_url = IM_USER_DETAIL_URL + "?id=" + im_user_id

        ohho_user_instance = OHHOUser(username)
        im_user_instance = IMUser()

        user = ohho_user_instance.get_user()
        im_user = im_user_instance.get_by_id(im_user_id)

        if submit and im_user and user:
            data = dict()
            data["account_id"] = user.id
            data["token"] = token
            data["name"] = name
            success = im_user_instance.update(im_user, data)
            if success:
                return self.redirect(IM_USER_LIST_URL)
        # if delete_or_restore and im_user:
        #     if im_user.state is True:
        #         success = im_user_instance.delete(im_user)
        #     else:
        #         success = im_user_instance.restore(im_user)
        #     if success:
        #         return self.redirect(IM_USER_LIST_URL)
        return self.redirect(detail_url)

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        im_user_id = the_get.get_id(self)

        im_user_instance = IMUser()
        ohho_user_instance = OHHOUser()

        im_user = im_user_instance.get_by_id(im_user_id)
        username = ""
        token = ""
        name = ""
        if im_user:
            ohho_user = ohho_user_instance.get_by_id(im_user.account_id)
            username = ohho_user.username
            if im_user.token is not None:
                token = im_user.token
            if im_user.name is not None:
                name = im_user.name
            state = im_user.state

        return self.render(IM_USER_DETAIL_HTML,
                           username=username,
                           token=token,
                           name=name,
                           state=state,
                           im_user_id=im_user_id,
                           detail_url=IM_USER_DETAIL_URL,
                           list_url=IM_USER_LIST_URL
                           )
