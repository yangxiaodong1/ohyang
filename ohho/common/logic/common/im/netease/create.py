import json
from Tools.ohho_http import OHHOHttp
from Tools.ohho_operation import OHHOOperation
from ohho.common.logic.common.im.netease.constant import *
from ohho.common.logic.common.im.netease.header import Header

from ohho.common.db.im.db_ohho_im_user import DBOHHOIMUser


class Create(object):
    @staticmethod
    def create(account_id, name=None, properties=None, icon=None, token=None):
        url = URL_CREATE
        headers = Header.get_create_header()
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
        instance = DBOHHOIMUser()
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
            data_dict["props"] = properties
            data_dict["icon"] = icon
            return instance.add(data_dict)
        else:
            return instance.get_none()

    @staticmethod
    def add(user_id, name="xiaobai", properties=None, icon=None, token=None):
        response = Create.create(user_id, name, properties, icon, token)
        success = Create.add2db(response, properties, icon)
        if success:
            return True
        else:
            return False


if __name__ == "__main__":
    data = Create.create("lileliang5")
    data_dict = json.loads(data)
    print(data_dict)
    print(data_dict["code"])
    Create.add2db(data)
