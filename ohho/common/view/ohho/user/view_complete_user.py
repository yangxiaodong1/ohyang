from Tools.decorator import authenticate
from ohho.common.logic.ohho.user.logic_complete_user import LogicCompleteUser
from ohho.common.logic.common.result import Result
from ohho.common.view.common.parameters import Post, Headers
from ohho.common.view.view_ohho_base import ViewOHHOBase


class CompleteUserHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        data = the_post.get_data(self)
        base_url = the_post.get_base_url(self)
        # icon0 = self.request.files["icon0"]
        icon0 = the_post.get_files_icon0(self)
        icon1 = the_post.get_files_icon1(self)
        icon2 = the_post.get_files_icon2(self)
        icon3 = the_post.get_files_icon3(self)

        instance = LogicCompleteUser()
        check_sensitive = instance.has_sensitive(data)
        if check_sensitive:
            result = Result.result_failed()
            result["sensitive"] = check_sensitive
        else:
            result = instance.complete(user_id, data, icon0, icon1, icon2, icon3, base_url)
        return self.response(result)

    def get(self):
        self.write(self.request.body)
        # self.write("This is a %s method, %s is not supported" % ("post", "get"))
