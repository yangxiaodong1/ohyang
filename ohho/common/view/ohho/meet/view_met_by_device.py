from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_met_by_device import LogicMetByDevice
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class MetByDeviceHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        apply_id = the_post.get_apply_id(self)
        friend_user_id = the_post.get_friend_id(self)
        base_url = the_post.get_base_url(self)

        instance = LogicMetByDevice()
        result = instance.met(user_id, friend_user_id, apply_id, base_url)
        return self.response(result)

    def get(self):
        pass
