from ohho.common.db.ohho.db_cellphone import DBCellphone
from ohho.common.db.ohho.relation.db_ohho_user_and_cellphone_relation import DBOHHOUserAndCellphoneRelation
from tornado.web import authenticated

from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.relations.constant import *
from ohho.common.view.common.parameters import Get, Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageUserAndCellphoneRelationDeleteHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        user_instance = DBOHHOUser()
        cellphone_instance = DBCellphone()
        relation_instance = DBOHHOUserAndCellphoneRelation()

        the_post = Post()
        username = the_post.get_username(self)
        relation_id = the_post.get_id(self)
        detail_url = USER_AND_CELLPHONE_DETAIL_URL + "?id=" + relation_id
        cellphone_key = the_post.get_cellphone_key(self)
        user = user_instance.get_by_username(username)
        cellphone_instance.set_key(cellphone_key)
        cellphone = cellphone_instance.get_by_key()
        relation = relation_instance.get_by_id(relation_id)

        # submit = self.get_body_argument("submit", None)
        delete_or_restore = self.get_body_argument("delete_or_restore", None)

        # if submit:
        #     if cellphone and user:
        #         if relation:
        #             data = dict()
        #             data["user_id"] = user.id
        #             data["cellphone_id"] = cellphone.id
        #             success = relation_instance.update(relation, data)
        #             if success:
        #                 return self.redirect(USER_AND_CELLPHONE_LIST_URL)
        #     return self.redirect(detail_url)
        if delete_or_restore:
            if cellphone and user:
                if relation:
                    if relation.state:
                        # print("execute delete")
                        success = relation_instance.delete(relation)
                        if success:
                            return self.redirect(USER_AND_CELLPHONE_LIST_URL)
                    else:
                        # print("execute restore")
                        success = relation_instance.restore(relation)
                        if success:
                            return self.redirect(USER_AND_CELLPHONE_LIST_URL)
            return self.redirect(detail_url)

    @permission
    @backstage_authenticate
    def get(self):
        user_instance = DBOHHOUser()
        cellphone_instance = DBCellphone()
        relation_instance = DBOHHOUserAndCellphoneRelation()

        the_get = Get()
        relation_id = the_get.get_id(self)
        username = ""
        cellphone_key = ""
        state = False
        if relation_id:
            relation = relation_instance.get_by_id(relation_id)
            if relation:
                state = relation.state
                user = user_instance.get_by_id(relation.user_id)
                username = user.username if user else ""
                cellphone = cellphone_instance.get_by_id(relation.cellphone_id)
                cellphone_key = cellphone.key if cellphone else ""

        return self.render(USER_AND_CELLPHONE_DELETE_HTML,
                           username=username,
                           cellphone_key=cellphone_key,
                           state=state,
                           relation_id=relation_id,
                           detail_url=USER_AND_CELLPHONE_DETAIL_URL,
                           list_url=USER_AND_CELLPHONE_LIST_URL,
                           delete_url=USER_AND_CELLPHONE_DELETE_URL
                           )
