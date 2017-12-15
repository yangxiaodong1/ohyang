from ohho.common.db.ohho.base.db_ohho_work_domain import DBOHHOWorkDomain
from ohho.common.logic.common.result import Result


class LogicAddWorkDomain(object):
    def __init__(self):
        self.work_domain = DBOHHOWorkDomain()

    def add(self, name):
        data = dict()
        data["name"] = name
        success = self.work_domain.add(data)
        if success:
            result = Result.result_success()
        else:
            result = Result.result_failed()
        return result
