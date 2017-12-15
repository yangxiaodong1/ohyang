import tornado.web
import json

from Tools.decorator import authenticate
from Tools.ohho_log import OHHOLog
from ohho.common.logic.ohho.user.logic_update_cellphone_number import LogicUpdateCellphoneNumber
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class UpdateCellphoneNumberHandler(ViewOHHOBase):
    @authenticate
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        user_id = the_post.get_user_id(self)
        OHHOLog.print_log(user_id)
        cellphone_number = the_post.get_cellphone_number(self)
        code = the_post.get_code(self)
        country_code = the_post.get_country_code(self)
        instance = LogicUpdateCellphoneNumber()
        result = instance.change(user_id, cellphone_number, code, country_code)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
