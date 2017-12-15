import tornado.web

from Tools.ohho_operation import OHHOOperation
from ohho.common.logic.ohho.register.logic_reset_password import LogicResetPassword
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class ResetPasswordHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        cellphone_number = the_post.get_cellphone_number(self)
        password = the_post.get_password(self)
        code = the_post.get_code(self)
        country_code = the_post.get_cellphone_country_code(self)
        cellphone_dict = the_post.get_cellphone(self)
        cellphone_dict = cellphone_dict if cellphone_dict else dict()
        base_url = the_post.get_base_url(self)
        instance = LogicResetPassword()
        result = instance.reset_password(cellphone_number, password, code, country_code, cellphone_dict, base_url)

        return self.response(result)
        # self.set_status(status_code=200)
        # self.write(OHHOOperation.dict2json(result))

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
