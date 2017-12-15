from ohho.common.db.ohho.permission.db_ohho_page import DBOHHOPermissionPage
from ohho.common.db.ohho.permission.db_ohho_page_permission import DBOHHOPermissionPagePermission
from ohho.common.db.ohho.permission.db_ohho_group import DBOHHOPermissionGroup
from ohho.common.db.ohho.permission.db_ohho_group_and_user_relation import DBOHHOPermissionGroupAndUserRelation
from ohho.common.db.ohho.permission.db_ohho_group_and_page_relation import DBOHHOPermissionGroupAndPageRelation
from functools import reduce
from Tools.ohho_log import OHHOLog
from Tools.ohho_datetime import OHHODatetime


class OHHOPermission(object):
    def __init__(self):
        self.page = DBOHHOPermissionPage()
        self.page_permission = DBOHHOPermissionPagePermission()
        self.group = DBOHHOPermissionGroup()
        self.group_and_page = DBOHHOPermissionGroupAndPageRelation()
        self.group_and_user = DBOHHOPermissionGroupAndUserRelation()

    def get_group_and_page(self, group_id, page_permission_id):
        query = self.group_and_page.get_query()
        query = self.group_and_page.get_by_group_id(query, group_id)
        query = self.group_and_page.get_by_page_permission_id(query, page_permission_id)
        return self.group_and_page.first(query)

    def add_group_and_page(self, permission_dict, group_id):
        timestamp = OHHODatetime.get_current_timestamp()
        permission_dict["timestamp"] = timestamp
        OHHOLog.print_log(permission_dict)
        if not self.page_permission.get_by_timestamp(timestamp) and group_id:
            success = self.page_permission.add(permission_dict)
            if success:
                permission = self.page_permission.get_by_timestamp(timestamp)
                if permission:
                    data = dict()
                    data["group_id"] = group_id
                    data["page_permission_id"] = permission.id
                    success = self.group_and_page.add(data)
                    if success:
                        return "添加成功"
                    else:
                        return "添加页面权限成功，但未绑定（请重新添加）"
            else:
                return "添加失败"
        else:
            return "参数不正确或者其他人和你同时添加，请重新添加"

    def get_relations_by_username(self, username):
        query = self.group_and_user.get_query()
        return self.group_and_user.get_by_username(query, username)

    def get_page_by_name(self, name):
        query = self.page.get_query()
        return self.page.get_by_name(query, name)

    def get_page_permission_by_page(self, page_id):
        query = self.page_permission.get_query()
        query = self.page_permission.get_by_page(query, page_id)
        return query

    def get_group_and_page_by_page_permission_and_group_list(self, page_permission_id_list, group_id_list):
        query = self.group_and_page.get_query()
        query = self.group_and_page.get_by_page_permission_ids(query, page_permission_id_list)
        query = self.group_and_page.get_by_group_ids(query, group_id_list)
        return query

    def get_group_by_ids(self, group_id_list):
        query = self.group.get_query()
        return self.group.get_group_by_ids(query, group_id_list)

    def get_page_permission_by_ids(self, page_permission_id_list):
        query = self.page_permission.get_query()
        query = self.page_permission.get_by_page_permission_ids(query, page_permission_id_list)
        return query

    def page_exist(self, name):
        page = self.get_page_by_name(name)
        if page and not self.page.is_empty(page):
            return True
        else:
            return False

    def add_page(self, name):
        return self.page.add(name)

    def get_page(self, name):
        query = self.page.get_query()
        query = self.page.get_by_name(query, name)
        return self.page.first(query)

    def get_or_create_page_from_permission(self, name):
        OHHOLog.print_log(name)
        if self.page_exist(name):
            OHHOLog.print_log("exist page")
            return self.get_page(name)
        else:
            OHHOLog.print_log("not exist page")
            success = self.add_page(name)
            OHHOLog.print_log(success)

            return self.get_page(name)

    def get_the_page_permission(self, page_permission_list):
        result = dict()
        insert = list()
        delete = list()
        change = list()
        select = list()
        if page_permission_list:
            for permission in page_permission_list:
                insert.append(permission.insert)
                delete.append(permission.delete)
                change.append(permission.update)
                select.append(permission.select)
        or_function = lambda x, y: x | y
        result["insert"] = reduce(or_function, insert) if insert else 0
        result["delete"] = reduce(or_function, delete) if delete else 0
        result["update"] = reduce(or_function, change) if change else 0
        result["select"] = reduce(or_function, select) if select else 0
        return result

    def get_the_page_permission_from_permission(self, username, page):
        if username and page:
            page_id = page.id
            page_permission_list = self.get_page_permission_by_page(page_id)
            page_permission_id_list = [p.id for p in page_permission_list]
            relations = self.get_relations_by_username(username)
            group_id_list = [r.group_id for r in relations]
            group_and_page_permissions = self.get_group_and_page_by_page_permission_and_group_list(
                page_permission_id_list,
                group_id_list)
            the_page_permission_id_list = [p.page_permission_id for p in group_and_page_permissions]
            the_page_permission_list = self.get_page_permission_by_ids(the_page_permission_id_list)
            permission = self.get_the_page_permission(the_page_permission_list)
            return permission
        else:
            return {"insert": 0, "delete": 0, "update": 0, "select": 0}
