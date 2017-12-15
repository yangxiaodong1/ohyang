from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.cellphone import Cellphone
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from Tools.ohho_operation import OHHOOperation
from ohho.common.view.backstage.constant import *
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageCellphoneListHandler(BaseHandler):
    def post(self):
        pass

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        cellphone_manufacturer = the_get.get_cellphone_manufacturer(self)
        if cellphone_manufacturer is None:
            cellphone_manufacturer = ""
        platform_type = the_get.get_cellphone_platform_type(self)
        if platform_type is None:
            platform_type = ""
        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        cellphone = Cellphone()
        query = cellphone.get_all_cellphone()
        if cellphone_manufacturer:
            query = cellphone.find_by_manufacturer(query, cellphone_manufacturer)

        if platform_type:
            query = cellphone.find_by_platform(query, platform_type)

        cellphones, count = cellphone.get_some_cellphones(query, offset, limit)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()

        # return self.render("backstage/management/cellphone_list.html",
        return self.render(MANAGEMENT_CELLPHONE_LIST_HTML,
                           cellphones=cellphones,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           cellphone_manufacturer=cellphone_manufacturer,
                           platform_type=platform_type,
                           detail_url=MANAGEMENT_CELLPHONE_DETAIL_URL,
                           delete_url=MANAGEMENT_CELLPHONE_DELETE_URL
                           )
