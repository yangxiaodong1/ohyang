from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.logic.common.permission.permission import OHHOPermission
from ohho.common.view.backstage.management.permission.constant import *
from ohho.common.view.backstage.constant import MANAGEMENT_PERMISSION_HOME_URL
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate

class BackstagePageListHandler(BaseHandler):
    def post(self):
        pass

    # @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        instance = OHHOPermission()
        name = the_get.get_name(self)
        if name is None:
            name = ""
        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        query = instance.page.get_all()

        if name:
            query = instance.page.get_by_name(query, name)

        query, count = instance.page.get_some(query, offset, limit)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()

        return self.render(PERMISSION_PAGE_BACKSTAGE_LIST_HTML,
                           page_querys=query,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           home_list_url=MANAGEMENT_PERMISSION_HOME_URL,
                           list_url=PERMISSION_PAGE_BACKSTAGE_LIST_URL,
                           detail_url=PERMISSION_PAGE_BACKSTAGE_DETAIL_URL,
                           add_url=PERMISSION_PAGE_BACKSTAGE_ADD_URL,
                           delete_url=PERMISSION_PAGE_BACKSTAGE_DELETE_URL,
                           name=name,
                           )
