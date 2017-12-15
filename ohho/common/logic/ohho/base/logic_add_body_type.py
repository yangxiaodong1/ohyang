from ohho.common.db.ohho.base.db_ohho_body_type import DBOHHOBodyType
from ohho.common.logic.common.result import Result


class LogicAddBodyType(object):
    def __init__(self):
        self.body_type = DBOHHOBodyType()

    def add(self, name):
        data = dict()
        data["name"] = name
        success = self.body_type.add(data)
        if success:
            result = Result.result_success()
        else:
            result = Result.result_failed()
        return result
