from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.common.parameters import Post
from tornado.web import authenticated
from ohho.common.logic.common.base.body_type import BodyType
from ohho.common.view.backstage.management.base.constant import BASE_BODY_TYPE_ADD_URL
from ohho.common.view.backstage.management.base.constant import BASE_BODY_TYPE_ADD_HTML
from ohho.common.view.backstage.management.base.constant import BASE_BODY_TYPE_LIST_URL


class BackstageBodyTypeAddHandler(BaseHandler):
    def post(self):
        the_post = Post()
        instance = BodyType()
        name = the_post.get_name(self)
        if name:
            data = dict()
            data["name"] = name
            success = instance.add(data)
            if success:
                return self.redirect(BASE_BODY_TYPE_LIST_URL)

        return self.redirect(BASE_BODY_TYPE_ADD_URL)

    @authenticated
    def get(self):
        return self.render(BASE_BODY_TYPE_ADD_HTML,
                           add_url=BASE_BODY_TYPE_ADD_URL,
                           list_url=BASE_BODY_TYPE_LIST_URL
                           )
