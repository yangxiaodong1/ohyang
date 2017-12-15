from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_where_meet import LogicWhereMeet
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class WhereMeetHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        apply_id = the_post.get_apply_id(self)
        address = the_post.get_map_address(self)
        longitude = the_post.get_map_longitude(self)
        latitude = the_post.get_map_latitude(self)
        name = the_post.get_name(self)
        code = the_post.get_code(self)

        address_dict = dict()
        address_dict["address"] = address
        address_dict["name"] = name
        address_dict["code"] = code
        address_dict["longitude"] = longitude
        address_dict["latitude"] = latitude

        instance = LogicWhereMeet()
        result = instance.where_meet(user_id, apply_id, address_dict)
        return self.response(result)

    def get(self):
        pass
