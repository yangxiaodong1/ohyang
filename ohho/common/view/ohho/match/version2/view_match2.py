from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.decorator import authenticate, execute_time
from ohho.common.logic.ohho.match.logic_match22 import LogicMatch
from ohho.common.view.common.parameters import Post


class Version2Match2Handler(ViewOHHOBase):
    @execute_time
    @authenticate
    def post(self):
        the_get = Post()
        self.set_format(the_get.get_format(self))
        user_id = the_get.get_user_id(self)
        device_identities = the_get.get_device_identities(self)
        identity_id = the_get.get_device_identity_id(self)
        base_url = the_get.get_base_url(self)

        instance = LogicMatch()
        result = instance.match_version22(user_id, device_identities, base_url, identity_id)
        return self.response(result)

    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
