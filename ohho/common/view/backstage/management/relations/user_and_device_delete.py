from ohho.common.db.ohho.device.db_ohho_device import DBOHHODevice
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from tornado.web import authenticated

from ohho.common.db.ohho.relation.db_ohho_user_and_device_relation import DBOHHOUserAndDeviceRelation
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.relations.constant import *
from ohho.common.view.common.parameters import Get, Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageUserAndDeviceRelationDeleteHandler(BaseHandler):
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
        delete_or_restore = the_post.get_delete_or_restore(self)
        if delete_or_restore:
            if device:
                relation = relation_instance.get_by_device(device.id)
                if relation:
                    if relation.state:
                        # print("execute delete")
                        relation_instance.delete(relation)
                    else:
                        # print("execute restore")
                        relation_instance.restore(relation)

        return self.redirect(USER_AND_DEVICE_LIST_URL)

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        relation_id = the_get.get_id(self)
        username = ""
        identity_id = ""
        state = False
        user_instance = DBOHHOUser()
        device_instance = DBOHHODevice()
        relation_instance = DBOHHOUserAndDeviceRelation()
        if relation_id:
            relation = relation_instance.get_by_id(relation_id)
            if relation:
                state = relation.state
                user = user_instance.get_by_id(relation.user_id)
                username = user.username if user else ""
                device = device_instance.get_by_id(relation.device_id)
                identity_id = device.identity_id if device else ""

        return self.render(USER_AND_DEVICE_DELETE_HTML,
                           username=username,
                           identity_id=identity_id,
                           state=state,
                           detail_url=USER_AND_DEVICE_DETAIL_URL,
                           list_url=USER_AND_DEVICE_LIST_URL,
                           delete_url=USER_AND_DEVICE_DELETE_URL,
                           )
