from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.logic.common.base.drink import Drink
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.view.backstage.constant import MANAGEMENT_BASE_HOME_URL


class BackstageDrinkListHandler(BaseHandler):
    def post(self):
        pass

    @authenticated
    def get(self):
        the_get = Get()
        instance = Drink()
        name = the_get.get_name(self)
        state = the_get.get_state(self)
        if name is None:
            name = ""
        if state is None:
            state = ""

        print("state", end=":")
        print(state)
        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        query = instance.get_all()

        if name:
            query = instance.find_by_name(query, name)
        if state:
            if state == "1":
                print("state is 1")
                query = instance.get_valid(query)
            else:
                print("state is not 1")
                query = instance.get_invalid(query)

        query, count = instance.get_some(query, offset, limit)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()

        return self.render(BASE_DRINK_LIST_HTML,
                           drinks=query,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           home_list_url=MANAGEMENT_BASE_HOME_URL,
                           list_url=BASE_DRINK_LIST_URL,
                           detail_url=BASE_DRINK_DETAIL_URL,
                           add_url=BASE_DRINK_ADD_URL,

                           name=name,
                           state=state
                           )
