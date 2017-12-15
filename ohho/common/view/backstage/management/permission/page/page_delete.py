from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.permission.constant import *
from ohho.common.logic.common.base.drink import Drink
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from ohho.common.logic.common.permission.permission import OHHOPermission
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate

class BackstagePageDeleteHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        page_id = the_post.get_id(self)
        instance = OHHOPermission()
        page_obj = instance.page.get_by_id(page_id)
        delete_or_restore = the_post.get_delete_or_restore(self)
        success = False
        if delete_or_restore:
            success = instance.page.delete(page_obj)

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
        return self.render(PERMISSION_PAGE_BACKSTAGE_DELETE_HTML,
                           page_obj=page_obj,
                           detail_url=PERMISSION_PAGE_BACKSTAGE_DETAIL_URL,
                           delete_url=PERMISSION_PAGE_BACKSTAGE_DELETE_URL,
                           list_url=PERMISSION_PAGE_BACKSTAGE_LIST_URL
                           )
