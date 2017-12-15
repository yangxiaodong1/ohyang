from Tools.decorator import authenticate
from ohho.common.logic.ohho.user.logic_add_user_favourite_movie import LogicAddUserFavouriteMovie
from ohho.common.view.common.parameters import Post, Headers
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AddUserFavouriteMovieHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        movie_id = the_post.get_movie_id(self)
        name = the_post.get_name(self)
        data = dict()
        data["user_id"] = user_id
        data["movie_id"] = movie_id
        data["name"] = name
        instance = LogicAddUserFavouriteMovie()
        result = instance.add_movie(data)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
