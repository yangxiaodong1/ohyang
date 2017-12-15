from DB.redis.operation import RedisDB
from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_log import OHHOLog
from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.record.match_agree import MatchAgree
from ohho.common.logic.common.record.match_apply import MatchApply
from ohho.common.logic.common.record.match_refuse import MatchRefuse
from ohho.common.logic.common.user import User
from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.constant import *


class LogicPollingGetMatchApply(object):
    def __init__(self):
        self.agree = MatchAgree()
        self.apply = MatchApply()
        self.refuse = MatchRefuse()
        self.meet = Meet()
        self.user = User()

    def get(self, user_id, base_url):
        data = list()
        result = Result.result_success()
        user = self.user.get_by_id(user_id)
        current_timestamp = OHHODatetime.get_current_timestamp()
        timestamp = RedisDB.hash_get(REDIS_APPLY_TIMESTAMP_NAME, user_id)

        if not timestamp:
            timestamp = current_timestamp - 5 * 60 * 1000

        OHHOLog.print_log(timestamp)
        RedisDB.hash_set(REDIS_APPLY_TIMESTAMP_NAME, user_id, current_timestamp)
        # OHHOLog.print_log("start")
        # OHHOLog.print_log(user_id)
        if user:
            # OHHOLog.print_log("user")
            apply_you = self.apply.polling_get_by_another(user, int(timestamp), current_timestamp)
            OHHOLog.print_log(current_timestamp)
            OHHOLog.print_log(current_timestamp)
            # OHHOLog.print_log(int(timestamp))
            # OHHOLog.print_log(current_timestamp)
            # OHHOLog.print_log(self.apply.apply.is_empty(apply_you))
            if not self.apply.apply.is_empty(apply_you):
                OHHOLog.print_log("has valid apply!")
                for apply in apply_you:
                    OHHOLog.print_log(apply.id)
                    if self.meet.has_agree_apply(apply.one_user_id) or self.meet.has_agree_apply(apply.another_user_id):
                        # OHHOLog.print_log("has agree apply!")
                        continue

                    if self.meet.has_valid_apply(apply.one_user_id, apply.another_user_id):
                        # OHHOLog.print_log("has valid apply 2!")
                        OHHOLog.print_log(apply.id)
                        user_dict = self.user.get_user_basic_information(apply.one_user_id, base_url)
                        if user_dict:
                            data.append(user_dict)
        if data:
            # OHHOLog.print_log("has data")
            # OHHOLog.print_log(data)
            result["data"] = data
        else:
            pass
            OHHOLog.print_log("not data")
        return result
