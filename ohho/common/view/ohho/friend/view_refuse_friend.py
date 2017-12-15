from Tools.decorator import authenticate
from ohho.common.logic.ohho.friend.logic_refuse_friend import LogicRefuseFriend
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class RefuseFriendHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_id = the_post.get_friend_id(self)

        instance = LogicRefuseFriend()
        result = instance.refuse_friend(user_id, friend_id)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
