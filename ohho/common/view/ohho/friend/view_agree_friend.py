from Tools.decorator import authenticate
from ohho.common.logic.ohho.friend.logic_agree_friend import LogicAgreeFriend
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AgreeFriendHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_id = the_post.get_friend_id(self)
        instance = LogicAgreeFriend()
        result = instance.agree_friend(user_id, friend_id)
        return self.response(result)

        # self.write(OHHOOperation.dict2json(result))

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
