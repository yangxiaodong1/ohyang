from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.logic.common.relations.user_and_device import UserAndDeviceRelation
from ohho.common.logic.common.device import Device
from ohho.common.logic.common.user import User
from ohho.common.view.backstage.management.relations.constant import *
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageUserAndDeviceRelationListHandler(BaseHandler):
    def post(self):
        pass

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()

        identity_id = the_get.get_device_identity_id(self)
        if identity_id is None:
            identity_id = ""
        username = the_get.get_username(self)
        if username is None:
            username = ""
        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        relation_instance = UserAndDeviceRelation()
        device_instance = Device()
        user_instance = User()

        users_query = user_instance.get_all()
        users_query = user_instance.get_valid(users_query)

        devices_query = device_instance.get_all_device()

        query = relation_instance.get_all()
        if identity_id:
            device_query = device_instance.get_all_device()
            device_instance.set_identity(identity_id)
            device_query = device_instance.find_by_identity(device_query)
            device_query = device_instance.device.get_all(device_query)
            device_id_list = list()
            if device_query:
                device_id_list = [device.id for device in device_query]
            query = relation_instance.find_by_device(query, device_id_list)

        if username:
            user_query = user_instance.find_by_username(username)
            user_query = user_instance.user.get_all(user_query)
            user_id_list = list()
            if user_query:
                user_id_list = [user.id for user in user_query]
            query = relation_instance.find_by_user(query, user_id_list)

        query, count = relation_instance.instance.get_some(query, offset, limit)
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
            device = device_instance.get_by_id(q.device_id)
            temp["identity_id"] = device.identity_id if device else ""
            temp["device_id"] = device.id if device else ""
            relations.append(temp)

        return self.render(USER_AND_DEVICE_LIST_HTML,
                           relations=relations,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           list_url=USER_AND_DEVICE_LIST_URL,
                           detail_url=USER_AND_DEVICE_DETAIL_URL,
                           add_url=USER_AND_DEVICE_ADD_URL,
                           delete_url=USER_AND_DEVICE_DELETE_URL,
                           username=username,
                           identity_id=identity_id,
                           user_query=users_query,
                           device_query=devices_query
                           )
