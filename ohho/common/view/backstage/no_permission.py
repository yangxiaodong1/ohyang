from ohho.common.view.common.parameters import Post, Get
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.user import User


class BackstageNoPermissionHandler(BaseHandler):
    def post(self):
        pass

    def get(self):
        the_get = Get()
        code = the_get.get_code(self)
        message = the_get.get_data(self)
        return self.render("backstage/no_permission.html", code=code, message=message)
        # self.redirect("/backstage/login/")
