from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate
from ohho.common.logic.ohho.device.logic_add_device_version import LogicAddDeviceVersion
from ohho.common.view.common.parameters import Post

# no use
class AddDeviceVersionHandler(ViewOHHOBase):
    # @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        version = the_post.get_device_version(self)
        name = the_post.get_name(self)
        url = the_post.get_url(self)
        instance = LogicAddDeviceVersion()
        result = instance.add_device_version(version, name, url)
        return self.response(result)

    @authenticate
    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
