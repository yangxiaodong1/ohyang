from tornado.web import authenticated

from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.permission.constant import *

from ohho.common.view.common.parameters import Post
from ohho.common.view.common.parameters import Get
from ohho.common.logic.common.permission.permission import OHHOPermission
from ohho.common.logic.common.user import User
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageGroupUserRelationAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        group_id = the_post.get_id(self)
        group_users_name = self.get_body_arguments("group_user")
        users_name = self.get_body_arguments("name")
        data = dict()
        instance = OHHOPermission().group_and_user
        success = ""
        if group_id:
            if users_name:
                for user_name in users_name:
                    group_name = instance.get_by_group_id_and_username(group_id, user_name)
                    if group_name:
                        success = instance.delete(group_name)
            if group_users_name:
                for user_name in group_users_name:
                    group_name = instance.get_by_group_id_and_username(group_id, user_name)
                    if not group_name:
                        data["group_id"] = group_id
                        data["username"] = user_name
                        success = instance.add(data)
        else:
            pass
        if success:
            return self.redirect(PERMISSION_GROUP_BACKSTAGE_LIST_URL)
        return self.redirect(PERMISSION_GROUP_USER_RELATION_ADD_URL + "?group_id=" + group_id)

    # @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        group_id = the_get.get_id(self)
        if group_id:
            instance_user = DBOHHOUser()
            instance_group_user_relation = OHHOPermission().group_and_user
            users = instance_user.get_query()
            users = instance_user.get_valid(users)
            users = instance_user.get_all(users)
            user_list = list()
            group_user_list = list()
            group_users = instance_group_user_relation.get_by_group_id(group_id)
            group_users = instance_group_user_relation.get_all(group_users)
            if users:
                for user in users:
                    if group_users:
                        for group_user in group_users:
                            if user.username == group_user.username:
                                group_user_list.append(user)
                    user_list.append(user)
            user_list = list(set(user_list) - set(group_user_list))
            return self.render(PERMISSION_GROUP_USER_RELATION_HTML,
                               add_url=PERMISSION_GROUP_USER_RELATION_ADD_URL,
                               delete_url=PERMISSION_GROUP_USER_RELATION_DELETE_URL,
                               list_url=PERMISSION_GROUP_BACKSTAGE_LIST_URL,
                               group_id=group_id,
                               user_list=user_list,
                               group_user_list=group_user_list,
                               )
        else:
            return self.redirect(PERMISSION_GROUP_BACKSTAGE_LIST_URL)
