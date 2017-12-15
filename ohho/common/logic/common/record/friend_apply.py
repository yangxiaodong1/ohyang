from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_log import OHHOLog
from ohho.common.db.record.db_ohho_record_friend_apply import DBOHHORecordFriendApply
from ohho.common.logic.common.record.constant import VALID_INTERVAL_MILLISECOND
from ohho.common.logic.ohho.detail_constant import *


class FriendApply(object):
    def __init__(self):
        self.apply = DBOHHORecordFriendApply()

    def get(self, one_user_id, another_user_id):
        """
        根据发起人和接收人获取最新的配对请求，
        并且这个请求只在30分钟内有效
        :param data_dict:
        :return:
        """
        if one_user_id and another_user_id:
            apply = self.apply
            query = apply.get_query()
            query = apply.get_by_one_user(query, one_user_id)
            query = apply.get_by_another_user(query, another_user_id)
            query = apply.order_by_id_desc(query)
            query = apply.first(query)
            if query:
                # 因为配对请求只能添加不能更改（没有地方会更改），
                # 所以这里的timestamp是添加时的timestamp
                if query.timestamp + VALID_INTERVAL_MILLISECOND > OHHODatetime.get_current_timestamp():
                    return query
                else:
                    OHHOLog.print_log(VALID_FRIEND_APPLY_NOT_EXIST)
            else:
                OHHOLog.print_log(FRIEND_APPLY_NOT_EXIST)
        else:
            OHHOLog.print_log(PARAMETERS_ARE_INVALID)
        return None

    def polling_get_by_one(self, user, small_timestamp, big_timestamp):
        apply = self.apply
        query = apply.get_query()
        query = apply.get_by_one_user(query, user.id)
        query = apply.get_by_timestamp_great_than_equal(query, small_timestamp)
        query = apply.get_by_timestamp_less_than(query, big_timestamp)
        query = apply.order_by_id_desc(query)
        return query

    def polling_get_by_another(self, user, small_timestamp, big_timestamp):
        apply = self.apply
        query = apply.get_query()
        query = apply.get_by_another_user(query, user.id)
        query = apply.get_by_timestamp_great_than_equal(query, small_timestamp)
        query = apply.get_by_timestamp_less_than(query, big_timestamp)
        query = apply.order_by_id_desc(query)
        return query

    def add(self, one_user_id, another_user_id, data_dict):
        """

        :param one_user_id:
        :param another_user_id:
        :param data_dict: match_condition_id
        :return:
        """
        apply = self.get(one_user_id, another_user_id)
        if not apply:
            data_dict["one_user_id"] = one_user_id
            data_dict["another_user_id"] = another_user_id
            apply = self.apply()
            success = apply.add(data_dict)
            if success:
                OHHOLog.print_log(ADD_FRIEND_APPLY_SUCCESS)
                return self.get(one_user_id, another_user_id)
            else:
                OHHOLog.print_log(ADD_FRIEND_APPLY_FAILED)
        else:
            OHHOLog.print_log(VALID_FRIEND_APPLY_EXIST)
        return None

    def get_information(self, apply_id):
        match_apply = self.apply
        apply = match_apply.get_by_id(apply_id)
        if apply:
            return match_apply.get_information(apply)
        else:
            return dict()


if __name__ == "__main__":
    FriendApply.add(1, 2, {"match_condition_id": 3})
