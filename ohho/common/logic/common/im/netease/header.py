from ohho.common.logic.common.im.netease.constant import *
from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_encryption import OHHOEncryption
from Tools.ohho_random import OHHORandom
from Tools.ohho_log import OHHOLog


class Header(object):
    @staticmethod
    def get_check_sum(app_secret, nonce, current_time):
        check_sum_string = app_secret + nonce + current_time
        # check_sum_string_utf8 = check_sum_string.encode("utf8")
        return OHHOEncryption.sha1(check_sum_string)

    @staticmethod
    def get_header():
        header = dict()
        nonce = OHHORandom.get_nonce()
        current_time = str(OHHODatetime.get_current_timestamp_second())
        app_secret = APP_SECRET
        app_key = APP_KEY
        check_sum = Header.get_check_sum(app_secret, nonce, current_time)
        header[HEADER_NAME_NONCE] = nonce
        header[HEADER_NAME_CURRENT_TIME] = current_time
        header[HEADER_NAME_APP_KEY] = app_key
        header[HEADER_NAME_CHECK_SUM] = check_sum
        return header

    @staticmethod
    def get_create_header():
        header = Header.get_header()
        header[HEADER_NAME_CONTENT_TYPE] = CONTENT_TYPE_CREATE
        # print(header)
        return header


if __name__ == "__main__":
    print(Header.get_create_header())
