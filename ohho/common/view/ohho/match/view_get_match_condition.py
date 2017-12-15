from Tools.decorator import authenticate
from Tools.ohho_operation import OHHOOperation
from ohho.common.logic.ohho.match.logic_get_match_condition import LogicGetMatchCondition
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


# no use
class GetMatchConditionHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        name = the_post.get_name(self)

        condition = LogicGetMatchCondition()
        result, query = condition.get(user_id, name)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
