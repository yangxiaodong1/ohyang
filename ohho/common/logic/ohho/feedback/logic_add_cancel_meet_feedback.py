from Tools.ohho_operation import OHHOOperation
from ohho.common.db.ohho.user.db_ohho_user_impression import DBOHHOUserImpression
from ohho.common.db.ohho.record.db_ohho_record_match_apply import DBOHHORecordMatchApply
from ohho.common.db.ohho.feedback.db_ohho_cancel_meet_feedback import DBOHHOCancelMeetFeedback
from ohho.common.logic.common.result import Result


class LogicAddCancelMeetFeedback(object):
    def __init__(self):
        self.feedback = DBOHHOCancelMeetFeedback()
        self.apply = DBOHHORecordMatchApply()

    def add_feedback(self, user_id, friend_user_id, apply_id, reason, content, category):
        data = dict()
        data["user_id"] = user_id
        data["another_user_id"] = friend_user_id
        data["apply_id"] = apply_id
        data["reason"] = reason
        data["message"] = content

        if self.apply.get_by_id(apply_id):
            success = self.feedback.add(data)
            category_list = OHHOOperation.json2list(category)
            impression_instance = DBOHHOUserImpression()
            for c in category_list:
                if c:
                    temp = dict()
                    temp["type"] = 1
                    temp["content_id"] = int(c)
                    temp["apply_id"] = apply_id
                    temp["user_id"] = user_id
                    temp["another_user_id"] = friend_user_id
                    impression_instance.add(temp)

            if success:
                result = Result.result_success()
            else:
                result = Result.result_failed()
        else:
            result = Result.result_failed("no valid apply!")
        return result
