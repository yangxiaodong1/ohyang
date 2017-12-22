from tornado.web import authenticated

from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.permission.constant import *

from ohho.common.view.common.parameters import Post
from ohho.common.view.common.parameters import Get
from ohho.common.logic.common.permission.permission import OHHOPermission
from ohho.common.logic.common.staff import Staff
from ohho.common.db.ohho.user.db_ohho_staff import DBOHHOStaff
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageGroupStaffRelationAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        group_id = the_post.get_id(self)
        group_staffs_name = self.get_body_arguments("group_user")
        staffs_name = self.get_body_arguments("name")
        data = dict()
        instance = OHHOPermission().group_and_staff
        success = ""
        if group_id:
            if staffs_name:
                for staff_name in staffs_name:
                    group_name = instance.get_by_group_id_and_username(group_id, staff_name)
                    if group_name:
                        success = instance.delete(group_name)
            if group_staffs_name:
                for staff_name in group_staffs_name:
                    group_name = instance.get_by_group_id_and_username(group_id, staff_name)
                    if not group_name:
                        data["group_id"] = group_id
                        data["username"] = staff_name
                        success = instance.add(data)
        else:
            pass
        if success:
            return self.redirect(PERMISSION_GROUP_BACKSTAGE_LIST_URL)
        return self.redirect(PERMISSION_GROUP_STAFF_RELATION_ADD_URL + "?group_id=" + group_id)

    # @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        group_id = the_get.get_id(self)
        if group_id:
            instance_staff = DBOHHOStaff()
            instance_group_staff_relation = OHHOPermission().group_and_staff
            staffs = instance_staff.get_query()
            staffs = instance_staff.get_valid(staffs)
            staffs = instance_staff.get_all(staffs)
            staff_list = list()
            group_staff_list = list()
            group_staffs = instance_group_staff_relation.get_by_group_id(group_id)
            group_staffs = instance_group_staff_relation.get_all(group_staffs)
            if staffs:
                for staff in staffs:
                    if group_staffs:
                        for group_staff in group_staffs:
                            if staff.username == group_staff.username:
                                group_staff_list.append(staff)
                    staff_list.append(staff)
            staff_list = list(set(staff_list) - set(group_staff_list))
            return self.render(PERMISSION_GROUP_STAFF_RELATION_HTML,
                               add_url=PERMISSION_GROUP_STAFF_RELATION_ADD_URL,
                               delete_url=PERMISSION_GROUP_STAFF_RELATION_DELETE_URL,
                               list_url=PERMISSION_GROUP_BACKSTAGE_LIST_URL,
                               group_id=group_id,
                               staff_list=staff_list,
                               group_staff_list=group_staff_list,
                               )
        else:
            return self.redirect(PERMISSION_GROUP_BACKSTAGE_LIST_URL)
