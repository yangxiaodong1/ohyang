from ohho.common.logic.common.record.user_and_match_condition import UserAndMatchCondition
from ohho.common.logic.common.record.match_condition import MatchCondition
from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.detail_constant import SUCCESS, DEFAULT, FAILED

DEFAULT_USER_ID = 1


class LogicGetMatchCondition(object):
    def __init__(self):
        self.relation = UserAndMatchCondition()
        self.condition = MatchCondition()

    # @staticmethod
    # def get_query(user_id, name):
    #     query = DBOHHOMatchCondition.get_by_user(user_id)
    #     query = DBOHHOMatchCondition.get_by_name(query, name)
    #     query = DBOHHOMatchCondition.order_by_id_asc(query)
    #     query = DBOHHOMatchCondition.first(query)
    #     return query

    def get(self, user_id, name=None):
        relation = self.relation.get(user_id, name)
        if relation:
            result = Result.result_success()
        else:
            user_id = 1
            name = "test"
            relation = self.relation.get(user_id, name)
            if relation:
                result = Result.result_not_exist(DEFAULT)
            else:
                result = Result.result_failed()
        if relation:
            condition = self.condition.get_by_id(relation.match_condition_id)
            if condition:
                result["data"] = self.condition.get_information(condition)
        else:
            condition = None

        return result, condition
