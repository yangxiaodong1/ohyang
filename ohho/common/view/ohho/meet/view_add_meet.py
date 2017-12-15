from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_add_meet import LogicAddMeet
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AddMeetHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_user_id = the_post.get_friend_id(self)
        address = the_post.get_map_address(self)

        instance = LogicAddMeet()
        result = instance.add_meet(user_id, friend_user_id, address)
        return self.response(result)

    def get(self):
        pass
