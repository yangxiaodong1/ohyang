from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.watchword import Watchword
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.base.interest_backstage import InterestBackstage
from tornado.web import authenticated
from Tools.decorator import permission
from Tools.decorator import backstage_authenticate

class BackstageInterestDeleteHandler(BaseHandler):

    @backstage_authenticate
    def post(self):
        the_post = Post()
        key = the_post.get_key(self)
        parent_id = the_post.get_id(self)
        if parent_id:
            parent_id = int(parent_id)
        else:
            parent_id = 1
        instance = InterestBackstage()
        obj = instance.get_by_key(key)
        submit = the_post.get_submit(self)
        success = False
        if submit:
            if obj:
                success = instance.delete(obj)
                if success:
                    message = "删除数据成功！"
                else:
                    message = "删除数据失败！"
            else:
                message = "本数据已经被删除！"
        if parent_id:
            return self.redirect(BASE_INTEREST_BACKSTAGE_LIST_URL + "?id=" + str(parent_id))
        else:
            return self.redirect(BASE_INTEREST_BACKSTAGE_LIST_URL)


    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        the_id = the_get.get_id(self)
        instance = InterestBackstage()
        obj = instance.get_by_id(the_id)
        name = obj.name if obj else ""
        key = obj.key if obj else ""
        parent = instance.get_by_id(obj.parent_id) if obj else None
        parent_id = parent.id if parent else 0
        parent_name = parent.name if parent else ""
        parent_key = parent.key if parent else ""
        message = ""

        return self.render(BASE_INTEREST_BACKSTAGE_DELETE_HTML,
                           name=name,
                           key=key,
                           parent_id=parent_id,
                           parent_name=parent_name,
                           parent_key=parent_key,
                           delete_url=BASE_INTEREST_BACKSTAGE_DELETE_URL,
                           list_url=BASE_INTEREST_BACKSTAGE_LIST_URL,
                           message=message
                           )

