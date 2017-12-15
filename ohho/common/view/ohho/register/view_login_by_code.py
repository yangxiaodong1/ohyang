from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.logic.ohho.register.logic_login_by_code import LogicLoginByCode
from ohho.common.view.common.parameters import Post


class LoginByCodeHandler(ViewOHHOBase):
    def post(self):
        the_post = Post()
        self.set_format(the_post.get_format(self))
        username = the_post.get_username(self)
        password = the_post.get_password(self)
        country_code = the_post.get_cellphone_country_code(self)
        cellphone_dict = the_post.get_cellphone(self)
        base_url = the_post.get_base_url(self)
        code = the_post.get_code(self)

        instance = LogicLoginByCode()
        result = instance.authenticate(country_code, username, password, cellphone_dict, base_url, code)
        return self.response(result)

    def get(self):
        self.write("This is a %s method, %s is not supported" % ("post", "get"))
