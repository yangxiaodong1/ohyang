from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.constant import MANAGEMENT_PERMISSION_HOME_HTML
from ohho.common.view.backstage.management.permission.constant import *
from tornado.web import authenticated


class BackstagePermissionHomeHandler(BaseHandler):
    def post(self):
        pass

    @authenticated
    def get(self):
        return self.render(MANAGEMENT_PERMISSION_HOME_HTML,
                           permission_group_backstage_list_url=PERMISSION_GROUP_BACKSTAGE_LIST_URL,
                           permission_page_backstage_list_url=PERMISSION_PAGE_BACKSTAGE_LIST_URL,

                           )
