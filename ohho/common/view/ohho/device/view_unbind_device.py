from Tools.decorator import authenticate
from ohho.common.logic.ohho.device.logic_unbind_device import LogicUnbindDevice
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class UnbindDeviceHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        identity_id = the_post.get_device_identity_id(self)
        mac_address = the_post.get_device_mac_address(self)
        instance = LogicUnbindDevice()
        result = instance.unbind_device(user_id, identity_id, mac_address)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
