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


class BackstageGroupPageRelationDetailHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        OHHOLog.print_log(self.request.body)
        permission = OHHOPermission()
        submit = the_post.get_submit(self)
        group_id = the_post.get_group_id(self)
        page_name = the_post.get_page_name(self)
        page_permission_id = int(the_post.get_page_permission_id(self))
        insert = int(the_post.get_insert(self))
        delete = int(the_post.get_delete(self))
        update = int(the_post.get_update(self))
        select = int(the_post.get_select(self))
        if submit:
            if page_permission_id:
                page_permission = permission.page_permission.get_by_id(page_permission_id)
                if page_permission:
                    data = dict()
                    data["insert"] = insert if insert else 0
                    data["delete"] = delete if delete else 0
                    data["update"] = update if update else 0
                    data["select"] = select if select else 0
                    success = permission.page_permission.update(page_permission, data)
                    if success:
                        message = "更新成功"
                    else:
                        message = "更新失败"
                else:
                    message = "暂时还没有页面权限，请添加"
            else:
                message = "页面权限ID不合法"
        else:
            message = "未提交"
        return self.redirect(
            PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_DETAIL_URL
            + "?page_permission_id=%d&data=%s&page_name=%s&insert=%d&delete=%d&update=%d&select=%d&group_id=%d" % (
                int(page_permission_id), message, page_name, int(insert), int(delete), int(update), int(select),
                int(group_id)))

    # @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        permission = OHHOPermission()
        group_id = the_get.get_group_id(self)
        group = permission.group.get_by_id(group_id)
        group_name = group.name if group else ""
        page_name = the_get.get_page_name(self)
        page_permission_id = int(the_get.get_page_permission_id(self))
        insert = int(the_get.get_insert(self))
        delete = int(the_get.get_delete(self))
        update = int(the_get.get_update(self))
        select = int(the_get.get_select(self))
        message = the_get.get_data(self)

        return self.render(PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_DETAIL_HTML,
                           page_name=page_name,
                           page_permission_id=page_permission_id,
                           insert=insert,
                           delete=delete,
                           update=update,
                           select=select,
                           group_id=group_id,
                           group_name=group_name,
                           home_list_url=MANAGEMENT_PERMISSION_HOME_URL,
                           list_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_LIST_URL + "?id=" + str(group_id),
                           detail_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_DETAIL_URL + "?page_permission_id=%d&data=%s&page_name=%s&insert=%d&delete=%d&update=%d&select=%d&group_id=%d" % (
                               int(page_permission_id), message, page_name, int(insert), int(delete), int(update),
                               int(select),
                               int(group_id)),
                           add_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_ADD_URL + "?group_id=" + str(group_id),
                           delete_url=PERMISSION_GROUP_PAGE_RELATION_BACKSTAGE_DELETE_URL + "?page_permission_id=%d&data=%s&page_name=%s&insert=%d&delete=%d&update=%d&select=%d&group_id=%d" % (
                               int(page_permission_id), message, page_name, int(insert), int(delete), int(update),
                               int(select),
                               int(group_id)),
                           message=message
                           )
