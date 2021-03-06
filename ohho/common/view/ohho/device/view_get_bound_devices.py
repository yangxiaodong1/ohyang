from ohho.common.logic.ohho.device.logic_get_bound_devices import LogicGetBoundDevices
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate


class GetBoundDevicesHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)

        instance = LogicGetBoundDevices()
        result = instance.get(user_id)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
