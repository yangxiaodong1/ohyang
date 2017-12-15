from Tools.ohho_operation import OHHOOperation
from ohho.common.db.ohho.report.db_ohho_report import DBOHHOReport
from ohho.common.logic.common.result import Result


class LogicAddReport(object):
    def __init__(self):
        self.report = DBOHHOReport()

    def add_report(self, user_id, reported_user_id, report_type, content):
        data = dict()
        data["user_id"] = user_id
        data["reported_user_id"] = reported_user_id
        data["report_type"] = report_type
        data["content"] = OHHOOperation.to_bytes(content)
        success = self.report.add(data)
        if success:
            result = Result.result_success()
        else:
            result = Result.result_failed()
        return result
