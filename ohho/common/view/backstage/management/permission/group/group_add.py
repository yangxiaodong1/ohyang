from tornado.web import authenticated

from ohho.common.logic.common.base.drink import Drink
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.permission.constant import *

from ohho.common.view.common.parameters import Post
from ohho.common.view.common.parameters import Get
from ohho.common.logic.common.permission.permission import OHHOPermission
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageGroupAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        name = the_post.get_name(self)
        description = the_post.get_description(self)
        data = dict()
        instance = OHHOPermission().group

        if name:
            data["name"] = name
            if description:
                data["description"] = description
            success = instance.add(data)
            if success:
                return self.redirect(PERMISSION_GROUP_BACKSTAGE_LIST_URL)

        return self.redirect(PERMISSION_GROUP_BACKSTAGE_ADD_URL)
    # @permission
    @backstage_authenticate
    def get(self):
        return self.render(PERMISSION_GROUP_BACKSTAGE_ADD_HTML,
                           add_url=PERMISSION_GROUP_BACKSTAGE_ADD_URL,
                           list_url=PERMISSION_GROUP_BACKSTAGE_LIST_URL,
                           )
