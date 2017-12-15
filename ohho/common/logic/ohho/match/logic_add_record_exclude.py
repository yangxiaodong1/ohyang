from ohho.common.db.ohho.record.db_ohho_record_exclude import DBOHHORecordExclude
from ohho.common.logic.common.result import Result


class LogicAddRecordExclude(object):
    def __init__(self):
        self.exclude = DBOHHORecordExclude()

    def add_exclude(self, user_id, exclude_user_id, match_condition_id):
        data = dict()
        data["user_id"] = user_id
        data["exclude_user_id"] = exclude_user_id
        data["match_condition_id"] = match_condition_id
        success = self.exclude.add(data)
        if success:
            result = Result.result_success()
        else:
            result = Result.result_failed()

        return result
