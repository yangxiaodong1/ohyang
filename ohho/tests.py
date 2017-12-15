from ohho.common.view.test.view_stressTesting_add_user import StressTestingAddUserHandler
from ohho.common.test.stressTesting.TestAddUser import StressTestAddUserHandler

# user
from ohho.common.test.user.test_complete_user import TestCompleteUserHandler
from ohho.common.test.user.test_add_user_accuracy_extension import TestAddUserAccuracyExtensionHandler
from ohho.common.test.user.test_update_cellphone_number import TestUpdateCellphoneNumberHandler
from ohho.common.test.user.test_add_user_icon import TestAddUserIconHandler
from ohho.common.test.user.test_add_user_exclude import TestAddUserExcludeHandler
from ohho.common.test.user.test_rebind_cellphone import TestRebindCellphoneHandler
from ohho.common.test.user.test_get_user_by_device import TestGetUserByDeviceHandler
from ohho.common.test.user.test_get_user_information import TestGetUserInformationHandler
from ohho.common.test.user.test_get_user_personal_information import TestGetUserPersonalInformationHandler
from ohho.common.test.user.test_get_user_personal_page import TestGetUserPersonalPageHandler

# match
from ohho.common.test.match.test_open_match_switch import TestOpenMatchSwitchHandler
from ohho.common.test.match.test_close_match_switch import TestCloseMatchSwitchHandler
from ohho.common.test.match.test_set_match_switch import TestSetMatchSwitchHandler
from ohho.common.test.match.test_add_exclude import TestAddExcludeHandler
from ohho.common.test.match.test_add_match_condition import TestAddMatchConditionHandler
from ohho.common.test.match.test_get_match_condition import TestGetMatchConditionHandler
from ohho.common.test.match.test_match import TestMatchHandler
from ohho.common.test.match.test_version2_match import TestVersion2MatchHandler
from ohho.common.test.match.test_polling_get_apply_state import TestPollingGetApplyStateHandler
from ohho.common.test.match.test_polling_get_apply_apply import TestPollingGetApplyApplyHandler

# device
from ohho.common.test.device.test_is_device_valid import TestIsDeviceValidHandler
from ohho.common.test.device.test_bind_device import TestBindDeviceHandler
from ohho.common.test.device.test_unbind_device import TestUnbindDeviceHandler
from ohho.common.test.device.test_cellphone_unbind_device import TestCellphoneUnbindDeviceHandler
from ohho.common.test.device.test_add_device import TestAddDeviceHandler
from ohho.common.test.device.test_bluetooth_position import TestBluetoothPositionHandler
from ohho.common.test.device.test_add_device_setting import TestAddDeviceSettingHandler
from ohho.common.test.device.test_update_device_setting import TestUpdateDeviceSettingHandler
from ohho.common.test.device.test_get_device_setting import TestGetDeviceSettingHandler
from ohho.common.test.device.test_find_device_position import TestFindDevicePositionHandler
from ohho.common.test.device.test_get_user_and_device_imei import TestGetUserAndDeviceIMEIHandler
from ohho.common.test.device.test_get_device_version import TestGetDeviceVersionHandler
from ohho.common.test.device.test_set_lost import TestSetLostHandler
from ohho.common.test.device.test_cancel_lost import TestCancelLostHandler
from ohho.common.test.device.test_set_device_use import TestSetDeviceUseHandler
from ohho.common.test.device.test_get_bound_device import TestGetBoundDeviceHandler

# home
from ohho.common.test.home.test_home import TestHomeHandler
from ohho.common.test.home.test_home_app import TestHomeAppHandler
from ohho.common.test.home.test_home_backstage import TestHomeBackstageHandler
from ohho.common.test.home.test_home_test import TestHomeTestHandler
from ohho.common.test.home.test_home_app_interfaces import TestHomeAppInterfacesHandler
from ohho.common.test.home.test_interfaces import TestInterfacesHandler
from ohho.common.test.home.test_home_app_quick_find import TestHomeAppQuickFindHandler

# register
from ohho.common.test.register.test_login import TestLoginHandler
from ohho.common.test.register.test_login_by_code import TestLoginByCodeHandler
from ohho.common.test.register.test_reset_password import TestResetPasswordHandler
from ohho.common.test.register.test_logout import TestLogoutHandler
from ohho.common.test.register.test_register import TestRegisterHandler

