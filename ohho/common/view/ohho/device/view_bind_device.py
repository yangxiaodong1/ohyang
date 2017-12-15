from Tools.decorator import authenticate
from ohho.common.logic.ohho.device.logic_bind_device import LogicBindDevice
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class BindDeviceHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        identity_id = the_post.get_device_identity_id(self)
        mac_address = the_post.get_device_mac_address(self)
        imei = the_post.get_imei(self)
        instance = LogicBindDevice()
        result = instance.bind_device(user_id, identity_id, mac_address, imei)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
