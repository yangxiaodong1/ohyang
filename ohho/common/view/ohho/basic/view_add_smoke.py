from ohho.common.logic.ohho.base.logic_add_smoke import LogicAddSmoke
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AddSmokeHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        name = the_post.get_name(self)
        instance = LogicAddSmoke()
        result = instance.add(name)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
