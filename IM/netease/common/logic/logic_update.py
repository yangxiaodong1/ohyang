import json
from Tools.ohho_http import OHHOHttp
from Tools.ohho_operation import OHHOOperation
from IM.netease.common.logic.constant import URL_UPDATE
from IM.netease.common.logic.constant import PARAMETER_NAME_TOKEN
from IM.netease.common.logic.constant import PARAMETER_NAME_ACCID
from IM.netease.common.logic.constant import PARAMETER_NAME_PROPERTIES
from IM.netease.common.logic.logic_header import LogicHeader
from IM.netease.common.db.db_account import DBOHHOIMUser


class LogicUpdate(object):
    @staticmethod
    def update(account_id, properties="", token=""):
        url = URL_UPDATE
        headers = LogicHeader.get_create_header()
        data = dict()
        data[PARAMETER_NAME_ACCID] = account_id,
        data[PARAMETER_NAME_PROPERTIES] = properties if properties else ""
        data[PARAMETER_NAME_TOKEN] = token if token else ""
        response = OHHOHttp.post(url, headers, data)
        return response


if __name__ == "__main__":
    print(LogicUpdate.update("lileliang5", properties="test"))