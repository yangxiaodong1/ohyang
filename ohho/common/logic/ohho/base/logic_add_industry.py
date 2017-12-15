from ohho.common.db.ohho.base.db_ohho_industry import DBOHHOIndustry
from ohho.common.logic.common.result import Result


class LogicAddIndustry(object):
    def __init__(self):
        self.industry = DBOHHOIndustry()

    def add(self, name):
        data = dict()
        data["name"] = name
        success = self.industry.add(data)
        if success:
            result = Result.result_success()
        else:
            result = Result.result_failed()
        return result
