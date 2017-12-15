from DB.mysql.models.model_cellphone import *

from DB.mysql.models.ohho.base.model_ohho_interest import *
from DB.mysql.models.ohho.base.model_ohho_sensitive import *

from DB.mysql.models.ohho.cellphone.model_ohho_country_code import *
from DB.mysql.models.ohho.user.model_ohho_user import *
from DB.mysql.models.ohho.user.model_ohho_user_token import *
from DB.mysql.models.ohho.user.model_ohho_user_accuracy_extension import *
from DB.mysql.models.ohho.user.model_ohho_user_configuration import *

from DB.mysql.models.ohho.user.model_ohho_user_favourite_movie import *
from DB.mysql.models.ohho.user.model_ohho_user_favourite_sport import *
from DB.mysql.models.ohho.user.model_ohho_user_favourite_music import *
from DB.mysql.models.ohho.user.model_ohho_user_favourite_book import *
from DB.mysql.models.ohho.user.model_ohho_user_impression import *
from DB.mysql.models.ohho.user.model_ohho_user_icon import *
from DB.mysql.models.ohho.user.model_ohho_user_description import *

from DB.mysql.models.ohho.device.model_ohho_device import *
from DB.mysql.models.ohho.device.model_ohho_device_version import *
from DB.mysql.models.ohho.device.model_ohho_device_setting import *
from DB.mysql.models.ohho.device.model_ohho_device_sensor import *

from DB.mysql.models.ohho.relation.model_ohho_user_and_device_relation import *
from DB.mysql.models.ohho.relation.model_ohho_user_and_cellphone_relation import *

from DB.mysql.models.ohho.feedback.model_ohho_feedback import *
from DB.mysql.models.ohho.feedback.model_ohho_cancel_meet_feedback import *
from DB.mysql.models.ohho.feedback.model_ohho_complete_meet_feedback import *

from DB.mysql.models.ohho.report.model_ohho_report import *

from DB.mysql.models.ohho.map.model_ohho_map_information import *
from DB.mysql.models.ohho.relation.model_ohho_user_and_device_imei import *

from DB.mysql.models.ohho.im.ohho_im_user import *
from DB.mysql.models.ohho.im.ohho_im_user_relation import *

from DB.mysql.models.ohho.record.model_ohho_record_match_condition import *
from DB.mysql.models.ohho.record.model_ohho_record_match_apply import *
from DB.mysql.models.ohho.record.model_ohho_record_match_refuse import *
from DB.mysql.models.ohho.record.model_ohho_record_match_agree import *
from DB.mysql.models.ohho.record.model_ohho_record_match_meet import *
from DB.mysql.models.ohho.record.model_ohho_record_match_meeting import *
from DB.mysql.models.ohho.record.model_ohho_record_match_met import *
from DB.mysql.models.ohho.record.model_ohho_record_match_meet_end import *
from DB.mysql.models.ohho.record.model_ohho_record_match_duplex_agree import *
from DB.mysql.models.ohho.record.model_ohho_record_user_and_match_condition import *
from DB.mysql.models.ohho.record.model_ohho_record_friend_apply import *
from DB.mysql.models.ohho.record.model_ohho_record_friend_refuse import *
from DB.mysql.models.ohho.record.model_ohho_record_friend_agree import *
from DB.mysql.models.ohho.record.model_ohho_record_exclude import *

from DB.mysql.models.ohho.meet.model_ohho_topic import *

from DB.mysql.models.ohho.permission.page import *
from DB.mysql.models.ohho.permission.page_permission import *
from DB.mysql.models.ohho.permission.group import *
from DB.mysql.models.ohho.permission.group_and_user_relation import *
from DB.mysql.models.ohho.permission.group_and_page_relation import *

from DB.mysql.models.ohho.meet.model_ohho_temp_meet_address import *

from DB.mysql.models.district.model_china import China
from DB.mysql.models.school.model_school import School

# Test
from DB.mysql.models.model_test_device import *
from DB.mysql.models.model_test_timestamp import *

from DB.mysql.models.ohho.test.model_test_rssi import *
from DB.mysql.models.ohho.test.model_test_rssi_distance import *
from DB.mysql.models.ohho.test.model_test_interest_point import *
from DB.mysql.models.ohho.test.model_test_map_information import *
from DB.mysql.models.model_test_phone_position import *

# 废弃的表
# from DB.mysql.models.model_province import *
# from DB.mysql.models.model_city import *
# from DB.mysql.models.model_area import Area
# from DB.mysql.models.ohho.base.model_ohho_watchword import *
# from DB.mysql.models.ohho.user.model_ohho_user_display_configuration import *
# from DB.mysql.models.ohho.match.model_ohho_match_condition import *
# from DB.mysql.models.ohho.match.model_ohho_match_log import *
# from DB.mysql.models.ohho.im.ohho_im_user_request_relation import *
# from DB.mysql.models.ohho.record.model_ohho_record_match_label import *

from DB.mysql.base_model import init_db

init_db()
