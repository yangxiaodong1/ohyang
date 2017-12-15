import sys
from Tools.ohho_datetime import OHHODatetime
import logging

logger = logging.getLogger()


class OHHOLog(object):
    @staticmethod
    def get_current_file_name(information=None):
        OHHOLog.print_log(information)

    @staticmethod
    def print_log(information=None):
        try:
            raise Exception
        except:
            f = sys.exc_info()[2].tb_frame.f_back
        now = OHHODatetime.get_now()
        now_string = OHHODatetime.clock2string(now)
        file_name = f.f_code.co_filename
        name = f.f_code.co_name
        line_no = f.f_lineno
        content = now_string + "\t" + file_name + "\t" + name + "\t" + str(line_no) + "\t" + str(information)
        logger.info(content)


if __name__ == "__main__":
    OHHOLog.get_current_file_name('abc')
    OHHOLog.get_current_file_name('def')
    OHHOLog.get_current_file_name('ghi')
