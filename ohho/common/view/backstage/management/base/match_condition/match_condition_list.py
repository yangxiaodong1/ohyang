from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.logic.common.record.match_condition import MatchCondition
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.view.backstage.constant import MANAGEMENT_BASE_HOME_URL


class BackstageMatchConditionListHandler(BaseHandler):
    def post(self):
        pass

    @authenticated
    def get(self):
        the_get = Get()
        instance = MatchCondition()
        sex = the_get.get_user_extension_sex(self)
        nickname = the_get.get_user_extension_nickname(self)
        if sex is None:
            sex = ""
        if nickname is None:
            nickname = ""

        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        query = instance.find(sex, nickname)

        query, count = instance.get_some(query, offset, limit)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()

        return self.render(BASE_MATCH_CONDITION_LIST_HTML,
                           match_conditions=query,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           home_list_url=MANAGEMENT_BASE_HOME_URL,
                           list_url=BASE_MATCH_CONDITION_LIST_URL,
                           detail_url=BASE_MATCH_CONDITION_DETAIL_URL,
                           add_url=BASE_MATCH_CONDITION_ADD_URL,

                           sex=sex,
                           nickname=nickname,
                           )
