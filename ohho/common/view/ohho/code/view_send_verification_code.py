from ohho.common.logic.ohho.code.logic_send_verification_code import LogicSendVerificationCode
from ohho.common.view.common.parameters import Post
from ohho.common.view.view_ohho_base import ViewOHHOBase


class SendVerificationCodeHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        country_code = the_post.get_cellphone_country_code(self)
        cellphone_number = the_post.get_cellphone_number(self)
        if not country_code:
            country_code = "+86"
        the_cellphone_number = country_code + cellphone_number

        result = LogicSendVerificationCode.send_verification_code(the_cellphone_number)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
