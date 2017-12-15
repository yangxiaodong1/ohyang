from ohho.common.db.ohho.db_cellphone import DBCellphone
from ohho.common.db.ohho.relation.db_ohho_user_and_cellphone_relation import DBOHHOUserAndCellphoneRelation
from tornado.web import authenticated

from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.relations.constant import *
from ohho.common.view.common.parameters import Post
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageUserAndCellphoneRelationAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        username = the_post.get_username(self)
        cellphone_key = the_post.get_cellphone_key(self)

        user_instance = DBOHHOUser()
        cellphone_instance = DBCellphone()
        relation_instance = DBOHHOUserAndCellphoneRelation()

        user = user_instance.get_by_username(username)
        cellphone_instance.set_key(cellphone_key)
        cellphone = cellphone_instance.get_by_key()
        if user and cellphone:
            relation = relation_instance.get_by_cellphone_and_user(cellphone.id, user.id)
            if not relation:
                data = dict()
                data["user_id"] = user.id
                data["cellphone_id"] = cellphone.id
                success = relation_instance.add(data)
                if success:
                    return self.redirect(USER_AND_CELLPHONE_LIST_URL)
            else:
                if not relation.state:
                    relation_instance.restore(relation)
                return self.redirect(USER_AND_CELLPHONE_LIST_URL)

        return self.redirect(USER_AND_CELLPHONE_ADD_URL)

    @permission
    @backstage_authenticate
    def get(self):
        user_instance = DBOHHOUser()
        cellphone_instance = DBCellphone()
        users_query = user_instance.get_query()
        users_query = user_instance.get_valid(users_query)
        cellphones_query = cellphone_instance.get_query()

        return self.render(USER_AND_CELLPHONE_ADD_HTML,
                           add_url=USER_AND_CELLPHONE_ADD_URL,
                           list_url=USER_AND_CELLPHONE_LIST_URL,
                           users_query=users_query,
                           cellphones_query=cellphones_query,
                           )
