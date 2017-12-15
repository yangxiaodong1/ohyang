from tornado.web import authenticated

from ohho.common.logic.common.base.drink import Drink
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.management.base.constant import BASE_DRINK_ADD_HTML
from ohho.common.view.backstage.management.base.constant import BASE_DRINK_ADD_URL
from ohho.common.view.backstage.management.base.constant import BASE_DRINK_LIST_URL
from ohho.common.view.common.parameters import Post


class BackstageDrinkAddHandler(BaseHandler):
    def post(self):
        the_post = Post()
        name = the_post.get_name(self)
        instance = Drink()
        if name:
            data = dict()
            data["name"] = name
            success = instance.add(data)
            if success:
                return self.redirect(BASE_DRINK_LIST_URL)

        return self.redirect(BASE_DRINK_ADD_URL)

    @authenticated
    def get(self):
        return self.render(BASE_DRINK_ADD_HTML,
                           add_url=BASE_DRINK_ADD_URL,
                           list_url=BASE_DRINK_LIST_URL
                           )
