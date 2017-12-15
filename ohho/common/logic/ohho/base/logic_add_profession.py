from ohho.common.db.ohho.base.db_ohho_profession import DBOHHOProfession
from ohho.common.logic.common.result import Result


class LogicAddProfession(object):
    def __init__(self):
        self.profession = DBOHHOProfession()

    def add(self, name):
        data = dict()
        data["name"] = name
        success = self.profession.add(data)
        if success:
            result = Result.result_success()
        else:
            result = Result.result_failed()
        return result
