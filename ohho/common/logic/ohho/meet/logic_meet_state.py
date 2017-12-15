from  ohho.common.db.ohho.record.db_ohho_record_match_apply import DBOHHORecordMatchApply
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.constant import *
from Tools.ohho_log import OHHOLog


class LogicMeetState(object):
    def __init__(self):
        self.meet = Meet()
        # self.meeting = DBOHHORecordMatchMeeting()
        # self.meet = DBOHHORecordMatchMeet()
        # self.meet_end = DBOHHORecordMatchMeetEnd()
        self.user = User()
        self.apply = DBOHHORecordMatchApply()

    # def get_user_state(self, user_id, apply_id=0):
    #     if apply_id:
    #         query_meeting = self.meeting.get_valid_by_apply_and_user(apply_id, user_id)
    #         if query_meeting:
    #             state = PUSH_STATE_TYPE_MEETING
    #         else:
    #             query_meet = self.meet.get_by_apply_and_user(apply_id, user_id)
    #             query_meet_end = self.meet_end.get_by_apply_and_user(apply_id, user_id)
    #             if query_meet and not query_meet_end:
    #                 state = PUSH_STATE_TYPE_MET
    #             else:
    #                 state = PUSH_STATE_TYPE_END_MEET
    #     else:
    #         query_meet = self.meet.get_valid_and_nearest_by_user(user_id)
    #         if query_meet:
    #             OHHOLog.print_log(query_meet.apply_id)
    #             OHHOLog.print_log(user_id)
    #             query_meet_end = self.meet_end.get_by_apply_and_user(query_meet.apply_id, user_id)
    #             OHHOLog.print_log(query_meet_end)
    #         else:
    #             query_meet_end = None
    #         query_meeting = self.meeting.get_valid_and_nearest_by_user(user_id)
    #
    #         if query_meeting:
    #             apply_id = query_meeting.apply_id
    #             OHHOLog.print_log(apply_id)
    #             state = PUSH_STATE_TYPE_MEETING
    #         elif query_meet and not query_meet_end:
    #             apply_id = query_meet.apply_id
    #             state = PUSH_STATE_TYPE_MET
    #         else:
    #             state = PUSH_STATE_TYPE_END_MEET
    #     return state, apply_id

    def meet_state(self, user_id, base_url):
        result = Result.result_success()

        result["state"], apply_id = self.meet.get_user_state(user_id)
        result["apply_id"] = apply_id
        if apply_id:
            apply = self.apply.get_by_id(apply_id)
            if apply:
                friend_user_id = apply.another_user_id if apply.one_user_id == int(user_id) else apply.one_user_id
                result["friend_state"], temp = self.meet.get_user_state(friend_user_id, result["apply_id"])
                if result["state"] == PUSH_STATE_TYPE_END_MEET:
                    pass
                else:
                    result["friend_user_information"] = self.user.get_duplex_agree_user_information(friend_user_id,
                                                                                                    apply_id,
                                                                                                    base_url)
        OHHOLog.print_log(result)
        return result
