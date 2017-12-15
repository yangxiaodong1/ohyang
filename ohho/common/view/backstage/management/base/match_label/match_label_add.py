from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.record.match_label import MatchLabel
from ohho.common.view.common.parameters import Post
from tornado.web import authenticated
from ohho.common.view.backstage.management.base.constant import BASE_MATCH_LABEL_ADD_URL
from ohho.common.view.backstage.management.base.constant import BASE_MATCH_LABEL_ADD_HTML
from ohho.common.view.backstage.management.base.constant import BASE_MATCH_LABEL_LIST_URL


class BackstageMatchLabelAddHandler(BaseHandler):
    def post(self):
        the_post = Post()
        name = the_post.get_name(self)
        parent_id = the_post.get_id(self)
        data = dict()
        data["name"] = name
        if parent_id is not None:
            data["parent_id"] = parent_id

        instance = MatchLabel()

        query = instance.get_query()
        query = instance.get_by_name(query, name)
        query = instance.get_by_parent_id(query, parent_id)
        query = instance.order_by_id_desc(query)

        if instance.is_empty(query):
            success = instance.add(data)
            if success:
                return self.redirect(BASE_MATCH_LABEL_LIST_URL)
        else:
            first = instance.first(query)
            if first.state == 1:
                return self.redirect(BASE_MATCH_LABEL_LIST_URL)
            else:
                success = instance.update(first, {"state": 1})
                if success:
                    return self.redirect(BASE_MATCH_LABEL_LIST_URL)

        return self.redirect(BASE_MATCH_LABEL_ADD_URL)

    @authenticated
    def get(self):
        return self.render(BASE_MATCH_LABEL_ADD_HTML,
                           add_url=BASE_MATCH_LABEL_ADD_URL,
                           list_url=BASE_MATCH_LABEL_LIST_URL
                           )
