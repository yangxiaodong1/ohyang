from  ohho.common.db.ohho.record.db_ohho_record_match_apply import DBOHHORecordMatchApply
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.constant import *
from Tools.ohho_log import OHHOLog
from Tools.ohho_operation import OHHOOperation


class LogicMeetState(object):
    def __init__(self):
        self.meet = Meet()
        self.user = User()
        self.apply = DBOHHORecordMatchApply()

    def meet_state(self, user_id, base_url):
        result = Result.result_success()

        result["state"], apply_id = self.meet.get_user_state(user_id)
        result["apply_id"] = apply_id
        if apply_id:
            countdown = self.meet.get_countdown(apply_id)
            # result = OHHOOperation.dict_add_dict(result, temp)
            apply = self.apply.get_by_id(apply_id)
            if apply:
                friend_user_id = apply.another_user_id if apply.one_user_id == int(user_id) else apply.one_user_id
                result["friend_state"], temp = self.meet.get_user_state(friend_user_id, result["apply_id"])
                if result["state"] == PUSH_STATE_TYPE_END_MEET:
                    pass
                else:
                    friend_user_information = self.user.get_basic_user_information(friend_user_id,
                                                                                   base_url)
                    friend_user_information["user_id"] = friend_user_id
                    friend_user_information["apply_id"] = apply_id
                    friend_user_information = OHHOOperation.dict_add_dict(friend_user_information, countdown)

                    result["friend_user_information"] = friend_user_information
        OHHOLog.print_log(result)
        return result
