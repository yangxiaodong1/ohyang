import json
from Tools.decorator import authenticate
from ohho.common.logic.ohho.user.logic_add_user_accuracy_extension import LogicAddUserAccuracyExtension
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AddUserAccuracyExtensionHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        data = the_post.get_data(self)
        user_extension_dict = json.loads(data)
        if user_extension_dict.get("interest", None):
            user_extension_dict["interest"] = json.dumps(user_extension_dict["interest"])
        instance = LogicAddUserAccuracyExtension()
        result = instance.add_user_accuracy_extension(user_id, user_extension_dict)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
