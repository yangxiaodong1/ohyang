import tornado.web

from Tools.ohho_operation import OHHOOperation
from ohho.common.logic.ohho.register.logic_reset_password import LogicResetPassword
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.view.backstage.constant import *

HOME_URL = "/rest/api/ohho/test/home/app/"

class BackageResetPasswordHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        cellphone_number = the_post.get_cellphone_number(self)
        password = the_post.get_password(self)
        code = the_post.get_code(self)
        instance = LogicResetPassword()
        result = instance.reset_password(cellphone_number, password, code)
        if result.get("code") == 1:
            return self.redirect("/backstage/home/")
        return self.redirect("/backstage/login/")

    def get(self):
        return self.render(BACKSTAGE_RESET_PASSWORD_HTML,
                           postUrl=BACKSTAGE_RESET_PASSWORD_URL,
                           home_url=HOME_URL
                           )

