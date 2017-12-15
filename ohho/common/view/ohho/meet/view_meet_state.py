from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_meet import LogicMeet
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.logic.ohho.meet.logic_meet_state import LogicMeetState


class MeetStateHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        base_url = the_post.get_base_url(self)
        instance = LogicMeetState()

        result = instance.meet_state(user_id, base_url)
        return self.response(result)

    def get(self):
        pass
