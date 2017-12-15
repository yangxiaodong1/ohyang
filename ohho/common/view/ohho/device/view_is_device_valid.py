from ohho.common.logic.ohho.device.logic_is_device_valid import LogicIsDeviceValid
from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class IsDeviceValidHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        identity_id = the_post.get_device_identity_id(self)
        mac_address = the_post.get_device_mac_address(self)

        instance = LogicIsDeviceValid()
        result = instance.is_device_valid(identity_id, mac_address)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
