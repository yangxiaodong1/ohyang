from Tools.decorator import authenticate
from ohho.common.view.common.parameters import Post
from ohho.common.logic.ohho.device.logic_get_device_version import LogicGetDeviceVersion
from ohho.common.view.view_ohho_base import ViewOHHOBase


class GetDeviceVersionHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        instance = LogicGetDeviceVersion()
        result = instance.get_device_version()
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
