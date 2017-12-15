from ohho.common.logic.ohho.code.logic_check_verification_code import LogicCheckVerificationCode
from ohho.common.view.common.parameters import Get
from ohho.common.view.view_ohho_base import ViewOHHOBase


class CheckVerificationCodeHandler(ViewOHHOBase):
    def post(self):
        self.write("This is a %s method, %s is not supported" % ("get", "post"))

    def get(self):
        the_get = Get()
        self.set_format(the_get.get_format(self))
        country_code = the_get.get_cellphone_country_code(self)
        cellphone_number = the_get.get_cellphone_number(self)
        code = the_get.get_code(self)
        the_cellphone = country_code + cellphone_number
        result = LogicCheckVerificationCode.check_verification_code(the_cellphone, code)
        return self.response(result)
