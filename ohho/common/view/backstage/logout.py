from ohho.common.view.common.parameters import Post
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.user import User


class BackstageLogoutHandler(BaseHandler):
    def post(self):
        pass

    def get(self):
        if self.current_user:
            self.clear_cookie("username")
        self.redirect("/backstage/login/")
