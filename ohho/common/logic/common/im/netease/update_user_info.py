from ohho.common.logic.common.im.netease.constant import *
from ohho.common.logic.common.im.netease.header import Header
from ohho.common.db.im.db_ohho_im_user import DBOHHOIMUser
from Tools.ohho_http import OHHOHttp
from Tools.ohho_operation import OHHOOperation


class UpdateUserInfo(object):
    @staticmethod
    def update_user_info(accid, name=None, icon=None, sign=None, email=None, birth=None, mobile=None, gender=None,
                         ex=None):
        """
        :param accid: string, 必填， 用户帐号，最大长度32字符，必须保证一个APP内唯一
        :param name: string, 选填， 用户昵称，最大长度64字符
        :param icon: string, 选填， 用户icon，最大长度1024字符
        :param sign: string, 选填， 用户签名，最大长度256字符
        :param email: string, 选填， 用户email，最大长度64字符
        :param birth: string, 选填， 用户生日，最大长度16字符
        :param mobile: string, 选填， 用户mobile，最大长度32字符，只支持国内号码
        :param gender: int, 选填， 用户性别，0表示未知，1表示男，2女表示女，其它会报参数错误
        :param ex: string, 选填， 用户名片扩展字段，最大长度1024字符，用户可自行扩展，建议封装成JSON字符串
        :return:
        """
        url = URL_UPDATE_USER_INFO
        headers = Header.get_create_header()
        data = dict()
        data[PARAMETER_NAME_ACCID] = accid
        if name is not None:
            data[PARAMETER_NAME_NAME] = name
        if icon is not None:
            data[PARAMETER_NAME_ICON] = icon
        if sign is not None:
            data[PARAMETER_UPDATE_USER_SIGN] = sign
        if email is not None:
            data[PARAMETER_UPDATE_USER_SIGN] = email
        if birth is not None:
            data[PARAMETER_UPDATE_USER_BIRTH] = birth
        if mobile is not None:
            data[PARAMETER_UPDATE_USER_MOBILE] = mobile
        if gender is not None:
            data[PARAMETER_UPDATE_USER_GENDER] = gender
        if ex is not None:
            data[PARAMETER_UPDATE_USER_EX] = ex

        response = OHHOHttp.post(url, headers, data)
        return response
