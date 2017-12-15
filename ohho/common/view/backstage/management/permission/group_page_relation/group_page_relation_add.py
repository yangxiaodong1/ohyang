from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from math import ceil
from ohho.common.view.common.pagination import Pagination
from ohho.common.logic.common.permission.permission import OHHOPermission
from ohho.common.view.backstage.management.permission.constant import *
from ohho.common.view.backstage.constant import MANAGEMENT_PERMISSION_HOME_URL
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageGroupPageRelationAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        OHHOLog.print_log(self.request.body)
        permission = OHHOPermission()
        submit = the_post.get_submit(self)
        group_id = int(the_post.get_group_id(self))
        page_id = int(the_post.get_page_id(self))
        insert = int(the_post.get_insert(self))
        delete = int(the_post.get_delete(self))
        update = int(the_post.get_update(self))
        select = int(the_post.get_select(self))
        if submit:
            if page_id:
                data = dict()
                data["page_id"] = page_id
                data["insert"] = insert if insert else 0
                data["delete"] = delete if delete else 0
                data["update"] = update if update else 0
                data["select"] = select if select else 0
                message = permission.add_group_and_page(data, group_id)
            else:
                message = "请选择有效页面"
        else:
            message = "未提交"
        return self.redirect(
            PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_ADD_URL + "?id=" + str(group_id) + "&data=" + message)

    # @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        instance = OHHOPermission()
        group_id = the_get.get_id(self)
        message = the_get.get_data(self)
        group_name = ""
        if group_id:
            group_id = int(group_id)
            group = instance.group.get_by_id(group_id)
            if group:
                group_name = group.name

        all_page = instance.page.get_query()
        page_ids = [p.id for p in all_page] if all_page else []

        query_group_and_page = instance.group_and_page.get_query()
        query_group_and_page = instance.group_and_page.get_by_group_id(query_group_and_page, group_id)
        permission_ids = [p.page_permission_id for p in query_group_and_page] if query_group_and_page else []

        query_page_permission = instance.page_permission.get_query()
        query_page_permission = instance.page_permission.get_by_page_permission_ids(query_page_permission,
                                                                                    permission_ids)
        permission_page_ids = [q.page_id for q in query_page_permission] if query_page_permission else []

        the_page_ids = OHHOOperation.list_minus_list(page_ids, permission_page_ids)
        rest_page_list = list()
        for page_id in the_page_ids:
            page = instance.page.get_by_id(page_id)
            temp = dict()
            if page:
                temp["page_id"] = page.id
                temp["page_description"] = page.description
                temp["page_name"] = page.name
            if temp:
                rest_page_list.append(temp)

        return self.render(PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_ADD_HTML,
                           group_id=group_id,
                           rest_page_list=rest_page_list,
                           group_name=group_name,
                           home_list_url=MANAGEMENT_PERMISSION_HOME_URL,
                           list_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_LIST_URL + "?id=" + str(group_id),
                           detail_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_DETAIL_URL,
                           add_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_ADD_URL + "?id=" + str(group_id),
                           delete_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_DELETE_URL,
                           message=message
                           )
