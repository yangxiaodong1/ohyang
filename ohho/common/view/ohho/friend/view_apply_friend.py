from Tools.decorator import authenticate
from ohho.common.logic.ohho.friend.logic_apply_friend import LogicApplyFriend
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.ohho_log import OHHOLog


class ApplyFriendHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_id = the_post.get_friend_id(self)
        apply_id = the_post.get_apply_id(self)
        OHHOLog.print_log("user_id=%d" % user_id)
        OHHOLog.print_log("friend_user_id=%d" % friend_id)
        instance = LogicApplyFriend()
        result = instance.apply_friend(user_id, friend_id, apply_id)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
