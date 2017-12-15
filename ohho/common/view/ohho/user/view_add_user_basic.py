from Tools.decorator import authenticate
from ohho.common.logic.ohho.user.logic_add_user_basic import LogicAddUserBasic
from ohho.common.view.common.parameters import Post, Headers
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AddUserBasicHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        data = the_post.get_data(self)

        result = LogicAddUserBasic.add_basic(user_id, data)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
