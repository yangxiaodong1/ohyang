from ohho.tests import *

handlers = [
    (r"/rest/api/ohho/test/test/", TestTestHandler),
    (r"/rest/api/ohho/test/meet/", TestMeetHandler),
    (r"/rest/api/ohho/test/meet/rematch/", TestRematchHandler),
    (r"/rest/api/ohho/test/send/meet/message/", TestMeetSendMessageHandler),
    (r"/rest/api/ohho/test/apply/meet/", TestApplyMeetHandler),
    (r"/rest/api/ohho/test/agree/meet/", TestAgreeMeetHandler),
    (r"/rest/api/ohho/test/refuse/meet/", TestRefuseMeetHandler),
    (r"/rest/api/ohho/test/cancel/meet/", TestCancelMeetHandler),
    (r"/rest/api/ohho/test/add/meet/", TestAddMeetHandler),
    (r"/rest/api/ohho/test/add/exclude/", TestAddExcludeHandler),
    (r"/rest/api/ohho/test/get/user/and/device/imei/", TestGetUserAndDeviceIMEIHandler),

    (r"/rest/api/ohho/test/apply/friend/", TestApplyFriendHandler),
    (r"/rest/api/ohho/test/agree/friend/", TestAgreeFriendHandler),
    (r"/rest/api/ohho/test/remove/friend/", TestRemoveFriendHandler),
    (r"/rest/api/ohho/test/refuse/friend/", TestRefuseFriendHandler),
    (r"/rest/api/ohho/test/list/apply/friend/", TestListApplyFriendHandler),

    (r"/rest/api/ohho/test/im/list/friends/", TestListFriendsHandler),
    (r"/rest/api/ohho/test/im/list/blacks/", TestListBlacksHandler),
    (r"/rest/api/ohho/test/im/add/black/", TestAddBlackHandler),
    (r"/rest/api/ohho/test/im/remove/black/", TestRemoveBlackHandler),

    (r"/rest/api/ohho/test/bluetooth/position/", TestBluetoothPositionHandler),

    (r"/rest/api/ohho/test/add/device/setting/", TestAddDeviceSettingHandler),
    (r"/rest/api/ohho/test/update/device/setting/", TestUpdateDeviceSettingHandler),
    (r"/rest/api/ohho/test/get/device/setting/", TestGetDeviceSettingHandler),

    (r"/rest/api/ohho/test/complete/user/", TestCompleteUserHandler),
    (r"/rest/api/ohho/test/add/user/accuracy/extension/", TestAddUserAccuracyExtensionHandler),
    (r"/rest/api/ohho/test/update/cellphone/number/", TestUpdateCellphoneNumberHandler),
    (r"/rest/api/ohho/test/add/user/icon/", TestAddUserIconHandler),
    (r"/rest/api/ohho/test/add/user/exclude/", TestAddUserExcludeHandler),
    (r"/rest/api/ohho/test/rebind/cellphone/", TestRebindCellphoneHandler),
    (r"/rest/api/ohho/test/add/device/", TestAddDeviceHandler),
    (r"/rest/api/ohho/test/is/device/valid/", TestIsDeviceValidHandler),
    (r"/rest/api/ohho/test/open/match/switch/", TestOpenMatchSwitchHandler),
    (r"/rest/api/ohho/test/close/match/switch/", TestCloseMatchSwitchHandler),
    (r"/rest/api/ohho/test/set/match/switch/", TestSetMatchSwitchHandler),
    (r"/rest/api/ohho/test/open/online/switch/", TestOpenOnlineSwitchHandler),
    (r"/rest/api/ohho/test/close/online/switch/", TestCloseOnlineSwitchHandler),
    (r"/rest/api/ohho/test/set/online/switch/", TestSetOnlineSwitchHandler),
    (r"/rest/api/ohho/test/bind/device/", TestBindDeviceHandler),
    (r"/rest/api/ohho/test/unbind/device/", TestUnbindDeviceHandler),
    (r"/rest/api/ohho/test/cellphone/unbind/device/", TestCellphoneUnbindDeviceHandler),
    (r"/rest/api/ohho/test/home/", TestHomeHandler),
    (r"/rest/api/ohho/test/home/app/", TestHomeAppHandler),
    (r"/rest/api/ohho/test/home/app/quick/find/", TestHomeAppQuickFindHandler),
    (r"/rest/api/ohho/test/home/backstage/", TestHomeBackstageHandler),
    (r"/rest/api/ohho/test/home/test/", TestHomeTestHandler),
    (r"/rest/api/ohho/test/app/interfaces/home/", TestHomeAppInterfacesHandler),
    (r"/rest/api/ohho/test/interfaces/", TestInterfacesHandler),
    (r"/rest/api/ohho/test/login/", TestLoginHandler),
    (r"/rest/api/ohho/test/login/by/code/", TestLoginByCodeHandler),
    (r"/rest/api/ohho/test/logout/", TestLogoutHandler),
    (r"/rest/api/ohho/test/register/", TestRegisterHandler),
    (r"/rest/api/ohho/test/reset/password/", TestResetPasswordHandler),
    (r"/rest/api/ohho/test/send/verification/code/", TestSendVerificationCodeHandler),
    (r"/rest/api/ohho/test/check/verification/code/", TestCheckVerificationCodeHandler),

    (r"/rest/api/ohho/test/upload/map/position/", TestUploadMapPositionHandler),
    (r"/rest/api/ohho/test/get/friend/map/position/", TestGetFriendMapPositionHandler),
    (r"/rest/api/ohho/test/find/device/position/", TestFindDevicePositionHandler),

    (r"/rest/api/ohho/test/add/report/", TestAddReportHandler),
    (r"/rest/api/ohho/test/add/feedback/", TestAddFeedbackHandler),
    (r"/rest/api/ohho/test/add/cancel/meet/feedback/", TestAddCancelMeetFeedbackHandler),
    (r"/rest/api/ohho/test/add/complete/meet/feedback/", TestAddCompleteMeetFeedbackHandler),

    (r"/rest/api/ohho/test/add/drink/", TestAddDrinkHandler),
    (r"/rest/api/ohho/test/add/smoke/", TestAddSmokeHandler),
    (r"/rest/api/ohho/test/add/profession/", TestAddProfessionHandler),
    (r"/rest/api/ohho/test/add/industry/", TestAddIndustryHandler),
    (r"/rest/api/ohho/test/add/work/domain/", TestAddWorkDomainHandler),
    (r"/rest/api/ohho/test/add/body/type/", TestAddBodyTypeHandler),

    (r"/rest/api/ohho/test/add/match/condition/", TestAddMatchConditionHandler),
    (r"/rest/api/ohho/test/get/match/condition/", TestGetMatchConditionHandler),
    (r"/rest/api/ohho/test/match/", TestMatchHandler),
    (r"/rest/api/ohho/test/version2/match/", TestVersion2MatchHandler),
    # 测试接口
    (r"/rest/api/ohho/test/get/user/by/device/", TestGetUserByDeviceHandler),
    (r"/rest/api/ohho/test/get/device/version/", TestGetDeviceVersionHandler),

    (r"/rest/api/ohho/test/polling/get/apply/state/", TestPollingGetApplyStateHandler),
    (r"/rest/api/ohho/test/polling/get/apply/apply/", TestPollingGetApplyApplyHandler),

    (r"/rest/api/ohho/test/redis/get/hash/", TestGetRedisHashHandler),
    (r"/rest/api/ohho/test/redis/set/hash/", TestSetRedisHashHandler),

    (r"/rest/api/ohho/test/get/map/positions/", TestGetMapPositionsHandler),
    (r"/rest/api/ohho/test/get/user/information/", TestGetUserInformationHandler),
    (r"/rest/api/ohho/test/update/device/information/", TestUpdateDeviceInformationHandler),
    (r"/rest/api/ohho/test/add/timestamp/", TestAddTimestampHandler),

    (r"/rest/api/ohho/test/set/lost/", TestSetLostHandler),
    (r"/rest/api/ohho/test/cancel/lost/", TestCancelLostHandler),
    (r"/rest/api/ohho/test/set/device/use/", TestSetDeviceUseHandler),
    (r"/rest/api/ohho/test/get/bound/devices/", TestGetBoundDeviceHandler),

    (r"/rest/api/ohho/test/meet/end/", TestMeetEndHandler),
    (r"/rest/api/ohho/test/meet/by/hand/", TestMeetByHandHandler),
    (r"/rest/api/ohho/test/meet/not/by/hand/", TestNotMeetByHandHandler),
    (r"/rest/api/ohho/test/meet/by/device/", TestMeetByDeviceHandler),
    (r"/rest/api/ohho/test/get/basic/data/", TestGetBasicDataHandler),
    (r"/rest/api/ohho/test/get/meet/topic/", TestGetMeetTopicHandler),
    (r"/rest/api/ohho/test/get/meet/state/", TestGetMeetStateHandler),

    # 测试接口
    (r"/rest/api/ohho/get/user/by/device/", GetUserByDeviceHandler),
    (r"/rest/api/ohho/delete/apply/", DeleteApplyHandler),
    (r"/rest/api/ohho/delete/test/", DeleteTestHandler),
    (r"/rest/api/ohho/test/test/", TestTestHandler),
    (r"/rest/api/ohho/test/distance/", TestDistanceHandler),

    # 获取个人信息yangxd
    (r"/rest/api/ohho/test/get/user/personal/information/", TestGetUserPersonalInformationHandler),
    (r"/rest/api/ohho/test/get/user/personal/page/", TestGetUserPersonalPageHandler),
    (r"/rest/api/ohho/stress/test/add/user/", StressTestAddUserHandler),
    (r"/rest/api/view/ohho/stress/testint/add/user/", StressTestingAddUserHandler),
]
