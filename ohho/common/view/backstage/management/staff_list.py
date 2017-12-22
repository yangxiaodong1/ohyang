from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.staff import Staff
from Tools.decorator import permission
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.view.backstage.constant import *
from Tools.decorator import backstage_authenticate


class BackstageStaffListHandler(BaseHandler):
    def post(self):
        pass

    @backstage_authenticate
    @permission
    def get(self):
        the_get = Get()
        cellphone = the_get.get_cellphone_number(self)
        if cellphone is None:
            cellphone = ""
        state = the_get.get_state(self)
        if state is None:
            state = ""
        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        instance = Staff()

        if cellphone:
            query = instance.find_by_cellphone(cellphone)
        else:
            query = instance.get_all()
        try:
            if state == "":
                pass
            elif int(state):
                query = instance.get_valid(query)
            else:
                query = instance.get_invalid(query)
        except Exception as ex:
            pass
        staffs, count = instance.get_some_staffs(query, offset, limit)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()

        return self.render(MANAGEMENT_STAFF_LIST_HTML,
                           staffs=staffs,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           cellphone_number=cellphone,
                           state=state,
                           detail_url=MANAGEMENT_STAFF_DETAIL_URL,
                           delete_url=MANAGEMENT_STAFF_DELETE_URL,
                           )