# code
from ohho.common.test.code.test_send_verification_code import TestSendVerificationCodeHandler
from ohho.common.test.code.test_check_verification_code import TestCheckVerificationCodeHandler

# friend
from ohho.common.test.friend.test_apply_friend import TestApplyFriendHandler
from ohho.common.test.friend.test_agree_friend import TestAgreeFriendHandler
from ohho.common.test.friend.test_remove_friend import TestRemoveFriendHandler
from ohho.common.test.friend.test_refuse_friend import TestRefuseFriendHandler
from ohho.common.test.friend.test_list_apply_friend import TestListApplyFriendHandler
from ohho.common.test.friend.test_open_online_switch import TestOpenOnlineSwitchHandler
from ohho.common.test.friend.test_close_online_switch import TestCloseOnlineSwitchHandler
from ohho.common.test.friend.test_set_online_switch import TestSetOnlineSwitchHandler
from ohho.common.test.friend.test_list_friends import TestListFriendsHandler
from ohho.common.test.friend.test_list_blacks import TestListBlacksHandler
from ohho.common.test.friend.test_add_black import TestAddBlackHandler
from ohho.common.test.friend.test_remove_black import TestRemoveBlackHandler

# meet
from ohho.common.test.meet.test_apply_meet import TestApplyMeetHandler
from ohho.common.test.meet.test_agree_meet import TestAgreeMeetHandler
from ohho.common.test.meet.test_refuse_meet import TestRefuseMeetHandler
from ohho.common.test.meet.test_cancel_meet import TestCancelMeetHandler
from ohho.common.test.meet.test_add_meet import TestAddMeetHandler
from ohho.common.test.meet.test_meet import TestMeetHandler
from ohho.common.test.meet.test_get_meet_state import TestGetMeetStateHandler
from ohho.common.test.meet.test_get_meet_topic import TestGetMeetTopicHandler
from ohho.common.test.meet.test_meet_by_device import TestMeetByDeviceHandler
from ohho.common.test.meet.test_meet_end import TestMeetEndHandler
from ohho.common.test.meet.test_meet_by_hand import TestMeetByHandHandler

# map
from ohho.common.test.map.test_upload_map_position import TestUploadMapPositionHandler
from ohho.common.test.map.test_get_friend_map_position import TestGetFriendMapPositionHandler
from ohho.common.test.map.test_get_map_positions import TestGetMapPositionsHandler

# report
from ohho.common.test.report.test_add_report import TestAddReportHandler

# feedback
from ohho.common.test.feedback.test_add_feedback import TestAddFeedbackHandler
from ohho.common.test.feedback.test_add_cancel_meet_feedback import TestAddCancelMeetFeedbackHandler
from ohho.common.test.feedback.test_add_complete_meet_feedback import TestAddCompleteMeetFeedbackHandler

# base
from ohho.common.test.base.test_add_drink import TestAddDrinkHandler
from ohho.common.test.base.test_add_smoke import TestAddSmokeHandler
from ohho.common.test.base.test_add_profession import TestAddProfessionHandler
from ohho.common.test.base.test_add_industry import TestAddIndustryHandler
from ohho.common.test.base.test_add_work_domain import TestAddWorkDomainHandler
from ohho.common.test.base.test_add_body_type import TestAddBodyTypeHandler
from ohho.common.test.base.test_get_basic_data import TestGetBasicDataHandler

# redis
from ohho.common.test.redis.test_get_redis_hash import TestGetRedisHashHandler
from ohho.common.test.redis.test_set_redis_hash import TestSetRedisHashHandler

# test
from ohho.common.test.test.test_add_timestamp import TestAddTimestampHandler

from ohho.common.view.test.view_test_update_device_information import *
from ohho.common.view.test.view_test_get_user_by_device import *
from ohho.common.view.test.view_test_delete_apply import *
from ohho.common.view.test.view_test_delete_test import *
# from ohho.common.view.test.view_test_test import *
from ohho.common.view.test.view_test_distance import *
from ohho.common.view.test.view_test_phone_position import *

# test rssi
from ohho.common.view.test.view_test_add_rssi import *
from ohho.common.view.test.view_test_compute_rssi import *
from ohho.common.view.test.view_test_add_interest_point import *

# test map
from ohho.common.view.test.view_test_add_map_information import *

# test user push information
from ohho.common.view.test.view_show_user_basic_information import *