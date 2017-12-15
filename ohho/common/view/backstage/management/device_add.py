from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.device import Device
from tornado.web import authenticated
from ohho.common.view.backstage.constant import *
from math import ceil
from ohho.common.view.common.pagination import Pagination
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageDeviceAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        device_dict = the_post.get_device(self)
        if device_dict.get("identity_id", None):
            instance = Device()
            success = instance.add(device_dict)
            if success:
                return self.redirect(MANAGEMENT_DEVICE_LIST_URL)
            else:
                return self.redirect(MANAGEMENT_DEVICE_ADD_URL)

        return self.redirect(MANAGEMENT_DEVICE_ADD_URL)

    @permission
    @backstage_authenticate
    def get(self):
        return self.render(MANAGEMENT_DEVICE_ADD_HTML)
        # return self.render("backstage/management/device_add.html")
