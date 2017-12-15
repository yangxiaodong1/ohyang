from Tools.decorator import authenticate
from ohho.common.logic.ohho.meet.logic_agree_meet import LogicAgreeMeet
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class AgreeMeetHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = int(the_post.get_user_id(self))
        friend_id = int(the_post.get_friend_id(self))
        base_url = the_post.get_base_url(self)
        apply_id = the_post.get_apply_id(self)
        instance = LogicAgreeMeet()
        result = instance.agree_meet(user_id, friend_id, apply_id, base_url)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
