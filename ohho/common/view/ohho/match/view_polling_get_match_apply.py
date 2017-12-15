from ohho.common.view.common.parameters import Post
from ohho.common.logic.ohho.match.logic_polling_get_match_apply import LogicPollingGetMatchApply
from Tools.decorator import authenticate
from ohho.common.view.view_ohho_base import ViewOHHOBase


class PollingGetMatchApplyHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        base_url = the_post.get_base_url(self)
        instance = LogicPollingGetMatchApply()
        result = instance.get(user_id, base_url)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
