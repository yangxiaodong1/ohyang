from ohho.common.logic.ohho.device.logic_get_user_and_device_imei import LogicGetUserAndDeviceIMEI
from ohho.common.view.common.parameters import Post, Get
from ohho.common.view.view_ohho_base import ViewOHHOBase


class GetUserAndDeviceIMEIHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        imei = LogicGetUserAndDeviceIMEI()
        result = imei.get()
        return self.response(result)

    def get(self):
        the_get = Get()
        self.set_format(the_get.get_format(self))
        imei = LogicGetUserAndDeviceIMEI()
        result = imei.get()
        return self.response(result)
