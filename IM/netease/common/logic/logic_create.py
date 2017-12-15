import json
from Tools.ohho_http import OHHOHttp
from Tools.ohho_operation import OHHOOperation
from IM.netease.common.logic.constant import URL_CREATE
from IM.netease.common.logic.logic_header import LogicHeader
from IM.netease.common.logic.constant import PARAMETER_NAME_ACCID
from IM.netease.common.logic.constant import PARAMETER_NAME_ICON
from IM.netease.common.logic.constant import PARAMETER_NAME_NAME
from IM.netease.common.logic.constant import PARAMETER_NAME_PROPERTIES
from IM.netease.common.logic.constant import PARAMETER_NAME_TOKEN
from IM.netease.common.logic.constant import RESPONSE_NAME_CODE
from IM.netease.common.logic.constant import RESPONSE_NAME_INFO
from IM.netease.common.logic.constant import RESPONSE_NAME_INFO_ACCID
from IM.netease.common.logic.constant import RESPONSE_NAME_INFO_NAME
from IM.netease.common.logic.constant import RESPONSE_NAME_INFO_TOKEN

from IM.netease.common.db.db_account import DBOHHOIMUser


class LogicCreate(object):
    @staticmethod
    def create(account_id, name="", properties="", icon="", token=""):
        url = URL_CREATE
        headers = LogicHeader.get_create_header()
        data = dict()
        data[PARAMETER_NAME_ACCID] = account_id,
        data[PARAMETER_NAME_NAME] = name if name else ""
        data[PARAMETER_NAME_PROPERTIES] = properties if properties else ""
        data[PARAMETER_NAME_ICON] = icon if icon else ""
        data[PARAMETER_NAME_TOKEN] = token if token else ""
        response = OHHOHttp.post(url, headers, data)
        return response

    @staticmethod
    def add2db(response, properties="", icon=""):
        response_dict = OHHOOperation.json2dict(response)
        if response_dict[RESPONSE_NAME_CODE] == 200:
            info = response_dict[RESPONSE_NAME_INFO]
            token = info[RESPONSE_NAME_INFO_TOKEN]
            account_id = info[RESPONSE_NAME_INFO_ACCID]
            name = info[RESPONSE_NAME_INFO_NAME]
            data_dict = dict()
            data_dict["account_id"] = account_id
            data_dict["token"] = token
            data_dict["name"] = name
            data_dict["properties"] = properties
            data_dict["icon"] = icon
            return DBOHHOIMUser.add(data_dict)
        else:
            return DBOHHOIMUser.get_none()


if __name__ == "__main__":
    data = LogicCreate.create("lileliang5")
    data_dict = json.loads(data)
    print(data_dict)
    print(data_dict["code"])
    # LogicCreate.add2db(data)
