from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.body_type import BodyType
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated


class BackstageBodyTypeDetailHandler(BaseHandler):
    def post(self):
        the_post = Post()
        instance = BodyType()
        body_type_id = the_post.get_id(self)
        name = the_post.get_name(self)
        body_type = instance.get(body_type_id)
        submit = self.get_body_argument("submit", None)
        delete_or_restore = self.get_body_argument("delete_or_restore", None)
        success = False
        if submit:
            data = dict()
            data["name"] = name
            success = instance.update(body_type, data)
        if delete_or_restore:
            if body_type.state:
                success = instance.delete(body_type)
            else:
                success = instance.restore(body_type)

        if success:
            return self.redirect(BASE_BODY_TYPE_LIST_URL)
        return self.redirect(BASE_BODY_TYPE_DETAIL_HTML + "?id=" + str(body_type_id))

    @authenticated
    def get(self):
        the_get = Get()
        body_type_id = the_get.get_id(self)
        name = ""
        state = False
        instance = BodyType()
        if body_type_id:
            body_type = instance.get(body_type_id)
            name = body_type.name
            state = body_type.state

        return self.render(BASE_BODY_TYPE_DETAIL_HTML,
                           name=name,
                           state=state,
                           body_type_id=body_type_id,
                           detail_url=BASE_BODY_TYPE_DETAIL_URL,
                           list_url=BASE_BODY_TYPE_LIST_URL
                           )
