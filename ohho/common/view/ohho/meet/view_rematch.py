from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_rematch import LogicRematch
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class RematchHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_user_id = the_post.get_friend_id(self)
        apply_id = the_post.get_apply_id(self)
        is_published = the_post.get_type(self)

        instance = LogicRematch()
        result = instance.rematch(user_id, friend_user_id, apply_id, is_published)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
