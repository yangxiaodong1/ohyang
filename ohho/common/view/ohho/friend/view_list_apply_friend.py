from Tools.decorator import authenticate
from ohho.common.logic.ohho.friend.logic_list_apply_friend import LogicListApplyFriend
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class ListApplyFriendHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        base_url = the_post.get_base_url(self)

        instance = LogicListApplyFriend()
        result = instance.list_apply_friend(user_id, base_url)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
