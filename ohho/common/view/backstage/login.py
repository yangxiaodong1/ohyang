from ohho.common.view.common.parameters import Post, Get
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.user import User
from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_log import OHHOLog


class BackstageLoginHandler(BaseHandler):
    def post(self):
        instance = User()
        the_post = Post()
        country_code = the_post.get_cellphone_country_code(self)
        username = the_post.get_username(self)
        password = the_post.get_password(self)

        if not username or not password or not country_code:
            message = "username or password or country_code is empty"
            return self.redirect("/backstage/login/?data=%s" % message)
        else:
            success, the_username = instance.check_user4backstage(username, password, country_code)
            if success:
                OHHOLog.print_log("login success")

                user_instance = instance.get_by_username(the_username)
                if user_instance:
                    instance.token.add(user_instance.id)
                    update_success = instance.update_user(user_instance, {"last_login": OHHODatetime.get_utc_now()})
                    OHHOLog.print_log(update_success)
                else:
                    OHHOLog.print_log("no such user")
                self.set_secure_cookie("username", the_username)
                return self.redirect("/backstage/home/")
            if the_username:
                message = "password is incorrect"
            else:
                message = "user does not exist"
        return self.redirect("/backstage/login/?data=%s" % message)

    def get(self):
        the_get = Get()
        message = the_get.get_data(self)
        if self.current_user:
            return self.redirect("/backstage/home/")
        return self.render("backstage/login.html", message=message)
