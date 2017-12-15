from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate
from ohho.common.logic.ohho.register.logic_logout import LogicLogout
from ohho.common.view.common.parameters import Post


class LogoutHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        token = the_post.get_token(self)

        instance = LogicLogout()
        result = instance.logout(user_id, token)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
