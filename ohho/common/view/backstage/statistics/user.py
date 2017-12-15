from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from tornado.web import authenticated
from Tools.ohho_datetime import OHHODatetime
from ohho.common.view.backstage.constant import *


class BackstageStatisticsUserHandler(BaseHandler):
    def post(self):
        pass

    @authenticated
    def get(self):
        user = DBOHHOUser()
        query = user.get_query()
        total_count = user.get_count(query)
        today_start = OHHODatetime.get_today_start()
        utc_today_start = OHHODatetime.beijing2utc(today_start)
        today_query = user.get_great_than_equal_created_at(query, utc_today_start)
        today_count = user.get_count(today_query)

        return self.render(STATISTICS_USER_HTML,
                           total_count=total_count,
                           today_count=today_count,
                           )
