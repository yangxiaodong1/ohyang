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

class BackstageGroupPageRelationListHandler(BaseHandler):
    def post(self):
        pass

    # @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        instance = OHHOPermission()
        group_id = the_get.get_id(self)
        page = the_get.get_page(self)
        data_count_per_page = the_get.get_data_count_per_page(self)
        page_count_per_page = the_get.get_page_count_per_page(self)
        offset = (page - 1) * data_count_per_page
        limit = data_count_per_page

        query = instance.group_and_page.get_query()
        group_name = ""

        if group_id:
            query = instance.group_and_page.get_by_group_id(query, group_id)
            group = instance.group.get_by_id(group_id)
            if group:
                group_name = group.name

        query, count = instance.group_and_page.get_some(query, offset, limit)
        # query = query
        # count = instance.page_permission.get_count(query)
        total_page = int(ceil(count / data_count_per_page))
        pagination = Pagination(total_page, page, data_count_per_page, page_count_per_page)
        page_list, previous, next = pagination.get_page_list_of_this_page()

        group_permissions = list()
        if query:
            for q in query:
                temp = dict()
                page_permission = instance.page_permission.get_by_id(q.page_permission_id)
                if page_permission:
                    temp["group_id"] = group_id
                    temp["page_permission_id"] = q.page_permission_id
                    page = instance.page.get_by_id(page_permission.page_id)
                    if page:
                        temp["page_description"] = page.description
                        temp["page_name"] = page.name
                    temp["insert"] = page_permission.insert
                    temp["update"] = page_permission.update
                    temp["select"] = page_permission.select
                    temp["delete"] = page_permission.delete
                if temp:
                    group_permissions.append(temp)

        return self.render(PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_LIST_HTML,
                           group_name=group_name,
                           group_permissions=group_permissions,
                           pages=page_list,
                           previous=previous,
                           next=next,
                           page=page,
                           home_list_url=MANAGEMENT_PERMISSION_HOME_URL,
                           list_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_LIST_URL,
                           detail_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_DETAIL_URL,
                           add_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_ADD_URL + "?id=" + str(group_id),
                           delete_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_DELETE_URL,
                           )
