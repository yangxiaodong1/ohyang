from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.smoke import Smoke
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated


class BackstageSmokeDetailHandler(BaseHandler):
    def post(self):
        instance = Smoke()
        the_post = Post()
        smoke_id = the_post.get_id(self)
        name = the_post.get_name(self)
        smoke = instance.get(smoke_id)
        submit = self.get_body_argument("submit", None)
        delete_or_restore = self.get_body_argument("delete_or_restore", None)
        success = False
        if submit:
            data = dict()
            data["name"] = name
            success = instance.update(smoke, data)
        if delete_or_restore:
            if smoke.state:
                success = instance.delete(smoke)
            else:
                success = instance.restore(smoke)

        if success:
            return self.redirect(BASE_SMOKE_LIST_URL)
        return self.redirect(BASE_SMOKE_DETAIL_HTML + "?id=" + str(smoke_id))

    @authenticated
    def get(self):
        the_get = Get()
        smoke_id = the_get.get_id(self)
        name = ""
        state = False
        instance = Smoke()
        if smoke_id:
            smoke = instance.get(smoke_id)
            name = smoke.name
            state = smoke.state

        return self.render(BASE_SMOKE_DETAIL_HTML,
                           name=name,
                           state=state,
                           smoke_id=smoke_id,
                           detail_url=BASE_SMOKE_DETAIL_URL,
                           list_url=BASE_SMOKE_LIST_URL
                           )
