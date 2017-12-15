from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_cancel_meet import LogicCancelMeet
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class CancelMeetHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_id = the_post.get_friend_id(self)
        apply_id = the_post.get_apply_id(self)
        base_url = the_post.get_base_url(self)
        instance = LogicCancelMeet()
        result = instance.cancel_meet(user_id, friend_id, apply_id, base_url)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
