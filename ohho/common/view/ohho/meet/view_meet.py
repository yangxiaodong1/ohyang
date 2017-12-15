from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_meet import LogicMeet
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class MeetHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        last_id = the_post.get_last_id(self)
        limit = the_post.get_limit(self)
        base_url = the_post.get_base_url(self)

        instance = LogicMeet()
        result = instance.met(user_id, last_id, limit, base_url)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
