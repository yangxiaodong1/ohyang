from ohho.common.view.common.parameters import Post
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.logic.common.user import User
from tornado.web import authenticated
from Tools.decorator import statistic, backstage_authenticate
from ohho.common.view.backstage.constant import *
from Tools.ohho_log import OHHOLog
from Tools.ohho_log import OHHODatetime


class BackstageHomeHandler(BaseHandler):
    def post(self):
        pass

    @backstage_authenticate
    @statistic
    def get(self):
        username = self.current_user
        user = User()
        user_object = user.get_by_username(username)
        if user_object:
            cellphone = user_object.cellphone
            country_code = user.get_country_code_by_id(user_object.country_code_id)
            if not country_code:
                country_code = "+86"
            last_login = OHHODatetime.clock2string(OHHODatetime.utc2beijing(user_object.last_login))
        else:
            cellphone = ""
            country_code = "+86"
            last_login = ""
        cellphone = cellphone if cellphone else ""
        phone = country_code + "-" + cellphone

        return self.render(BACKSTAGE_HOME_HTML,
                           phone=phone,
                           last_login=last_login,
                           user_url=MANAGEMENT_USER_LIST_URL,
                           device_url=MANAGEMENT_DEVICE_LIST_URL,
                           cellphone_url=MANAGEMENT_CELLPHONE_LIST_URL,
                           relation_url=MANAGEMENT_RELATION_HOME_URL,
                           base_home_url=MANAGEMENT_BASE_HOME_URL,
                           permission_home_url=MANAGEMENT_PERMISSION_HOME_URL,
                           statistics_user=STATISTICS_USER_URL,
                           statistics_device=STATISTICS_DEVICE_URL,
                           )
