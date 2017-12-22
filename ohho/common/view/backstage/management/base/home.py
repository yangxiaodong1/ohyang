from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.view.backstage.constant import MANAGEMENT_BASE_HOME_HTML
from ohho.common.view.backstage.management.base.constant import *
from tornado.web import authenticated


class BackstageBaseHomeHandler(BaseHandler):
    def post(self):
        pass

    @authenticated
    def get(self):
        return self.render(MANAGEMENT_BASE_HOME_HTML,
                           base_country_code_backstage_list_url=BASE_COUNTRY_CODE_BACKSTAGE_LIST_URL,
                           base_interest_backstage_list_url=BASE_INTEREST_BACKSTAGE_LIST_URL,
                           base_sensitive_backstage_list_url=BASE_SENSITIVE_BACKSTAGE_LIST_URL,
                           base_hint_backstage_list_url=BASE_HINT_BACKSTAGE_LIST_URL,
                           base_userdisplayconfig_list_url=BASE_USER_DISPLAY_CONFIG_LIST_URL,
                           base_watchword_list_url=BASE_WATCHWORD_LIST_URL,
                           base_drink_list_url=BASE_DRINK_LIST_URL,
                           base_smoke_list_url=BASE_SMOKE_LIST_URL,
                           base_industry_list_url=BASE_INDUSTRY_LIST_URL,
                           base_profession_list_url=BASE_PROFESSION_LIST_URL,
                           base_body_type_list_url=BASE_BODY_TYPE_LIST_URL,
                           base_work_domain_list_url=BASE_WORK_DOMAIN_LIST_URL,
                           base_match_condition_list_url=BASE_MATCH_CONDITION_LIST_URL,
                           )
