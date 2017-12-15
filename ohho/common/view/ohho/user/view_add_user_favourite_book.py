from Tools.decorator import authenticate
from ohho.common.logic.ohho.user.logic_add_user_favourite_book import LogicAddUserFavouriteBook
from ohho.common.view.common.parameters import Post, Headers
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AddUserFavouriteBookHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        # the_header = Headers()
        user_id = the_post.get_user_id(self)
        name = the_post.get_name(self)
        isbn = the_post.get_isbn()
        data = dict()
        data["user_id"] = user_id
        data["name"] = name
        data["isbn"] = isbn

        instance = LogicAddUserFavouriteBook()
        result = instance.add_book(data)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
