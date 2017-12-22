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
        message = ""
        key = the_post.get_key(self)
        name = the_post.get_name(self)
        parent_id = the_post.get_parent_id(self)

        instance = InterestBackstage()
        parent = instance.get_by_id(parent_id)
        parent_name = parent.name if parent else "==未定义=="
        parent_key = parent.key if parent else "==未定义=="

        if key:
            obj = instance.get_by_key(key)
            if obj:
                message = "该数据已经存在了，请更改key值！"
            else:
                data = dict()
                data["key"] = key
                data["name"] = name
                if parent:
                    data["parent_id"] = parent_id

                success = instance.add(data)
                if success:
                    message = "添加数据成功！"
                    key = ""
                    name = ""
                else:
                    message = "添加数据失败！"
        else:
            message = "key不能为空！"

        return self.render(BASE_INTEREST_BACKSTAGE_ADD_HTML,
                           add_url=BASE_INTEREST_BACKSTAGE_ADD_URL,
                           list_url=BASE_INTEREST_BACKSTAGE_LIST_URL,
                           parent_id=parent_id,
                           parent_name=parent_name,
                           parent_key=parent_key,
                           key=key,
                           name=name,
                           message=message,
                           )


    @permission
    @backstage_authenticate
    def get(self):
        the_get = Get()
        parent_id = the_get.get_id(self)
        if not parent_id:
            parent_id = 1
        instance = InterestBackstage()
        obj = instance.get_by_id(parent_id)
        parent_name = obj.name if obj else "==未定义=="
        parent_key = obj.key if obj else "==未定义=="
        return self.render(BASE_INTEREST_BACKSTAGE_ADD_HTML,
                           add_url=BASE_INTEREST_BACKSTAGE_ADD_URL,
                           list_url=BASE_INTEREST_BACKSTAGE_LIST_URL,
                           parent_id=parent_id,
                           parent_name=parent_name,
                           parent_key=parent_key,
                           name="",
                           key="",
                           description="",
                           message="",
                           )
