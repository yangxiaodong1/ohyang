from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.watchword import Watchword
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.base.sensitive_backstage import SensitiveBackstage
from tornado.web import authenticated
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageSensitiveDeleteHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        sensitive_id = the_post.get_id(self)
        delete_or_restore = the_post.get_delete_or_restore(self)
        instance = SensitiveBackstage()
        sensitive_object = instance.get_by_id(sensitive_id)
        if delete_or_restore and sensitive_object:
            success = instance.delete(sensitive_object)
            if success:
                return self.redirect(BASE_SENSITIVE_BACKSTAGE_LIST_URL)
        return self.redirect(BASE_SENSITIVE_BACKSTAGE_DELETE_HTML + "?id=" + str(sensitive_id))

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

        return self.render(BASE_SENSITIVE_BACKSTAGE_DELETE_HTML,
                           name=name,
                           sensitive_id=sensitive_id,
                           detail_url=BASE_SENSITIVE_BACKSTAGE_DETAIL_URL,
                           list_url=BASE_SENSITIVE_BACKSTAGE_LIST_URL,
                           add_url=BASE_SENSITIVE_BACKSTAGE_ADD_URL,
                           delete_url=BASE_SENSITIVE_BACKSTAGE_DELETE_URL
                           )
