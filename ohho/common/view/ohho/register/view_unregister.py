from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.logic.ohho.register.logic_register import LogicRegister
from ohho.common.view.common.parameters import Post
from Tools.ohho_log import OHHOLog
from Tools.decorator import authenticate


class UnregisterHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        user_id = the_post.get_user_id(self)
        format = the_post.get_format(self)
        self.set_format(format)
        instance = LogicRegister(dict(), dict())
        result = instance.unregister(user_id)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
