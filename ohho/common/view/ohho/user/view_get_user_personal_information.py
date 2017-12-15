import json
from Tools.decorator import authenticate
from ohho.common.logic.ohho.user.logic_add_user_accuracy_extension import LogicAddUserAccuracyExtension
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.logic.ohho.user.logic_get_user_personal_information import LogicGetUserPersonalInformation


class GetUserPersonalInformationHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        base_url = the_post.get_base_url(self)
        # data = the_post.get_data(self)
        # user_extension_dict = json.loads(data)
        # if user_extension_dict.get("interest", None):
        #     user_extension_dict["interest"] = json.dumps(user_extension_dict["interest"])

        instance = LogicGetUserPersonalInformation()
        result = instance.get(user_id, base_url)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
