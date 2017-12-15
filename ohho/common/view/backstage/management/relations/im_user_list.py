from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.logic.common.relations.user_and_cellphone import UserAndCellphoneRelation
from ohho.common.logic.common.cellphone import Cellphone
from ohho.common.logic.common.im.user import User as IMUser
from ohho.common.logic.common.user import User as OHHOUser
from ohho.common.view.backstage.management.relations.constant import *
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageIMUserListHandler(BaseHandler):
    def post(self):
        pass

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        username = the_get.get_username(self)
        if username is None:
            username = ""
        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        im_user_instance = IMUser()
        ohho_user_instance = OHHOUser()

        users_query = ohho_user_instance.get_all()
        users_query = ohho_user_instance.get_valid(users_query)

        query = im_user_instance.get_all()
        users = ohho_user_instance.find_by_username(username)
        user_id_list = list()
        if not ohho_user_instance.user.is_empty(users):
            user_id_list = [user.id for user in users]
        query = im_user_instance.find_by_account(query, user_id_list)

        query, count = im_user_instance.im_user.get_some(query, offset, limit)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()
        im_users = list()
        for u in query:
            temp = dict()
            temp["id"] = u.id
            temp["state"] = u.state
            temp["user_id"] = u.account_id
            if u.name is not None:
                temp["name"] = u.name
            else:
                temp["name"] = ""
            the_user = ohho_user_instance.get_by_id(u.account_id)
            if the_user:
                temp["username"] = the_user.username
            im_users.append(temp)

        return self.render(IM_USER_LIST_HTML,
                           im_users=im_users,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           list_url=IM_USER_LIST_URL,
                           detail_url=IM_USER_DETAIL_URL,
                           add_url=IM_USER_ADD_URL,
                           delete_url=IM_USER_DELETE_URL,
                           username=username,
                           users_query=users_query,
                           )
