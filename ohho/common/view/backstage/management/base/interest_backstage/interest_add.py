from tornado.web import authenticated

from ohho.common.logic.common.base.interest_backstage import InterestBackstage
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.base.constant import *

from ohho.common.view.common.parameters import Post
from ohho.common.view.common.parameters import Get
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate


class BackstageInterestAddHandler(BaseHandler):
    @backstage_authenticate
    def post(self):
        the_post = Post()
        parent_id = the_post.get_parent_id(self)
        name = the_post.get_name(self)
        instance = InterestBackstage()
        if name:
            data = dict()
            data["parent_id"] = parent_id
            data["name"] = name
            success = instance.add(data)
            if success:
                if parent_id == "1":
                    return self.redirect(BASE_INTEREST_BACKSTAGE_LIST_URL)
                else:   # 跳转详细中添加的跳转,只跳转到上一级
                    back_interest_id = parent_id
                    back_interest_parent_id = instance.get(parent_id).parent_id
                    # return self.redirect(BASE_INTEREST_BACKSTAGE_ADD_URL +"?id="+str(back_interest_id)+"&parent_id="+str(back_interest_parent_id))

        return self.redirect(BASE_INTEREST_BACKSTAGE_ADD_URL + "?id=" + str(parent_id))

    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        interest_id = the_get.get_id(self)
        parent_id = the_get.get_parent_id(self)
        sign =the_get.get_sign(self)
        name = ""
        instance = InterestBackstage()
        if not parent_id: # 如果不是从第一个页面
            obj_interest = instance.get_by_id(interest_id)
            parent_id = obj_interest.parent_id
            if str(parent_id) == "1" and str(sign) == "1":
                return self.redirect(BASE_INTEREST_BACKSTAGE_LIST_URL)
            print(parent_id)
            if interest_id:
                children_query = instance.get_by_parent_id(interest_id)
                state = True
                has_state = True
                children_query = instance.get_by_state(children_query, state, has_state)
        else:
            children_query = instance.get_by_parent_id(parent_id)
            interest_id = parent_id

        return self.render(BASE_INTEREST_BACKSTAGE_ADD_HTML,
                           add_url=BASE_INTEREST_BACKSTAGE_ADD_URL,
                           list_url=BASE_INTEREST_BACKSTAGE_LIST_URL,
                           parent_id=parent_id,
                           # name=name,
                           # interest_obj=interest_obj,
                           children_query=children_query,
                           interest_id=interest_id,
                           )
