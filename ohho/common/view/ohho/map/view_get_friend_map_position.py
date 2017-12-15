from Tools.decorator import authenticate
from ohho.common.logic.ohho.map.logic_get_map_positions import LogicGetMapPositions
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class GetFriendMapPositionHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_friend_id(self)
        base_url = the_post.get_base_url(self)

        instance = LogicGetMapPositions()
        result = instance.get(user_id, base_url)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("get", "post"))
