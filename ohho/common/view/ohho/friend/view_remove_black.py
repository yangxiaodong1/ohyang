from Tools.decorator import authenticate
from ohho.common.logic.ohho.friend.logic_remove_black import LogicRemoveBlack
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class RemoveBlackHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_user_id = the_post.get_friend_id(self)
        instance = LogicRemoveBlack()
        result = instance.remove_black(user_id, friend_user_id)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
