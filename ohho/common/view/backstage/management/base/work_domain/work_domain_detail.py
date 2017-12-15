from ohho.common.view.common.parameters import Get, Post
from ohho.common.view.backstage.management.base.constant import *
from ohho.common.logic.common.base.work_domain import WorkDomain
from ohho.common.view.backstage.base_handler import BaseHandler
from tornado.web import authenticated


class BackstageWorkDomainDetailHandler(BaseHandler):
    def post(self):
        instance = WorkDomain()
        the_post = Post()
        work_domain_id = the_post.get_id(self)
        name = the_post.get_name(self)
        work_domain = instance.get(work_domain_id)
        submit = self.get_body_argument("submit", None)
        delete_or_restore = self.get_body_argument("delete_or_restore", None)
        success = False
        if submit:
            data = dict()
            data["name"] = name
            success = instance.update(work_domain, data)
        if delete_or_restore:
            if work_domain.state:
                success = instance.delete(work_domain)
            else:
                success = instance.restore(work_domain)

        if success:
            return self.redirect(BASE_WORK_DOMAIN_LIST_URL)
        return self.redirect(BASE_WORK_DOMAIN_DETAIL_HTML + "?id=" + str(work_domain_id))

    @authenticated
    def get(self):
        the_get = Get()
        work_domain_id = the_get.get_id(self)
        name = ""
        state = False
        instance = WorkDomain()
        if work_domain_id:
            work_domain = instance.get(work_domain_id)
            name = work_domain.name
            state = work_domain.state

        return self.render(BASE_WORK_DOMAIN_DETAIL_HTML,
                           name=name,
                           state=state,
                           work_domain_id=work_domain_id,
                           detail_url=BASE_WORK_DOMAIN_DETAIL_URL,
                           list_url=BASE_WORK_DOMAIN_LIST_URL
                           )
