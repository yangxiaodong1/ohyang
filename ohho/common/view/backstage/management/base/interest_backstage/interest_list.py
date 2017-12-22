from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.logic.common.base.watchword import Watchword
from ohho.common.logic.common.base.interest_backstage import InterestBackstage
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.view.backstage.constant import MANAGEMENT_BASE_HOME_URL
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageInterestListHandler(BaseHandler):
    def post(self):
        pass

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        instance = InterestBackstage()
        page = the_get.get_page(self)
        submit = the_get.get_submit(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        parent_id = the_get.get_id(self)
        if not parent_id:
            parent_id = 1
        name = the_get.get_name(self)
        # OHHOLog.print_log(submit)
        if submit:
            query = instance.get_all()
        else:
            query = instance.get_by_parent_id(parent_id)

        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        if name is not None:
            query = instance.find_by_name(query, name)
        else:
            name = ""

        query, count = instance.get_some(query, offset, limit)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()

        return self.render(BASE_INTEREST_BACKSTAGE_LIST_HTML,
                           interests=query,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           home_list_url=MANAGEMENT_BASE_HOME_URL,
                           list_url=BASE_INTEREST_BACKSTAGE_LIST_URL,
                           detail_url=BASE_INTEREST_BACKSTAGE_DETAIL_URL,
                           add_url=BASE_INTEREST_BACKSTAGE_ADD_URL,
                           delete_url=BASE_INTEREST_BACKSTAGE_DELETE_URL,
                           name=name,
                           parent_id=parent_id,
                           )