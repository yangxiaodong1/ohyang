from ohho.common.view.common.parameters import Get
from ohho.common.view.backstage.base_handler import BaseHandler
from ohho.common.db.ohho.device.db_ohho_device import DBOHHODevice
from ohho.common.db.ohho.relation.db_ohho_user_and_device_relation import DBOHHOUserAndDeviceRelation
from tornado.web import authenticated
from Tools.ohho_datetime import OHHODatetime
from ohho.common.view.backstage.constant import *


class BackstageStatisticsDeviceHandler(BaseHandler):
    def post(self):
        pass

    @authenticated
    def get(self):
        device = DBOHHODevice()
        query = device.get_query()
        total_count = device.get_count(query)
        today_start = OHHODatetime.get_today_start()
        utc_today_start = OHHODatetime.beijing2utc(today_start)
        today_query = device.get_great_than_equal_changed_at(query, utc_today_start)
        today_count = device.get_count(today_query)

        relation = DBOHHOUserAndDeviceRelation()
        relation_query = relation.get_query()
        relation_query = relation.get_valid(relation_query)
        total_bind_count = relation.get_count(relation_query)
        today_bind_query = relation.get_great_than_equal_changed_at(relation_query, utc_today_start)
        today_bind_count = relation.get_count(today_bind_query)

        return self.render(STATISTICS_DEVICE_HTML,
                           total_count=total_count,
                           today_count=today_count,
                           today_bind_count=today_bind_count,
                           total_bind_count=total_bind_count,
                           )
