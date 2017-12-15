from ohho.common.db.ohho.base.db_ohho_watchword import DBOHHOWatchword
from ohho.common.logic.common.base.base_class import BaseClass


class Watchword(BaseClass):
    def __init__(self):
        super(Watchword, self).__init__(DBOHHOWatchword)

