from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.drink import Drink
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated


class BackstageDrinkDetailHandler(BaseHandler):
    def post(self):
        the_post = Post()
        drink_id = the_post.get_id(self)
        name = the_post.get_name(self)
        instance = Drink()
        drink = instance.get(drink_id)
        submit = the_post.get_submit(self)
        delete_or_restore = the_post.get_delete_or_restore(self)
        success = False
        if submit:
            data = dict()
            data["name"] = name
            success = instance.update(drink, data)
        if delete_or_restore:
            if drink.state:
                success = instance.delete(drink)
            else:
                success = instance.restore(drink)

        if success:
            return self.redirect(BASE_DRINK_LIST_URL)
        return self.redirect(BASE_DRINK_DETAIL_HTML + "?id=" + str(drink_id))

    @authenticated
    def get(self):
        the_get = Get()
        drink_id = the_get.get_id(self)
        name = ""
        state = False
        instance = Drink()
        if drink_id:
            drink = instance.get(drink_id)
            name = drink.name
            state = drink.state

        return self.render(BASE_DRINK_DETAIL_HTML,
                           name=name,
                           state=state,
                           drink_id=drink_id,
                           detail_url=BASE_DRINK_DETAIL_URL,
                           list_url=BASE_DRINK_LIST_URL
                           )
