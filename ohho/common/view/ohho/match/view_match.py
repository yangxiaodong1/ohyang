from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate
from Tools.ohho_operation import OHHOOperation
from ohho.common.logic.ohho.match.logic_match import LogicMatch
from ohho.common.view.common.parameters import Post


class MatchHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        device_identities = the_post.get_device_identities(self)
        user_id = the_post.get_user_id(self)
        name = the_post.get_name(self)
        base_url = the_post.get_base_url(self)
        conditions = the_post.get_conditions(self)
        if conditions:
            condition_dict = OHHOOperation.json2dict(conditions)
        else:
            condition_dict = dict()

        instance = LogicMatch()
        result = instance.match(device_identities, user_id, name, condition_dict, base_url)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
