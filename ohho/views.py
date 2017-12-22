from ohho.common.view.ohho.basic.view_add_body_type import *
from ohho.common.view.ohho.basic.view_add_device import *
from ohho.common.view.ohho.basic.view_add_drink import *
from ohho.common.view.ohho.basic.view_add_industry import *
from ohho.common.view.ohho.basic.view_add_profession import *
from ohho.common.view.ohho.basic.view_add_smoke import *
from ohho.common.view.ohho.basic.view_add_work_domain import *

from ohho.common.view.ohho.code.view_send_verification_code import *
from ohho.common.view.ohho.code.view_check_verification_code import *

from ohho.common.view.ohho.device.view_add_device_setting import *
from ohho.common.view.ohho.device.view_add_device_version import *
from ohho.common.view.ohho.device.view_bind_device import *
from ohho.common.view.ohho.device.view_bluetooth_position import *
from ohho.common.view.ohho.device.view_cancel_lost import *
from ohho.common.view.ohho.device.view_cellphone_unbind_device import *
from ohho.common.view.ohho.device.view_find_device_position import *
from ohho.common.view.ohho.device.view_get_bound_devices import *
from ohho.common.view.ohho.device.view_get_device_setting import *
from ohho.common.view.ohho.device.view_get_device_version import *
from ohho.common.view.ohho.device.view_get_user_and_device_imei import *
from ohho.common.view.ohho.device.view_is_device_valid import *
from ohho.common.view.ohho.device.view_set_device_use import *
from ohho.common.view.ohho.device.view_set_lost import *
from ohho.common.view.ohho.device.view_unbind_device import *
from ohho.common.view.ohho.device.view_update_device_setting import *

from ohho.common.view.ohho.friend.view_add_black import *
from ohho.common.view.ohho.friend.view_agree_friend import *
from ohho.common.view.ohho.friend.view_apply_friend import *
from ohho.common.view.ohho.friend.view_remove_friend import *
from ohho.common.view.ohho.friend.view_list_apply_friend import *
from ohho.common.view.ohho.friend.view_list_blacks import *
from ohho.common.view.ohho.friend.view_list_friends import *
from ohho.common.view.ohho.friend.view_refuse_friend import *
from ohho.common.view.ohho.friend.view_remove_black import *
from ohho.common.view.ohho.friend.view_open_online_switch import *
from ohho.common.view.ohho.friend.view_close_online_switch import *
from ohho.common.view.ohho.friend.view_set_online_switch import *

from ohho.common.view.ohho.map.view_get_friend_map_position import *
from ohho.common.view.ohho.map.view_get_map_positions import *
from ohho.common.view.ohho.map.view_map_distance import *
from ohho.common.view.ohho.map.view_upload_map_position import *

from ohho.common.view.ohho.match.view_add_match_condition import *
from ohho.common.view.ohho.match.view_add_record_exclude import *
from ohho.common.view.ohho.match.view_get_match_condition import *
from ohho.common.view.ohho.match.view_match import *
from ohho.common.view.ohho.match.view_match3 import *
from ohho.common.view.ohho.match.version2.view_match import *
from ohho.common.view.ohho.match.version2.view_match2 import *
from ohho.common.view.ohho.match.view_polling_get_match_apply import *
from ohho.common.view.ohho.match.view_polling_get_match_state import *
from ohho.common.view.ohho.match.view_open_match_switch import *
from ohho.common.view.ohho.match.view_close_match_switch import *
from ohho.common.view.ohho.match.view_set_match_switch import *

from ohho.common.view.ohho.meet.view_add_meet import *
from ohho.common.view.ohho.meet.view_agree_meet import *
from ohho.common.view.ohho.meet.view_apply_meet import *
from ohho.common.view.ohho.meet.view_cancel_meet import *
from ohho.common.view.ohho.meet.view_meet import *
from ohho.common.view.ohho.meet.view_meet_send_message import *
from ohho.common.view.ohho.meet.view_meet_state import *
from ohho.common.view.ohho.meet.view_refuse_meet import *
from ohho.common.view.ohho.meet.view_meet_end import *
from ohho.common.view.ohho.meet.view_met_by_device import *
from ohho.common.view.ohho.meet.view_met_by_hand import *
from ohho.common.view.ohho.meet.view_not_met_by_hand import *
from ohho.common.view.ohho.meet.view_rematch import *

from ohho.common.view.ohho.feedback.view_add_feedback import *
from ohho.common.view.ohho.feedback.view_get_feedback_type import *
from ohho.common.view.ohho.feedback.view_get_cancel_meet_feedback_type import *
from ohho.common.view.ohho.feedback.view_get_complete_meet_feedback_type import *
from ohho.common.view.ohho.feedback.view_add_cancel_meet_feedback import *
from ohho.common.view.ohho.feedback.view_add_complete_meet_feedback import *

from ohho.common.view.ohho.report.view_add_report import *
from ohho.common.view.ohho.report.view_get_report_type import *

from ohho.common.view.ohho.other.view_rebind_cellphone import *
from ohho.common.view.ohho.other.view_update_user_and_cellphone_relation import *
from ohho.common.view.ohho.other.view_get_basic_data import *

from ohho.common.view.ohho.register.view_login import *
from ohho.common.view.ohho.register.view_login_by_code import *
from ohho.common.view.ohho.register.view_logout import *
from ohho.common.view.ohho.register.view_register import *
from ohho.common.view.ohho.register.view_unregister import *

from ohho.common.view.ohho.user.view_add_user_accuracy_extension import *
from ohho.common.view.ohho.user.view_add_user_icon import *
from ohho.common.view.ohho.user.view_add_user_exclude import *
from ohho.common.view.ohho.user.view_add_one_user_exclude import *
from ohho.common.view.ohho.user.view_delete_one_user_exclude import *
from ohho.common.view.ohho.user.view_get_user_information import *
from ohho.common.view.ohho.user.view_reset_password import *
from ohho.common.view.ohho.user.view_update_cellphone_number import *
# 添加个人信息
from ohho.common.view.ohho.user.view_exist_cellphone import *
from ohho.common.view.ohho.user.view_complete_user import *
from ohho.common.view.ohho.user.view_add_user_basic import *
from ohho.common.view.ohho.user.view_add_user_favourite_book import *
from ohho.common.view.ohho.user.view_add_user_favourite_movie import *
from ohho.common.view.ohho.user.view_add_user_favourite_music import *
from ohho.common.view.ohho.user.view_add_user_favourite_sport import *

# 获取个人信息
from ohho.common.view.ohho.user.view_get_user_personal_information import *
from ohho.common.view.ohho.user.view_get_user_personal_page import *

from ohho.common.view.ohho.meet.view_meet_topic import *
from ohho.common.view.ohho.meet.view_where_meet import *

# from ohho.common.view.test.view_test_update_device_information import *
# from ohho.common.view.test.view_test_get_user_by_device import *
# from ohho.common.view.test.view_test_delete_apply import *
# from ohho.common.view.test.view_test_delete_test import *
# from ohho.common.view.test.view_test_test import *
# from ohho.common.view.test.view_test_distance import *
