import json
from Tools.ohho_http import OHHOHttp
from Tools.ohho_operation import OHHOOperation
from IM.netease.common.logic.constant import URL_REFRESH_TOKEN
from IM.netease.common.logic.constant import RESPONSE_NAME_CODE
from IM.netease.common.logic.constant import RESPONSE_NAME_INFO
from IM.netease.common.logic.constant import RESPONSE_NAME_INFO_ACCID
from IM.netease.common.logic.constant import RESPONSE_NAME_INFO_TOKEN
from IM.netease.common.logic.constant import RESPONSE_CODE_SUCCESS
from IM.netease.common.logic.constant import PARAMETER_NAME_ACCID
from IM.netease.common.logic.constant import PARAMETER_NAME_PROPERTIES
from IM.netease.common.logic.logic_header import LogicHeader
from IM.netease.common.db.db_account import DBOHHOIMUser


class LogicRefreshToken(object):
    @staticmethod
    def refresh_token(account_id):
        url = URL_REFRESH_TOKEN
        headers = LogicHeader.get_create_header()
        data = dict()
        data[PARAMETER_NAME_ACCID] = account_id
        response = OHHOHttp.post(url, headers, data)
        return response

    @staticmethod
    def update2db(response):
        response_dict = OHHOOperation.json2dict(response)
        code = response_dict[RESPONSE_NAME_CODE]
        if code == RESPONSE_CODE_SUCCESS:
            info = response_dict[RESPONSE_NAME_INFO]
            accid = info[RESPONSE_NAME_INFO_ACCID]
            obj = DBOHHOIMUser.get_by_account_id(accid)
            if obj:
                data = dict()
                data["token"] = info[RESPONSE_NAME_INFO_TOKEN]
                success = DBOHHOIMUser.update(obj, data)
                return success
        return False


if __name__ == "__main__":
    # response = LogicRefreshToken.refresh_token("lileliang5")
    response = LogicRefreshToken.refresh_token("lileliang8")
    print(response)
    # LogicRefreshToken.update2db(response)
