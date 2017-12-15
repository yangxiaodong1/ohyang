from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_meet_end import LogicMeetEnd
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class MeetEndHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        apply_id = the_post.get_apply_id(self)
        friend_user_id = the_post.get_friend_id(self)
        base_url = the_post.get_base_url(self)

        instance = LogicMeetEnd()
        result = instance.meet_end(user_id, friend_user_id, apply_id, base_url)
        return self.response(result)

    def get(self):
        pass
