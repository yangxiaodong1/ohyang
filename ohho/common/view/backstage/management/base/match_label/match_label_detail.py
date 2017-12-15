from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.record.match_label import MatchLabel
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated


class BackstageMatchLabelDetailHandler(BaseHandler):
    def post(self):
        the_post = Post()
        instance = MatchLabel()
        match_label_id = the_post.get_id(self)
        name = the_post.get_name(self)
        parent_id = the_post.get_parent_id(self)
        match_label = instance.get_by_id(match_label_id)
        submit = the_post.get_submit(self)
        delete = the_post.get_delete(self)
        success = False
        if submit and match_label:
            data = dict()
            data["name"] = name
            data["parent_id"] = parent_id
            success = instance.update(match_label, data)

        if delete:
            success = instance.delete(match_label)

        if success:
            return self.redirect(BASE_MATCH_LABEL_LIST_URL)
        return self.redirect(BASE_MATCH_LABEL_DETAIL_HTML + "?id=" + str(match_label_id))

    @authenticated
    def get(self):
        the_get = Get()
        instance = MatchLabel()
        match_label_id = the_get.get_id(self)
        match_label = instance.get_by_id(match_label_id)
        match_label_dict = instance.get_information(match_label)

        return self.render(BASE_MATCH_LABEL_DETAIL_HTML,
                           label=match_label_dict,
                           match_label_id=match_label_id,
                           detail_url=BASE_MATCH_LABEL_DETAIL_URL,
                           list_url=BASE_MATCH_LABEL_LIST_URL
                           )
