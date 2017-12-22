from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_meet_send_message import LogicMeetSendMessage
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class MeetSendMessageHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_user_id = the_post.get_friend_id(self)
        content = the_post.get_content(self)
        type = the_post.get_type(self)

        instance = LogicMeetSendMessage()
        result = instance.send(user_id, friend_user_id, content, type)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
