from Tools.decorator import authenticate
from ohho.common.logic.ohho.user.logic_add_user_favourite_sport import LogicAddUserFavouriteSport
from ohho.common.view.common.parameters import Post, Headers
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AddUserFavouriteSportHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        name = the_post.get_name(self)
        sport_id = the_post.get_sport_id(self)
        data = dict()
        data["user_id"] = user_id
        data["name"] = name
        data["sport_id"] = sport_id

        instance = LogicAddUserFavouriteSport()
        result = instance.add_sport(data)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
