from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.profession import Profession
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated


class BackstageProfessionDetailHandler(BaseHandler):
    def post(self):
        instance = Profession()
        the_post = Post()
        profession_id = the_post.get_id(self)
        name = the_post.get_name(self)
        profession = instance.get(profession_id)
        submit = self.get_body_argument("submit", None)
        delete_or_restore = self.get_body_argument("delete_or_restore", None)
        success = False
        if submit:
            data = dict()
            data["name"] = name
            success = instance.update(profession, data)
        if delete_or_restore:
            if profession.state:
                success = instance.delete(profession)
            else:
                success = instance.restore(profession)

        if success:
            return self.redirect(BASE_PROFESSION_LIST_URL)
        return self.redirect(BASE_PROFESSION_DETAIL_HTML + "?id=" + str(profession_id))

    @authenticated
    def get(self):
        the_get = Get()
        profession_id = the_get.get_id(self)
        name = ""
        state = False
        instance = Profession()
        if profession_id:
            profession = instance.get(profession_id)
            name = profession.name
            state = profession.state

        return self.render(BASE_PROFESSION_DETAIL_HTML,
                           name=name,
                           state=state,
                           profession_id=profession_id,
                           detail_url=BASE_PROFESSION_DETAIL_URL,
                           list_url=BASE_PROFESSION_LIST_URL
                           )
