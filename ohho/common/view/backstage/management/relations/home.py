from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.constant import MANAGEMENT_RELATION_HOME_HTML
from ohho.common.view.backstage.management.relations.constant import *
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination


class BackstageRelationHomeHandler(BaseHandler):
    def post(self):
        pass

    @authenticated
    def get(self):
        return self.render(MANAGEMENT_RELATION_HOME_HTML,
                           user_and_device_list_url=USER_AND_DEVICE_LIST_URL,
                           user_and_cellphone_list_url=USER_AND_CELLPHONE_LIST_URL,
                           im_user_list_url=IM_USER_LIST_URL,
                           user_and_match_condition_list_url=USER_AND_MATCH_CONDITION_LIST_URL
                           )
