from ohho.common.logic.common.user import User
from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.record.match_agree import MatchAgree
from ohho.common.logic.common.record.match_apply import MatchApply
from ohho.common.logic.common.record.match_refuse import MatchRefuse
from ohho.common.logic.common.result import Result


class LogicPollingGetMatchState(object):
    def __init__(self):
        self.agree = MatchAgree()
        self.apply = MatchApply()
        self.refuse = MatchRefuse()
        self.meet = Meet()
        self.user = User()

    def get(self, user_id, friend_user_id, is_apply, base_url):
        result = Result.result_success()

        user = self.user.get_by_id(user_id)
        if user:
            if int(is_apply):
                apply = self.apply.get_nearest(user_id, friend_user_id)
            else:
                apply = self.apply.get_nearest(friend_user_id, user_id)
            if apply:
                agree = self.agree.get(apply.id)
                refuse = self.refuse.get(apply.id)
                if self.meet.is_meet_by_apply(apply.id):
                    result["state"] = 6  # 见面
                else:
                    if agree:
                        if not refuse:
                            result["state"] = 1  # "agree"
                        else:
                            result["state"] = 3  # "cancel"
                    else:
                        if refuse:
                            result["state"] = 2  # "refuse"
                        else:
                            result["state"] = 4  # "default"
            else:
                result["state"] = 5  # "no such apply"

            if result["state"] in [1, 6]:
                result["data"] = self.user.get_user_basic_information(friend_user_id, base_url)

        return result
