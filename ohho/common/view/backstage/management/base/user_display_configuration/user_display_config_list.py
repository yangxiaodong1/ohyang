from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.logic.common.base.user_display_configuration import UserDisplayConfiguration
from ohho.common.logic.common.base.drink import Drink
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.view.backstage.constant import MANAGEMENT_BASE_HOME_URL


class BackstageUserDisplayConfigListHandler(BaseHandler):
    """用户配置列表展示"""
    def post(self):
        pass
    @authenticated
    def get(self):
        the_get = Get()
        instance = UserDisplayConfiguration()
        drink = Drink()
        drinks = drink.get_all()

        distance = the_get.get_distance(self)
        if distance is None:
            distance = ""
        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        query = instance.get_all()
        if distance:
            query = instance.find_by_distance(query,distance)
        query, count = instance.get_some(query, offset, limit)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()

        return self.render(BASE_USER_DISPLAY_CONFIG_LIST_HTML,
                           userConfigs=query,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           home_list_url=MANAGEMENT_BASE_HOME_URL,
                           list_url=BASE_USER_DISPLAY_CONFIG_LIST_URL,
                           detail_url=BASE_USER_DISPLAY_CONFIG_DETAIL_URL,
                           add_url=BASE_USER_DISPLAY_CONFIG_ADD_URL,

                           distance=distance,

                           )




