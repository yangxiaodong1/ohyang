from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_log import OHHOLog
from ohho.common.db.record.db_ohho_record_friend_agree import DBOHHORecordFriendAgree
from ohho.common.logic.common.record.constant import VALID_INTERVAL_MILLISECOND
from ohho.common.logic.common.record.friend_refuse import FriendRefuse
from ohho.common.logic.ohho.detail_constant import ADD_FRIEND_AGREE_FAILED
from ohho.common.logic.ohho.detail_constant import ADD_FRIEND_AGREE_SUCCESS
from ohho.common.logic.ohho.detail_constant import FRIEND_AGREE_NOT_EXIST
from ohho.common.logic.ohho.detail_constant import PARAMETERS_ARE_INVALID
from ohho.common.logic.ohho.detail_constant import VALID_FRIEND_AGREE_EXIST
from ohho.common.logic.ohho.detail_constant import VALID_FRIEND_AGREE_NOT_EXIST
from ohho.common.logic.ohho.detail_constant import VALID_FRIEND_REFUSE_EXIST


class FriendAgree(object):
    def __init__(self):
        self.agree = DBOHHORecordFriendAgree()

    def get(self, apply_id):
        """
        根据请求ID获取最新的配对请求，
        并且这个请求只在30分钟内有效
        :param data_dict:
        :return:
        """
        if apply_id:
            agree = self.agree
            query = agree.filter_by_apply(apply_id)
            query = agree.order_by_id_desc(query)
            query = agree.first(query)
            if query:
                # 因为配对同意只能添加不能更改（没有地方会更改），
                # 所以这里的timestamp是添加时的timestamp
                if query.timestamp + VALID_INTERVAL_MILLISECOND > OHHODatetime.get_current_timestamp():
                    return query
                else:
                    OHHOLog.print_log(VALID_FRIEND_AGREE_NOT_EXIST)
            else:
                OHHOLog.print_log(FRIEND_AGREE_NOT_EXIST)
        else:
            OHHOLog.print_log(PARAMETERS_ARE_INVALID)
        return None

    def get_by_apply(self, apply_id_list):
        result = list()
        if apply_id_list:
            agree = self.agree
            query = agree.find_by_apply(apply_id_list)
            query = agree.order_by_id_desc(query)
            query = agree.first(query)

            if not agree.is_empty(query):
                for q in query:
                    if q.timestamp + VALID_INTERVAL_MILLISECOND > OHHODatetime.get_current_timestamp():
                        result.append(q)
        return result

    def add(self, apply_id, data_dict=dict()):
        """
        当没有同意并且没有拒绝过时，可以同意；
        同意或者拒绝过，不可以同意
        :param apply_id:
        :param data_dict:
        :return:
        """
        match_refuse = FriendRefuse()
        agree = self.get(apply_id)
        refuse = match_refuse.get(apply_id)
        if not agree:
            if not refuse:
                data_dict["apply_id"] = apply_id
                match_agree = self.agree()
                success = match_agree.add(data_dict)
                if success:
                    OHHOLog.print_log(ADD_FRIEND_AGREE_SUCCESS)
                    return self.get(apply_id)
                else:
                    OHHOLog.print_log(ADD_FRIEND_AGREE_FAILED)
            else:
                OHHOLog.print_log(VALID_FRIEND_REFUSE_EXIST)
        else:
            OHHOLog.print_log(VALID_FRIEND_AGREE_EXIST)

        return None
