from ohho.common.logic.common.im.netease.constant import *
from ohho.common.logic.common.im.netease.header import Header
from ohho.common.db.im.db_ohho_im_user import DBOHHOIMUser
from Tools.ohho_http import OHHOHttp
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog


class RefreshToken(object):
    @staticmethod
    def refresh_token(account_id):
        url = URL_REFRESH_TOKEN
        headers = Header.get_create_header()
        data = dict()
        data[PARAMETER_NAME_ACCID] = account_id
        response = OHHOHttp.post(url, headers, data)
        return response

    @staticmethod
    def update2db(response):
        instance = DBOHHOIMUser()
        response_dict = OHHOOperation.json2dict(response)
        code = response_dict[RESPONSE_NAME_CODE]
        if code == RESPONSE_CODE_SUCCESS:
            info = response_dict[RESPONSE_NAME_INFO]
            accid = info[RESPONSE_NAME_INFO_ACCID]
            query = instance.get_query()
            obj = instance.get_by_account(query, accid)
            obj = instance.first(obj)
            if obj:
                data = dict()
                data["token"] = info[RESPONSE_NAME_INFO_TOKEN]
                success = instance.update(obj, data)
                return success
            else:
                data = dict()
                data["token"] = info[RESPONSE_NAME_INFO_TOKEN]
                data["account_id"] = info[RESPONSE_NAME_INFO_ACCID]
                success = instance.add(data)
                return success
        return False

    @staticmethod
    def create_or_update(account_id):
        response = RefreshToken.refresh_token(account_id)
        OHHOLog.print_log(response)
        return RefreshToken.update2db(response)

if __name__ == "__main__":
    print(RefreshToken.refresh_token(10))
