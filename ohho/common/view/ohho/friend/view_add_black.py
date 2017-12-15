from Tools.decorator import authenticate
from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.logic.ohho.friend.logic_add_black import LogicAddBlack
from ohho.common.view.common.parameters import Post


class AddBlackHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        friend_user_id = the_post.get_friend_id(self)


        black = LogicAddBlack()

        result = black.add_black(user_id, friend_user_id)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
        # the_get = Get()
        # user_id = the_get.get_user_id(self)
        #
        # result = LogicListBlacks.list_blacks(user_id)
        #
        # self.set_status(status_code=200)
        # self.write(OHHOOperation.dict2json(result))
