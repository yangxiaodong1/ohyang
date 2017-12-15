from ohho.common.db.ohho.device.db_ohho_device import DBOHHODevice
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from tornado.web import authenticated

from ohho.common.db.ohho.relation.db_ohho_user_and_device_relation import DBOHHOUserAndDeviceRelation
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.relations.constant import *
from ohho.common.view.common.parameters import Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageUserAndDeviceRelationAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        username = the_post.get_username(self)
        identity_id = the_post.get_device_identity_id(self)
        user_instance = DBOHHOUser()
        device_instance = DBOHHODevice()
        relation_instance = DBOHHOUserAndDeviceRelation()
        user = user_instance.get_by_username(username)
        device_instance.set_identity(identity_id)
        device = device_instance.get_by_identity()
        if user and device:
            data = dict()
            data["user_id"] = user.id
            data["device_id"] = device.id
            success = relation_instance.add(data)
            if success:
                return self.redirect(USER_AND_DEVICE_LIST_URL)
        return self.redirect(USER_AND_DEVICE_ADD_URL)

    @permission
    @backstage_authenticate
    def get(self):
        user_instance = DBOHHOUser()
        device_instance = DBOHHODevice()
        user_query = user_instance.get_query()
        user_query = user_instance.get_valid(user_query)
        device_query = device_instance.get_query()
        device_query = device_instance.get_all(device_query)
        return self.render(USER_AND_DEVICE_ADD_HTML,
                           add_url=USER_AND_DEVICE_ADD_URL,
                           list_url=USER_AND_DEVICE_LIST_URL,
                           user_query=user_query,
                           device_query=device_query
                           )
