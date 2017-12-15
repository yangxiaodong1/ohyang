from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.record.match_condition import MatchCondition
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated


class BackstageMatchConditionDetailHandler(BaseHandler):
    def post(self):
        the_post = Post()
        instance = MatchCondition()
        match_condition_id = the_post.get_id(self)
        match_condition_parameters = the_post.get_match_condition(self)
        match_condition = instance.get_by_id(match_condition_id)
        submit = the_post.get_submit(self)
        delete = the_post.get_delete(self)
        success = False
        if submit and match_condition:
            success = instance.update(match_condition, match_condition_parameters)

        if delete:
            success = instance.delete(match_condition)

        if success:
            return self.redirect(BASE_MATCH_CONDITION_LIST_URL)
        return self.redirect(BASE_MATCH_CONDITION_DETAIL_HTML + "?id=" + str(match_condition_id))

    @authenticated
    def get(self):
        the_get = Get()
        instance = MatchCondition()
        match_condition_id = the_get.get_id(self)
        match_condition = instance.get_by_id(match_condition_id)
        match_condition_dict = instance.get_information(match_condition)

        return self.render(BASE_MATCH_CONDITION_DETAIL_HTML,
                           condition=match_condition_dict,
                           match_condition_id=match_condition_id,
                           detail_url=BASE_MATCH_CONDITION_DETAIL_URL,
                           list_url=BASE_MATCH_CONDITION_LIST_URL
                           )
