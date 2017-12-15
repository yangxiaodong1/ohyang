from Tools.decorator import authenticate
from Tools.ohho_operation import OHHOOperation
from ohho.common.logic.ohho.map.logic_map_distance import LogicMapDistance
from ohho.common.view.common.parameters import Post, Get
from ohho.common.view.view_ohho_base import ViewOHHOBase


# no use
class MapDistanceHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_id = the_post.get_friend_id(self)
        latitude = the_post.get_friend_id(self)
        longitude = the_post.get_friend_id(self)

        instance = LogicMapDistance()
        result = LogicMapDistance.map_distance(user_id, friend_id, latitude, longitude)
        return self.response(result)

    @authenticate
    def get(self):
        the_get = Get()
        user_id = the_get.get_user_id(self)
        friend_id = the_get.get_friend_id(self)
        latitude = the_get.get_friend_id(self)
        longitude = the_get.get_friend_id(self)

        instance = LogicMapDistance()
        result = instance.map_distance(user_id, friend_id, latitude, longitude)
        return self.write(OHHOOperation.dict2json(result))
