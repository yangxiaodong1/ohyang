from ohho.common.db.ohho.base.db_ohho_smoke import DBOHHOSmoke
from ohho.common.logic.common.result import Result


class LogicAddSmoke(object):
    def __init__(self):
        self.smoke = DBOHHOSmoke()

    def add(self, name):
        data = dict()
        data["name"] = name
        success = self.smoke.add(data)
        if success:
            result = Result.result_success()
        else:
            result = Result.result_failed()
        return result
