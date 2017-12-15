from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.watchword import Watchword
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated


class BackstageWatchwordDetailHandler(BaseHandler):
    def post(self):
        the_post = Post()
        watchword_id = the_post.get_id(self)
        first = the_post.get_first(self)
        second = the_post.get_second(self)
        instance = Watchword()
        watchword_obj = instance.get(watchword_id)
        submit = the_post.get_submit(self)
        delete_or_restore = the_post.get_delete_or_restore(self)
        success = False
        if submit:
            data = dict()
            if first or second:
                data["first"] = first
                data["second"] = second

            success = instance.update(watchword_obj, data)
        if delete_or_restore:
            if watchword_obj.first or watchword_obj.second:
                success = instance.delete(watchword_obj)
            else:
                success = instance.restore(watchword_obj)

        if success:
            return self.redirect(BASE_WATCHWORD_LIST_URL)
        return self.redirect(BASE_WATCHWORD_DETAIL_HTML + "?id=" + str(watchword_id))

    @authenticated
    def get(self):
        the_get = Get()
        watchword_id = the_get.get_id(self)
        first = ""
        second = ""
        instance = Watchword()
        if watchword_id:
            watchword_obj = instance.get(watchword_id)
            first = watchword_obj.first
            second = watchword_obj.second

        return self.render(BASE_WATCHWORD_DETAIL_HTML,
                           first=first,
                           second=second,
                           watchword_id=watchword_id,
                           detail_url=BASE_WATCHWORD_DETAIL_URL,
                           list_url=BASE_WATCHWORD_LIST_URL
                           )
