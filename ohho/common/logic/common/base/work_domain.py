from ohho.common.db.ohho.base.db_ohho_work_domain import DBOHHOWorkDomain
from ohho.common.logic.common.base.base_class import BaseClass


class WorkDomain(BaseClass):
    def __init__(self):
        super(WorkDomain, self).__init__(DBOHHOWorkDomain)
