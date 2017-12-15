from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.common.parameters import Post
from tornado.web import authenticated
from ohho.common.logic.common.base.industry import Industry
from ohho.common.view.backstage.management.base.constant import BASE_INDUSTRY_ADD_URL
from ohho.common.view.backstage.management.base.constant import BASE_INDUSTRY_ADD_HTML
from ohho.common.view.backstage.management.base.constant import BASE_INDUSTRY_LIST_URL


class BackstageIndustryAddHandler(BaseHandler):
    def post(self):
        the_post = Post()
        name = the_post.get_name(self)
        instance = Industry()
        if name:
            data = dict()
            data["name"] = name
            success = instance.add(data)
            if success:
                return self.redirect(BASE_INDUSTRY_LIST_URL)

        return self.redirect(BASE_INDUSTRY_ADD_URL)

    @authenticated
    def get(self):
        return self.render(BASE_INDUSTRY_ADD_HTML,
                           add_url=BASE_INDUSTRY_ADD_URL,
                           list_url=BASE_INDUSTRY_LIST_URL
                           )
