from ohho.common.logic.ohho.device.logic_get_device_setting import LogicGetDeviceSetting
from ohho.common.view.common.parameters import Post, Get
from ohho.common.view.view_ohho_base import ViewOHHOBase


class GetDeviceSettingHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        identity_id = the_post.get_device_identity_id(self)
        setting = LogicGetDeviceSetting()
        result = setting.get_device_setting(identity_id)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
