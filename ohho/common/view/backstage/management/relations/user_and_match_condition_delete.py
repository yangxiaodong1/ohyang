from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.relations.constant import *
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated
from ohho.common.logic.common.record.user_and_match_condition import UserAndMatchCondition
from ohho.common.logic.common.user import User
from Tools.ohho_log import OHHOLog
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageUserAndMatchConditionDeleteHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        user_instance = User()
        relation_instance = UserAndMatchCondition()

        username = the_post.get_username(self)
        name = the_post.get_name(self)
        match_condition_id = the_post.get_match_condition_id(self)
        user_and_match_condition_id = the_post.get_id(self)

        relation = relation_instance.get_by_id(user_and_match_condition_id)
        match_condition = relation_instance.get_match_condition(match_condition_id)

        submit = the_post.get_submit(self)
        delete = the_post.get_delete(self)
        detail_url = USER_AND_MATCH_CONDITION_DETAIL_URL + "?id=" + user_and_match_condition_id

        user = user_instance.get_by_cellphone(username)
        OHHOLog.print_log(submit)
        OHHOLog.print_log(relation)
        OHHOLog.print_log(user)
        OHHOLog.print_log(match_condition)

        if submit and relation and user and match_condition:
            OHHOLog.print_log("start logic")
            data = dict()
            data["user_id"] = user.id
            data["name"] = name
            data["match_condition_id"] = match_condition_id
            success = relation_instance.update(relation, data)
            if success:
                return self.redirect(USER_AND_MATCH_CONDITION_LIST_URL)
        if delete and relation:
            success = relation_instance.delete(relation)
            if success:
                return self.redirect(USER_AND_MATCH_CONDITION_LIST_URL)
        return self.redirect(detail_url)

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        user_instance = User()
        relation_instance = UserAndMatchCondition()

        user_and_match_condition_id = the_get.get_id(self)
        relation = relation_instance.get_by_id(user_and_match_condition_id)
        username = ""
        match_condition_id = ""
        name = ""
        if relation:
            user = user_instance.get_by_id(relation.user_id)
            username = user.username
            if relation.match_condition_id is not None:
                match_condition_id = relation.match_condition_id
            if relation.name is not None:
                name = relation.name

        return self.render(USER_AND_MATCH_CONDITION_DELETE_HTML,
                           username=username,
                           name=name,
                           match_condition_id=match_condition_id,
                           user_and_match_condition_id=user_and_match_condition_id,
                           detail_url=USER_AND_MATCH_CONDITION_DETAIL_URL,
                           list_url=USER_AND_MATCH_CONDITION_LIST_URL,
                           delete_url=USER_AND_MATCH_CONDITION_DELETE_URL
                           )
