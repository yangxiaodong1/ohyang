from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.permission.constant import *
from ohho.common.logic.common.base.drink import Drink
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from ohho.common.logic.common.permission.permission import OHHOPermission
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate

class BackstageGroupDetailHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        name = the_post.get_name(self)
        description = the_post.get_description(self)
        group_id = the_post.get_id(self)
        instance = OHHOPermission()
        group_obj = instance.group.get_by_id(group_id)
        submit = the_post.get_submit(self)
        success = False
        if submit:
            data = dict()
            data["name"] = name
            data["description"] = description
            success = instance.group.update(group_obj, data)

        if success:
            return self.redirect(PERMISSION_GROUP_BACKSTAGE_LIST_URL)
        return self.redirect(PERMISSION_GROUP_BACKSTAGE_DETAIL_URL + "?id=" + str(group_id))

    # @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        group_id = the_get.get_id(self)
        instance = OHHOPermission()
        if group_id:
            group_obj = instance.group.get_by_id(group_id)
        return self.render(PERMISSION_GROUP_BACKSTAGE_DETAIL_HTML,
                           group_obj=group_obj,
                           detail_url=PERMISSION_GROUP_BACKSTAGE_DETAIL_URL,
                           list_url=PERMISSION_GROUP_BACKSTAGE_LIST_URL
                           )
