from Tools.decorator import authenticate
from ohho.common.logic.ohho.map.logic_get_map_positions import LogicGetMapPositions
from ohho.common.view.common.parameters import Post, Get
from ohho.common.view.view_ohho_base import ViewOHHOBase


class GetMapPositionsHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        base_url = the_post.get_base_url(self)
        positions = LogicGetMapPositions()
        result = positions.get(user_id, base_url)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
