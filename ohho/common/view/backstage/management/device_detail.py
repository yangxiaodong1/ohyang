from tornado.web import authenticated

from ohho.common.logic.common.device import Device
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.constant import *
from ohho.common.view.common.parameters import Get, Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageDeviceDetailHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        device_id = the_post.get_device_id(self)
        submit = self.get_body_argument("submit", "")
        delete = self.get_body_argument("delete", "")
        detail_url = MANAGEMENT_DEVICE_DETAIL_URL + "?device_id=" + str(device_id)
        instance = Device()
        if delete:
            device = instance.get_by_id(device_id)
            success = instance.delete(device)
            if success:
                return self.redirect(MANAGEMENT_DEVICE_LIST_URL)
            else:
                return self.redirect(detail_url)

        if submit:
            device_instance = instance.get_by_id(device_id)
            data = the_post.get_device(self)
            success = instance.update(device_instance, data)

            if success:
                return self.redirect(MANAGEMENT_DEVICE_LIST_URL)
            else:
                return self.redirect(detail_url)
        return self.redirect(detail_url)

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        device_id = the_get.get_device_id(self)
        instance = Device()
        device = instance.get_by_id(device_id)

        return self.render(MANAGEMENT_DEVICE_DETAIL_HTML, device=device)
        # return self.render("backstage/management/device_detail.html", device=device)
