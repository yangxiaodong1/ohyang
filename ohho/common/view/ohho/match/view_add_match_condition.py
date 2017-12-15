from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate
from ohho.common.logic.ohho.match.logic_add_match_condition import LogicAddMatchCondition
from ohho.common.view.common.parameters import Post


class AddMatchConditionHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        name = the_post.get_name(self)
        condition_dict = the_post.get_match_condition(self)
        instance = LogicAddMatchCondition()
        result = instance.add(user_id, name, condition_dict)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
