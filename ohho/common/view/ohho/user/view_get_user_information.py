from ohho.common.logic.ohho.user.logic_get_user_information import LogicGetUserInformation
from ohho.common.view.common.parameters import Post
from Tools.decorator import authenticate
from ohho.common.view.view_ohho_base import ViewOHHOBase


class GetUserInformationHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        user_id = the_post.get_user_id(self)
        friend_user_id = the_post.get_friend_id(self)
        format = the_post.get_format(self)
        base_url = the_post.get_base_url(self)
        if format:
            self.set_format(format)
        else:
            self.set_format()
        instance = LogicGetUserInformation()
        result = instance.get(friend_user_id, user_id, base_url)
        return self.response(result)

    # @authenticate
    def get(self):
        return self.write("This is a %s method, %s is not supported" % ("post", "get"))
        # the_get = Get()
        # user_id = the_get.get_user_id(self)
        # instance = LogicGetUserInformation()
        # result = instance.get(user_id)
        # return self.write(OHHOOperation.dict2json(result))
        # self.write("This is a %s method, %s is not supported" % ("post", "get"))
        # the_get = Get()
        # user_id = the_get.get_user_id(self)
        #
        # result = LogicListBlacks.list_blacks(user_id)
        #
        # self.set_status(status_code=200)
        # self.write(OHHOOperation.dict2json(result))
