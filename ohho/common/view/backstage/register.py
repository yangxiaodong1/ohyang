from ohho.common.view.common.parameters import Post
from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler

from ohho.common.logic.common.user import User
from ohho.common.logic.common.result import Result

from ohho.common.view.backstage.constant import *
from ohho.common.logic.ohho.register.logic_backstage_register import LogicBackstageRegister
from ohho.common.logic.ohho.register.logic_register import LogicRegister
from ohho.common.logic.common.code import Code
from Tools.ohho_log import OHHOLog


class BackstageRegisterHandler(BaseHandler):
    def post(self):
        user = User()
        the_post = Post()
        country_code = the_post.get_country_code(self)
        cellphone = the_post.get_username(self)
        password = the_post.get_password(self)
        code = the_post.get_code(self)
        instance = LogicBackstageRegister()
        register_instance = LogicRegister()
        msg = ""
        country_code_object = user.get_country_code(country_code)
        if country_code_object and not user.get_by_country_code_and_cellphone(country_code_object.id, cellphone):
            register_result = register_instance.add_new_user(password, cellphone, country_code)
            OHHOLog.print_log(register_result)
            if Result.is_success(register_result):
                user_id = register_result.get("user_id", 0)

                user_object = user.get_by_id(user_id)
                if user_object:
                    self.set_secure_cookie("username", user_object.username)
                    return self.redirect("/backstage/home/")
        # if Code.check_code(username, code):  # 目前验证码没有用，先注释掉
        #     pass
        # else:
        #     return self.render(BACKSTAGE_REGISTER_HTML,
        #                        postUrl=BACKSTAGE_REGISTER_URL,
        #                        msg="验证码不正确"
        #                        )
        # if username and password:
        #     result1 = instance.register(username, password)
        #     if result1:
        #         self.set_secure_cookie("username", username)
        #         return self.redirect("/backstage/home/")
        return self.render(BACKSTAGE_REGISTER_HTML,
                           postUrl=BACKSTAGE_REGISTER_URL,
                           msg="注册不成功"
                           )

    def get(self):
        instance = User()
        the_get = Get()
        username = the_get.get_username(self)
        if username:
            user = instance.get_by_username(username)
            if user:
                return self.write("false")
            else:
                return self.write("true")
        return self.render(BACKSTAGE_REGISTER_HTML,
                           postUrl=BACKSTAGE_REGISTER_URL,
                           msg=""
                           )
