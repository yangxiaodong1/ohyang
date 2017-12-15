from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_meet_topic import LogicMeetTopic
from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class MeetTopicHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        base_url = the_post.get_base_url(self)

        instance = LogicMeetTopic()
        result = instance.meet_topic()
        return self.response(result)

    def get(self):
        the_post = Get()
        self.set_format(the_post.get_format(self))
        base_url = the_post.get_base_url(self)

        instance = LogicMeetTopic()
        result = instance.meet_topic()
        return self.response(result)
