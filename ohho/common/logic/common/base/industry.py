from ohho.common.db.ohho.base.db_ohho_industry import DBOHHOIndustry
from ohho.common.logic.common.base.base_class import BaseClass


class Industry(BaseClass):
    def __init__(self):
        super(Industry, self).__init__(DBOHHOIndustry)
