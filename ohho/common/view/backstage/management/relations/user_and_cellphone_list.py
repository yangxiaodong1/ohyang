from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.logic.common.relations.user_and_cellphone import UserAndCellphoneRelation
from ohho.common.logic.common.cellphone import Cellphone
from ohho.common.logic.common.user import User
from ohho.common.view.backstage.management.relations.constant import *
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageUserAndCellphoneRelationListHandler(BaseHandler):
    def post(self):
        pass

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        cellphone_instance = Cellphone()
        relation_instance = UserAndCellphoneRelation()
        user_instance = User()

        users_query = user_instance.get_all()
        users_query = user_instance.get_valid(users_query)
        cellphones_query = cellphone_instance.get_all_cellphone()

        cellphone_key = the_get.get_cellphone_key(self)
        if cellphone_key is None:
            cellphone_key = ""
        username = the_get.get_username(self)
        if username is None:
            username = ""
        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        query = relation_instance.get_all()
        if cellphone_key:
            cellphone_query = cellphone_instance.get_all_cellphone()
            cellphone_query = cellphone_instance.find_by_key(cellphone_query, cellphone_key)
            cellphone_id_list = list()
            if not cellphone_instance.cellphone.is_empty(cellphone_query):
                cellphone_id_list = [cellphone.id for cellphone in cellphone_query]
            query = relation_instance.find_by_cellphone(query, cellphone_id_list)

        if username:
            user_query = user_instance.find_by_username(username)
            user_id_list = list()
            if not user_instance.user.is_empty(user_query):
                user_id_list = [user.id for user in user_query]
            query = relation_instance.find_by_user(query, user_id_list)

        query, count = relation_instance.get_some(query, offset, limit)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()
        relations = list()
        for q in query:
            temp = dict()
            temp["id"] = q.id
            temp["state"] = q.state
            user = user_instance.get_by_id(q.user_id)
            temp["username"] = user.username if user else ""
            temp["user_id"] = user.id if user else ""
            cellphone = cellphone_instance.get_by_id(q.cellphone_id)
            temp["key"] = cellphone.key if cellphone else ""
            temp["cellphone_id"] = cellphone.id if cellphone else ""
            relations.append(temp)

        return self.render(USER_AND_CELLPHONE_LIST_HTML,
                           relations=relations,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           list_url=USER_AND_CELLPHONE_LIST_URL,
                           detail_url=USER_AND_CELLPHONE_DETAIL_URL,
                           add_url=USER_AND_CELLPHONE_ADD_URL,
                           delete_url=USER_AND_CELLPHONE_DELETE_URL,

                           username=username,
                           cellphone_key=cellphone_key,
                           users_query=users_query,
                           cellphones_query=cellphones_query
                           )
