from Tools.decorator import authenticate
from ohho.common.logic.ohho.device.logic_cancel_lost import LogicCancelLost
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class CancelLostHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        identity_id = the_post.get_device_identity_id(self)
        cancel_lost = LogicCancelLost()

        result = cancel_lost.cancel_lost(user_id, identity_id)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
