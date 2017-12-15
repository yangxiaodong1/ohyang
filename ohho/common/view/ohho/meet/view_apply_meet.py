from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_apply_meet import LogicApplyMeet
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class ApplyMeetHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_id = the_post.get_friend_id(self)
        match_condition_id = the_post.get_match_condition_id(self)
        base_url = the_post.get_base_url(self)
        instance = LogicApplyMeet()
        result = instance.apply_meet(user_id, friend_id, match_condition_id, base_url)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
