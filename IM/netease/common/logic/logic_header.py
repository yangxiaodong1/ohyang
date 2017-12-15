from IM.netease.common.logic.constant import APP_SECRET, APP_KEY
from IM.netease.common.logic.constant import CONTENT_TYPE_CREATE
from IM.netease.common.logic.constant import HEADER_NAME_APP_KEY
from IM.netease.common.logic.constant import HEADER_NAME_CHECK_SUM
from IM.netease.common.logic.constant import HEADER_NAME_CURRENT_TIME
from IM.netease.common.logic.constant import HEADER_NAME_NONCE
from IM.netease.common.logic.constant import HEADER_NAME_CONTENT_TYPE
from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_encryption import OHHOEncryption
from Tools.ohho_random import OHHORandom


class LogicHeader(object):
    @staticmethod
    def get_check_sum(app_secret, nonce, current_time):
        check_sum_string = app_secret + nonce + current_time
        check_sum_string_utf8 = check_sum_string.encode("utf8")
        return OHHOEncryption.sha1(check_sum_string_utf8)

    @staticmethod
    def get_header():
        header = dict()
        nonce = OHHORandom.get_nonce()
        current_time = str(OHHODatetime.get_current_timestamp())
        app_secret = APP_SECRET
        app_key = APP_KEY
        check_sum = LogicHeader.get_check_sum(app_secret, nonce, current_time)
        header[HEADER_NAME_NONCE] = nonce
        header[HEADER_NAME_CURRENT_TIME] = current_time
        header[HEADER_NAME_APP_KEY] = app_key
        header[HEADER_NAME_NONCE] = nonce
        header[HEADER_NAME_CHECK_SUM] = check_sum
        return header

    @staticmethod
    def get_create_header():
        header = LogicHeader.get_header()
        header[HEADER_NAME_CONTENT_TYPE] = CONTENT_TYPE_CREATE
        return header


if __name__ == "__main__":
    print(LogicHeader.get_create_header())
