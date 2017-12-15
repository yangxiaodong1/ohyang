from Tools.ohho_log import OHHOLog
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.db.ohho.record.db_ohho_record_match_condition import DBOHHORecordMatchCondition
from ohho.common.db.ohho.record.db_ohho_record_user_and_match_condition import DBOHHORecordUserAndMatchCondition
from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.detail_constant import ADD_USER_AND_MATCH_CONDITION_FAILED
from ohho.common.logic.ohho.detail_constant import ADD_USER_AND_MATCH_CONDITION_SUCCESS
from ohho.common.logic.ohho.detail_constant import PARAMETERS_ARE_INVALID
from ohho.common.logic.ohho.detail_constant import USER_AND_MATCH_CONDITION_EXIST


class UserAndMatchCondition(object):
    def __init__(self):
        self.relation = DBOHHORecordUserAndMatchCondition()
        self.condition = DBOHHORecordMatchCondition()
        self.user = DBOHHOUser()

    def get_nearest_match_relation_by_user(self, user_id):
        query = self.relation.get_query()
        query = self.relation.filter_by_user(query, user_id)
        query = self.relation.order_by_id_desc(query)
        return self.relation.first(query)

    def add(self, user_id, name, match_condition_id):
        """
        用户ID，名称唯一确定一条值，match_condition可以更改
        :param data: name, user_id, match_condition_id
        :return:
        """
        if user_id:
            relation = self.get_nearest_match_relation_by_user(user_id)
            if relation:
                result = Result.result_exist(USER_AND_MATCH_CONDITION_EXIST)
                result["data"] = relation
            else:
                data = dict()
                data["user_id"] = user_id
                data["match_condition_id"] = match_condition_id
                if name:
                    data["name"] = name
                success = self.relation.add(data)
                if success:
                    result = Result.result_success()
                    relation = self.get_nearest_match_relation_by_user(user_id)
                    result["data"] = relation
                else:
                    result = Result.result_failed()
                    result["data"] = None
        else:
            result = Result.result_failed(PARAMETERS_ARE_INVALID)
            result["data"] = None
        return result


        # if user_id and name:
        #     query = self.relation.get_query()
        #     query = self.relation.filter_by_user(query, user_id)
        #     query = self.relation.filter_by_name(query, name)
        #     query = self.relation.order_by_id_asc(query)
        #     relation = self.relation.first(query)
        #     if relation:
        #         OHHOLog.print_log(USER_AND_MATCH_CONDITION_EXIST)
        #         result = Result.result_exist(USER_AND_MATCH_CONDITION_EXIST)
        #         result["data"] = relation
        #     else:
        #         data = dict()
        #         data["user_id"] = user_id
        #         data["name"] = name
        #         data["match_condition_id"] = match_condition_id
        #         success = self.relation.add(data)
        #         if success:
        #             OHHOLog.print_log(ADD_USER_AND_MATCH_CONDITION_SUCCESS)
        #             result = Result.result_success()
        #             relation = self.get(user_id, name)
        #             result["data"] = relation
        #         else:
        #             OHHOLog.print_log(ADD_USER_AND_MATCH_CONDITION_FAILED)
        #             result = Result.result_failed()
        #             result["data"] = None
        # else:
        #     OHHOLog.print_log(PARAMETERS_ARE_INVALID)
        #     result = Result.result(-2, PARAMETERS_ARE_INVALID)
        #     result["data"] = None
        # return result

    def get(self, user_id, name=None):
        if user_id:
            query = self.relation.get_query()
            query = self.relation.filter_by_user(query, user_id)
            if name:
                query = self.relation.filter_by_name(query, name)
            query = self.relation.order_by_id_desc(query)
            query = self.relation.first(query)
            return query
        else:
            OHHOLog.print_log(PARAMETERS_ARE_INVALID)
        return None

    def get_by_id(self, user_and_match_condition_id):
        return self.relation.get_by_id(user_and_match_condition_id)

    def update(self, relation, data):
        return self.relation.update(relation, data)

    def delete(self, instance):
        return self.relation.delete(instance)

    def find(self, username, name, match_condition_ids):
        query = self.relation.get_query()
        if username:
            users = self.user.find_by_username(username)
            user_id_list = list()
            if not self.user.is_empty(users):
                user_id_list = [user.id for user in users]
            query = self.relation.find_by_user(query, user_id_list)

        if name:
            query = self.relation.find_by_name(query, name)

        if match_condition_ids:
            match_condition_id_list = match_condition_ids.split(",")
            query = self.relation.find_by_match_condition(query, match_condition_id_list)

        return query

    def get_some(self, query, offset, limit):
        return self.relation.get_some(query, offset, limit)

    def get_match_condition(self, match_condition_id):
        return self.condition.get_by_id(match_condition_id)
