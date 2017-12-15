from ohho.common.logic.common.record.match_condition import MatchCondition
from ohho.common.logic.common.record.user_and_match_condition import UserAndMatchCondition
from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.detail_constant import MATCH_CONDITION_NOT_EXIST
from ohho.common.logic.ohho.detail_constant import ADD_FAILED
from Tools.ohho_log import OHHOLog


class LogicAddMatchCondition(object):
    def __init__(self):
        self.match_condition = MatchCondition()
        self.relation = UserAndMatchCondition()

    def add(self, user_id, name, condition_dict):
        OHHOLog.print_log(condition_dict)
        relation = self.relation.get_nearest_match_relation_by_user(user_id)
        if relation:
            condition = self.match_condition.get_by_id(relation.match_condition_id)
            if not condition:
                success = self.match_condition.add(condition_dict)
                if success:
                    OHHOLog.print_log("add match condition successfully!")
                    return Result.result_success()
                else:
                    return Result.result_failed(ADD_FAILED)
            else:
                success = self.match_condition.update(condition, condition_dict)
                if success:
                    OHHOLog.print_log("update match condition successfully!")
                    return Result.result_success("update successfully!")
                else:
                    return Result.result_failed("update failed!")
        else:
            return Result.result_failed(MATCH_CONDITION_NOT_EXIST)

            # if condition:
            #     relation = self.relation.add(user_id, name, condition.id)
            #     if relation:
            #         OHHOLog.print_log("add user and match condition relation successfully!")
            #         return Result.result_success()
            #     else:
            #         return Result.result_failed("add relation failed!")
            # else:
            #     OHHOLog.print_log("not find match condition!")
            #     return Result.result_not_exist(MATCH_CONDITION_NOT_EXIST)
