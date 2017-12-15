from Tools.ohho_operation import OHHOOperation
from ohho.common.db.ohho.feedback.db_ohho_feedback import DBOHHOFeedback
from ohho.common.logic.common.result import Result


class LogicAddFeedback(object):
    def __init__(self):
        self.feedback = DBOHHOFeedback()

    def add_feedback(self, user_id, feedback_type, content):
        data = dict()
        data["user_id"] = user_id
        data["feedback_type"] = feedback_type
        data["content"] = OHHOOperation.to_bytes(content)
        success = self.feedback.add(data)
        if success:
            result = Result.result_success()
        else:
            result = Result.result_failed()
        return result
