from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.industry import Industry
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated


class BackstageIndustryDetailHandler(BaseHandler):
    def post(self):
        the_post = Post()
        instance = Industry()
        industry_id = the_post.get_id(self)
        name = the_post.get_name(self)
        industry = instance.get(industry_id)
        submit = self.get_body_argument("submit", None)
        delete_or_restore = self.get_body_argument("delete_or_restore", None)
        success = False
        if submit:
            data = dict()
            data["name"] = name
            success = instance.update(industry, data)
        if delete_or_restore:
            if industry.state:
                success = instance.delete(industry)
            else:
                success = instance.restore(industry)

        if success:
            return self.redirect(BASE_SMOKE_LIST_URL)
        return self.redirect(BASE_SMOKE_DETAIL_HTML + "?id=" + str(industry_id))

    @authenticated
    def get(self):
        the_get = Get()
        industry_id = the_get.get_id(self)
        name = ""
        state = False
        instance = Industry()
        if industry_id:
            industry = instance.get(industry_id)
            name = industry.name
            state = industry.state

        return self.render(BASE_SMOKE_DETAIL_HTML,
                           name=name,
                           state=state,
                           industry_id=industry_id,
                           detail_url=BASE_SMOKE_DETAIL_URL,
                           list_url=BASE_SMOKE_LIST_URL
                           )
