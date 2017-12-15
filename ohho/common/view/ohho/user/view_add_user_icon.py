from Tools.decorator import authenticate
from ohho.common.logic.ohho.user.logic_add_user_icon import LogicAddUserIcon
from ohho.common.view.common.parameters import Post, Headers
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AddUserIconHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        # the_header = Headers()
        user_id = the_post.get_user_id(self)
        # user_id = user_id if user_id else the_header.get_user_id(self)
        # return self.write(self.request.files.get("icon"))
        image_file = self.request.files.get("icon")
        image_sequence = the_post.get_sequence(self)
        base_url = the_post.get_base_url(self)

        instance = LogicAddUserIcon()
        result = instance.add_user_icon(user_id, image_file, base_url, image_sequence)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
