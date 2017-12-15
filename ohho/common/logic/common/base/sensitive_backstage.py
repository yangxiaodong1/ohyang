from ohho.common.db.ohho.base.db_ohho_sensitive import DBOHHOSensitive
# from DB.mysql.models.ohho.model_ohho_watchword import OHHOWatchword
from ohho.common.logic.common.base.base_class import BaseClass


class SensitiveBackstage(BaseClass):
    def __init__(self):
        super(SensitiveBackstage, self).__init__(DBOHHOSensitive)
