from Tools.decorator import authenticate
from ohho.common.logic.ohho.friend.logic_set_online_switch import LogicSetOnlineSwitch
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class SetOnlineSwitchHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        is_online = int(the_post.get_is_online(self))
        instance = LogicSetOnlineSwitch()
        result = instance.set_online_switch(user_id, is_online)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
