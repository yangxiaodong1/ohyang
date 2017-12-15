from Tools.decorator import authenticate
from ohho.common.logic.ohho.match.logic_set_match_switch import LogicSetMatchSwitch
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class SetMatchSwitchHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        is_match = int(the_post.get_is_match(self))

        instance = LogicSetMatchSwitch()
        result = instance.set_match_switch(user_id, is_match)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
