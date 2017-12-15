from Tools.decorator import authenticate
from ohho.common.logic.ohho.match.logic_add_record_exclude import LogicAddRecordExclude
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AddExcludeHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        exclude_user_id = the_post.get_exclude_user_id(self)
        match_condition_id = the_post.get_match_condition_id(self)
        exclude = LogicAddRecordExclude()

        result = exclude.add_exclude(user_id, exclude_user_id, match_condition_id)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
