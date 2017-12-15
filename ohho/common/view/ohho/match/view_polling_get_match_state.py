from ohho.common.view.common.parameters import Post
from ohho.common.logic.ohho.match.logic_polling_get_match_state import LogicPollingGetMatchState
from Tools.decorator import authenticate
from ohho.common.view.view_ohho_base import ViewOHHOBase


class PollingGetMatchStateHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_user_id = the_post.get_friend_id(self)
        is_apply = the_post.get_is_apply(self)
        base_url = the_post.get_base_url(self)

        instance = LogicPollingGetMatchState()
        result = instance.get(user_id, friend_user_id, is_apply, base_url)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
