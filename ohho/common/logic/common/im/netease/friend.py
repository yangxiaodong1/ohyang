from ohho.common.logic.common.im.netease.constant import *
from ohho.common.logic.common.im.netease.header import Header
from ohho.common.db.im.db_ohho_im_user import DBOHHOIMUser
from Tools.ohho_http import OHHOHttp
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog


class Friend(object):
    @staticmethod
    def add_friend(account_id, friend_account_id, type, message):
        url = URL_USER_RELATION_ADD_FRIEND
        headers = Header.get_create_header()
        data = dict()
        data[PARAMETER_NAME_ACCID] = account_id
        data[PARAMETER_NAME_FRIEND_ACCID] = friend_account_id
        data[PARAMETER_NAME_ADD_FRIEND_TYPE] = type
        data[PARAMETER_NAME_ADD_FRIEND_MESSAGE] = message
        response = OHHOHttp.post(url, headers, data)
        return response

    @staticmethod
    def apply_friend(account_id, friend_account_id, message):
        return Friend.add_friend(account_id, friend_account_id, APPLY_FRIEND, message)

    @staticmethod
    def agree_friend(account_id, friend_account_id, message):
        return Friend.add_friend(account_id, friend_account_id, AGREE_FRIEND, message)

    @staticmethod
    def refuse_friend(account_id, friend_account_id, message):
        return Friend.add_friend(account_id, friend_account_id, REFUSE_FRIEND, message)

    @staticmethod
    def update_friend(account_id, friend_account_id, alias=None, ex=None):
        url = URL_USER_RELATION_REMOVE_FRIEND
        headers = Header.get_create_header()
        data = dict()
        data[PARAMETER_NAME_ACCID] = account_id
        data[PARAMETER_NAME_FRIEND_ACCID] = friend_account_id
        if alias is not None:
            data[PARAMETER_NAME_UPDATE_FRIEND_ALIAS] = alias
        if ex is not None:
            data[PARAMETER_NAME_UPDATE_FRIEND_EXTRA] = ex
        response = OHHOHttp.post(url, headers, data)
        return response

    @staticmethod
    def remove_friend(account_id, friend_account_id):
        url = URL_USER_RELATION_REMOVE_FRIEND
        headers = Header.get_create_header()
        data = dict()
        data[PARAMETER_NAME_ACCID] = account_id
        data[PARAMETER_NAME_FRIEND_ACCID] = friend_account_id
        response = OHHOHttp.post(url, headers, data)
        return response
