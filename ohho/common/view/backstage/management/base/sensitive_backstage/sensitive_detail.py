from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.watchword import Watchword
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.base.sensitive_backstage import SensitiveBackstage
from tornado.web import authenticated
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageSensitiveDetailHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        sensitive_id = the_post.get_id(self)
        submit = the_post.get_submit(self)
        name = the_post.get_name(self)
        instance = SensitiveBackstage()
        sensitive_object = instance.get_by_id(sensitive_id)
        if submit and sensitive_object:
            data = dict()
            data["word"] = name
            success = instance.update(sensitive_object, data)
            if success:
                return self.redirect(BASE_SENSITIVE_BACKSTAGE_LIST_URL)
        return self.redirect(BASE_SENSITIVE_BACKSTAGE_DETAIL_HTML + "?id=" + str(sensitive_id))

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        sensitive_id = the_get.get_id(self)
        instance = SensitiveBackstage()
        sensitive_object = instance.get_by_id(sensitive_id)
        name = ""
        if sensitive_object:
            name = sensitive_object.word

        return self.render(BASE_SENSITIVE_BACKSTAGE_DETAIL_HTML,
                           name=name,
                           sensitive_id=sensitive_id,
                           detail_url=BASE_SENSITIVE_BACKSTAGE_DETAIL_URL,
                           list_url=BASE_SENSITIVE_BACKSTAGE_LIST_URL,
                           add_url=BASE_SENSITIVE_BACKSTAGE_ADD_URL,
                           delete_url=BASE_SENSITIVE_BACKSTAGE_DELETE_URL
                           )
