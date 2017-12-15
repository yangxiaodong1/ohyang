from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.watchword import Watchword
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.base.interest_backstage import InterestBackstage
from tornado.web import authenticated
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageInterestDetailHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        interest_id = the_post.get_id(self)
        parent_id = the_post.get_parent_id(self)
        name = the_post.get_name(self)
        instance = InterestBackstage()
        interest_obj = instance.get(interest_id)
        submit = the_post.get_submit(self)
        delete_or_restore = the_post.get_delete_or_restore(self)
        success = False
        if submit:
            data = dict()
            if name:
                data["name"] = name
            success = instance.update(interest_obj, data)
        if delete_or_restore:
            if interest_obj.name:
                success = instance.delete(interest_obj)
            else:
                success = instance.restore(interest_obj)

        if success:
            # return self.redirect(BASE_INTEREST_BACKSTAGE_LIST_URL)
            # id = interest_id
            # back_interest_id = parent_id
            back_interest_id = instance.get(interest_id).parent_id
            # print(back_parent_id)
            if back_interest_id != 1:
                back_parent_id = instance.get(back_interest_id).parent_id
                return self.redirect(
                    BASE_INTEREST_BACKSTAGE_DETAIL_URL + "?id=" + str(back_interest_id) + "&parent_id=" + str(
                        back_parent_id))
            else:
                return self.redirect(BASE_INTEREST_BACKSTAGE_LIST_URL)
        return self.redirect(BASE_INTEREST_BACKSTAGE_DETAIL_HTML + "?id=" + str(interest_id))

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        interest_id = the_get.get_id(self)
        parent_id = the_get.get_parent_id(self)
        name = ""
        instance = InterestBackstage()
        if interest_id:
            interest_obj = instance.get(interest_id)
            children_query = instance.get_by_parent_id(interest_id)
            state = True
            has_state = True
            children_query = instance.get_by_state(children_query,state,has_state)
            name = interest_obj.name

        return self.render(BASE_INTEREST_BACKSTAGE_DETAIL_HTML,
                           name=name,
                           parent_id=parent_id,
                           interest_id=interest_id,
                           detail_url=BASE_INTEREST_BACKSTAGE_DETAIL_URL,
                           list_url=BASE_INTEREST_BACKSTAGE_LIST_URL,
                           interest_obj =interest_obj,
                           children_query = children_query,
                           add_url=BASE_INTEREST_BACKSTAGE_ADD_URL,

                           )
