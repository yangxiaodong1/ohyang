from tornado.web import authenticated

from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.db.ohho.record.db_ohho_record_match_condition import DBOHHORecordMatchCondition
from ohho.common.logic.common.record.user_and_match_condition import UserAndMatchCondition
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.relations.constant import *
from ohho.common.view.common.parameters import Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate

class BackstageUserAndMatchConditionAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        user_instance = DBOHHOUser()
        condition_instance = DBOHHORecordMatchCondition()
        relation_instance = UserAndMatchCondition()

        username = the_post.get_username(self)
        name = the_post.get_name(self)
        match_condition_id = the_post.get_id(self)

        user = user_instance.get_by_cellphone(username)
        match_condition = condition_instance.get_by_id(match_condition_id)
        if user and match_condition:
            result = relation_instance.add(user.id, name, match_condition_id)
            if result["code"] == 1:
                return self.redirect(USER_AND_MATCH_CONDITION_LIST_URL)
        return self.redirect(USER_AND_MATCH_CONDITION_ADD_URL)

    @permission
    @backstage_authenticate
    def get(self):
        return self.render(USER_AND_MATCH_CONDITION_ADD_HTML,
                           add_url=USER_AND_MATCH_CONDITION_ADD_URL,
                           list_url=USER_AND_MATCH_CONDITION_LIST_URL
                           )
