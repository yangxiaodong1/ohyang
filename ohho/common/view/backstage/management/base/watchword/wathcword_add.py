from tornado.web import authenticated

from ohho.common.logic.common.base.watchword import Watchword
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.base.constant import BASE_WATCHWORD_ADD_HTML
from ohho.common.view.backstage.management.base.constant import BASE_WATCHWORD_ADD_URL
from ohho.common.view.backstage.management.base.constant import BASE_WATCHWORD_LIST_URL
from ohho.common.view.common.parameters import Post


class BackstageWatchwordAddHandler(BaseHandler):
    def post(self):
        the_post = Post()
        first = the_post.get_first(self)
        second = the_post.get_second(self)
        instance = Watchword()
        if first or second:
            data = dict()
            data["first"] = first
            data["second"] = second
            success = instance.add(data)
            if success:
                return self.redirect(BASE_WATCHWORD_LIST_URL)

        return self.redirect(BASE_WATCHWORD_ADD_URL)

    @authenticated
    def get(self):
        return self.render(BASE_WATCHWORD_ADD_HTML,
                           add_url=BASE_WATCHWORD_ADD_URL,
                           list_url=BASE_WATCHWORD_LIST_URL
                           )
