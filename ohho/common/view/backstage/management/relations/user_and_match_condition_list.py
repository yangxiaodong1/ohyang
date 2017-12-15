from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.logic.common.user import User
from ohho.common.logic.common.relations.user_and_cellphone import UserAndCellphoneRelation
from ohho.common.logic.common.cellphone import Cellphone
from ohho.common.logic.common.record.user_and_match_condition import UserAndMatchCondition
from ohho.common.view.backstage.management.relations.constant import *
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageUserAndMatchConditionListHandler(BaseHandler):
    def post(self):
        pass

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        user_instance = User()
        relation_instance = UserAndMatchCondition()

        username = the_get.get_username(self)
        name = the_get.get_name(self)
        match_condition_ids = the_get.get_id(self)

        if username is None:
            username = ""
        if name is None:
            name = ""
        if match_condition_ids is None:
            match_condition_ids = ""

        query = relation_instance.find(username, name, match_condition_ids)

        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        query, count = relation_instance.get_some(query, offset, limit)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()
        relations = list()
        for u in query:
            temp = dict()
            temp["id"] = u.id
            temp["user_id"] = u.user_id
            temp["match_condition_id"] = u.match_condition_id
            if u.name is not None:
                temp["name"] = u.name
            else:
                temp["name"] = ""
            the_user = user_instance.get_by_id(u.user_id)
            if the_user:
                temp["username"] = the_user.username
            else:
                temp["username"] = ""
            relations.append(temp)

        return self.render(USER_AND_MATCH_CONDITION_LIST_HTML,
                           relations=relations,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           list_url=USER_AND_MATCH_CONDITION_LIST_URL,
                           detail_url=USER_AND_MATCH_CONDITION_DETAIL_URL,
                           add_url=USER_AND_MATCH_CONDITION_ADD_URL,
                           delete_url=USER_AND_MATCH_CONDITION_DELETE_URL,
                           username=username,
                           name=name,
                           match_condition_ids=match_condition_ids,
                           )
