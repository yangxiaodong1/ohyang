from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.permission.constant import *
from ohho.common.logic.common.base.drink import Drink
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from ohho.common.logic.common.permission.permission import OHHOPermission
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate

class BackstagePageDetailHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        name = the_post.get_name(self)
        description = the_post.get_description(self)
        page_id = the_post.get_id(self)
        instance = OHHOPermission()
        page_obj = instance.page.get_by_id(page_id)
        submit = the_post.get_submit(self)
        success = False
        if submit:
            data = dict()
            data["name"] = name
            data["description"] = description
            success = instance.page.update(page_obj, data)

        if success:
            return self.redirect(PERMISSION_PAGE_BACKSTAGE_LIST_URL)
        return self.redirect(PERMISSION_PAGE_BACKSTAGE_DETAIL_URL + "?id=" + str(page_id))

    # @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        page_id = the_get.get_id(self)
        instance = OHHOPermission()
        if page_id:
            page_obj = instance.page.get_by_id(page_id)
        return self.render(PERMISSION_PAGE_BACKSTAGE_DETAIL_HTML,
                           page_obj=page_obj,
                           detail_url=PERMISSION_PAGE_BACKSTAGE_DETAIL_URL,
                           list_url=PERMISSION_PAGE_BACKSTAGE_LIST_URL
                           )
