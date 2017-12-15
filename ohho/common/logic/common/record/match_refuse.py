from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_log import OHHOLog
from ohho.common.db.record.db_ohho_record_match_refuse import DBOHHORecordMatchRefuse
from ohho.common.logic.common.record.constant import VALID_INTERVAL_MILLISECOND
from ohho.common.logic.ohho.detail_constant import ADD_MATCH_REFUSE_FAILED
from ohho.common.logic.ohho.detail_constant import ADD_MATCH_REFUSE_SUCCESS
from ohho.common.logic.ohho.detail_constant import MATCH_REFUSE_NOT_EXIST
from ohho.common.logic.ohho.detail_constant import PARAMETERS_ARE_INVALID
from ohho.common.logic.ohho.detail_constant import VALID_MATCH_REFUSE_EXIST
from ohho.common.logic.ohho.detail_constant import VALID_MATCH_REFUSE_NOT_EXIST


class MatchRefuse(object):
    def __init__(self):
        self.refuse = DBOHHORecordMatchRefuse()

    def get(self, apply_id):
        """
        根据请求ID获取最新的配对请求，
        并且这个请求只在30分钟内有效
        :param data_dict:
        :return:
        """
        if apply_id:
            query = self.refuse.filter_by_apply(apply_id)
            query = self.refuse.order_by_id_desc(query)
            query = self.refuse.first(query)
            if query:
                # 因为配对同意只能添加不能更改（没有地方会更改），
                # 所以这里的timestamp是添加时的timestamp
                # 拒绝无过期
                # if query.timestamp + VALID_INTERVAL_MILLISECOND > OHHODatetime.get_current_timestamp():
                return query
                # else:
                #     OHHOLog.print_log(VALID_MATCH_REFUSE_NOT_EXIST)
            else:
                OHHOLog.print_log(MATCH_REFUSE_NOT_EXIST)
        else:
            OHHOLog.print_log(PARAMETERS_ARE_INVALID)
        return None

    def get_by_apply(self, apply_id_list):
        result = list()
        if apply_id_list:
            query = self.refuse.find_by_apply(apply_id_list)
            query = self.refuse.order_by_id_desc(query)
            query = self.refuse.first(query)
            if not self.refuse.is_empty(query):
                for q in query:
                    if q.timestamp + VALID_INTERVAL_MILLISECOND > OHHODatetime.get_current_timestamp():
                        result.append(q)
        return result

    def add(self, apply_id, data_dict=dict()):
        """
        没有拒绝过，可以拒绝；
        :param apply_id:
        :param data_dict:
        :return:
        """
        refuse = self.get(apply_id)
        if not refuse:
            data_dict["apply_id"] = apply_id
            success = self.refuse.add(data_dict)
            if success:
                OHHOLog.print_log(ADD_MATCH_REFUSE_SUCCESS)
                return self.get(apply_id)
            else:
                OHHOLog.print_log(ADD_MATCH_REFUSE_FAILED)
        else:
            OHHOLog.print_log(VALID_MATCH_REFUSE_EXIST)
        return None
