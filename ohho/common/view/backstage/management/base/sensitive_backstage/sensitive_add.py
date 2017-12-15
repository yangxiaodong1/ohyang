from tornado.web import authenticated

from ohho.common.logic.common.base.sensitive_backstage import SensitiveBackstage
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.base.constant import *

from ohho.common.view.common.parameters import Post
from ohho.common.view.common.parameters import Get
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageSensitiveAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        name = the_post.get_name(self)
        instance = SensitiveBackstage()
        if name:
            data = dict()
            data["word"] = name
            success = instance.add(data)
            if success:
                return self.redirect(BASE_SENSITIVE_BACKSTAGE_LIST_URL)

        return self.redirect(BASE_SENSITIVE_BACKSTAGE_ADD_URL)

    @permission
    @backstage_authenticate
    def get(self):
        return self.render(BASE_SENSITIVE_BACKSTAGE_ADD_HTML,
                           add_url=BASE_SENSITIVE_BACKSTAGE_ADD_URL,
                           list_url=BASE_SENSITIVE_BACKSTAGE_LIST_URL,
                           )
