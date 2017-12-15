from Tools.decorator import authenticate
from ohho.common.logic.ohho.device.logic_set_device_use import LogicSetDeviceUse
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class SetDeviceUseHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        identity_id = the_post.get_device_identity_id(self)

        type = the_post.get_device_type(self)
        name = the_post.get_name(self)

        data = dict()
        if type is not None:
            data["type"] = type

        if name is not None:
            data["name"] = name

        lost = LogicSetDeviceUse()

        result = lost.set_device_use(user_id, identity_id, data)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
