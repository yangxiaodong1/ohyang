from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.record.match_condition import MatchCondition
from ohho.common.view.common.parameters import Post
from tornado.web import authenticated
from ohho.common.view.backstage.management.base.constant import BASE_MATCH_CONDITION_ADD_URL
from ohho.common.view.backstage.management.base.constant import BASE_MATCH_CONDITION_ADD_HTML
from ohho.common.view.backstage.management.base.constant import BASE_MATCH_CONDITION_LIST_URL


class BackstageMatchConditionAddHandler(BaseHandler):
    def post(self):
        the_post = Post()
        match_condition = the_post.get_match_condition(self)
        instance = MatchCondition()
        condition = instance.get(match_condition)

        if not condition:
            success = instance.add(match_condition)
            if success:
                return self.redirect(BASE_MATCH_CONDITION_LIST_URL)

        return self.redirect(BASE_MATCH_CONDITION_ADD_URL)

    @authenticated
    def get(self):
        return self.render(BASE_MATCH_CONDITION_ADD_HTML,
                           add_url=BASE_MATCH_CONDITION_ADD_URL,
                           list_url=BASE_MATCH_CONDITION_LIST_URL
                           )
