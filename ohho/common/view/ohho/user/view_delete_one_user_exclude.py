from Tools.decorator import authenticate
from ohho.common.logic.ohho.user.logic_add_user_exclude import LogicAddUserExclude
from ohho.common.view.common.parameters import Post, Headers
from ohho.common.view.view_ohho_base import ViewOHHOBase


class DeleteOneUserExcludeHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        # the_header = Headers()
        user_id = the_post.get_user_id(self)
        # user_id = user_id if user_id else the_header.get_user_id(self)
        exclude_user_id = the_post.get_user_extension_exclude(self)

        instance = LogicAddUserExclude()
        result = instance.delete_one_user_exclude(user_id, exclude_user_id)
        return self.response(result)

    def get(self):
        self.write(self.request.host)
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
