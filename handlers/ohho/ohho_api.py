from ohho.views import *

handlers = [
    # 添加用户个人信息
    (r"/rest/api/ohho/exist/cellphone/", ExistCellphoneHandler),
    (r"/rest/api/ohho/complete/user/", CompleteUserHandler),
    (r"/rest/api/ohho/add/user/icon/", AddUserIconHandler),
    (r"/rest/api/ohho/add/user/basic/", AddUserBasicHandler),
    (r"/rest/api/ohho/add/user/favourite/book/", AddUserFavouriteBookHandler),
    (r"/rest/api/ohho/add/user/favourite/movie/", AddUserFavouriteMovieHandler),
    (r"/rest/api/ohho/add/user/favourite/music/", AddUserFavouriteMusicHandler),
    (r"/rest/api/ohho/add/user/favourite/sport/", AddUserFavouriteSportHandler),

    # 获取个人信息（进入个人信息的时候显示的数据）
    (r"/rest/api/ohho/get/user/personal/information/", GetUserPersonalInformationHandler),
    (r"/rest/api/ohho/get/user/personal/page/", GetUserPersonalPageHandler),
    # 添加用户个人信息

    (r"/rest/api/ohho/add/user/exclude/", AddUserExcludeHandler),
    (r"/rest/api/ohho/add/one/user/exclude/", AddOneUserExcludeHandler),
    (r"/rest/api/ohho/delete/one/user/exclude/", DeleteOneUserExcludeHandler),

    (r"/rest/api/ohho/rebind/cellphone/", RebindCellphoneHandler),
    (r"/rest/api/ohho/add/device/", AddDeviceHandler),
    # (r"/rest/api/ohho/is/device/valid/", IsDeviceValidHandler),
    (r"/rest/api/ohho/bind/device/", BindDeviceHandler),
    (r"/rest/api/ohho/unbind/device/", UnbindDeviceHandler),
    (r"/rest/api/ohho/cellphone/unbind/device/", CellphoneUnbindDeviceHandler),

    (r"/rest/api/ohho/login/", LoginHandler),
    (r"/rest/api/ohho/login/by/code/", LoginByCodeHandler),
    (r"/rest/api/ohho/logout/", LogoutHandler),
    (r"/rest/api/ohho/register/", RegisterHandler),
    (r"/rest/api/ohho/unregister/", UnregisterHandler),

    (r"/rest/api/ohho/match/", MatchHandler),
    (r"/rest/api/ohho/version2/match/", Version2MatchHandler),
    (r"/rest/api/ohho/version3/match/", Version3MatchHandler),
    (r"/rest/api/ohho/meet/", MeetHandler),

    (r"/rest/api/ohho/add/exclude/", AddExcludeHandler),
    (r"/rest/api/ohho/get/user/and/device/imei/", GetUserAndDeviceIMEIHandler),

    # 见面接口
    (r"/rest/api/ohho/apply/meet/", ApplyMeetHandler),
    (r"/rest/api/ohho/agree/meet/", AgreeMeetHandler),
    (r"/rest/api/ohho/refuse/meet/", RefuseMeetHandler),
    (r"/rest/api/ohho/cancel/meet/", CancelMeetHandler),

    (r"/rest/api/ohho/end/meet/", MeetEndHandler),
    (r"/rest/api/ohho/met/by/hand/", MetByHandHandler),
    (r"/rest/api/ohho/met/by/device/", MetByDeviceHandler),

    (r"/rest/api/ohho/add/meet/", AddMeetHandler),
    # 交友接口
    (r"/rest/api/ohho/apply/friend/", ApplyFriendHandler),
    (r"/rest/api/ohho/agree/friend/", AgreeFriendHandler),
    (r"/rest/api/ohho/remove/friend/", RemoveFriendHandler),
    (r"/rest/api/ohho/refuse/friend/", RefuseFriendHandler),
    (r"/rest/api/ohho/list/apply/friend/", ListApplyFriendHandler),

    # im
    (r"/rest/api/ohho/im/list/friends/", ListFriendsHandler),
    (r"/rest/api/ohho/im/list/blacks/", ListBlacksHandler),
    (r"/rest/api/ohho/im/add/black/", AddBlackHandler),
    (r"/rest/api/ohho/im/remove/black/", RemoveBlackHandler),

    # 蓝牙设备密码
    (r"/rest/api/ohho/add/device/setting/", AddDeviceSettingHandler),
    (r"/rest/api/ohho/update/device/setting/", UpdateDeviceSettingHandler),
    (r"/rest/api/ohho/get/device/setting/", GetDeviceSettingHandler),

    (r"/rest/api/ohho/add/report/", AddReportHandler),
    (r"/rest/api/ohho/get/report/type/", GetReportTypeHandler),
    (r"/rest/api/ohho/add/feedback/", AddFeedbackHandler),
    (r"/rest/api/ohho/get/feedback/type/", GetFeedbackTypeHandler),
    (r"/rest/api/ohho/get/cancel/meet/feedback/type/", GetCancelMeetFeedbackTypeHandler),
    (r"/rest/api/ohho/get/complete/meet/feedback/type/", GetCompleteMeetFeedbackTypeHandler),
    (r"/rest/api/ohho/add/cancel/meet/feedback/", AddCancelMeetFeedbackHandler),
    (r"/rest/api/ohho/add/complete/meet/feedback/", AddCompleteMeetFeedbackHandler),

    (r"/rest/api/ohho/upload/map/position/", UploadMapPositionHandler),
    (r"/rest/api/ohho/get/friend/map/position/", GetFriendMapPositionHandler),
    (r"/rest/api/ohho/find/device/position/", FindDevicePositionHandler),

    (r"/rest/api/ohho/send/verification/code/", SendVerificationCodeHandler),
    (r"/rest/api/ohho/check/verification/code/", CheckVerificationCodeHandler),
    (r"/rest/api/ohho/bluetooth/position/", BluetoothPositionHandler),
    (r"/rest/api/ohho/is/device/valid/", IsDeviceValidHandler),
    (r"/rest/api/ohho/open/match/switch/", OpenMatchSwitchHandler),
    (r"/rest/api/ohho/close/match/switch/", CloseMatchSwitchHandler),
    # (r"/rest/api/ohho/set/match/switch/", SetMatchSwitchHandler),

    (r"/rest/api/ohho/set/lost/", SetLostHandler),
    (r"/rest/api/ohho/cancel/lost/", CancelLostHandler),

    (r"/rest/api/ohho/open/online/switch/", OpenOnlineSwitchHandler),
    (r"/rest/api/ohho/close/online/switch/", CloseOnlineSwitchHandler),
    # (r"/rest/api/ohho/set/online/switch/", SetOnlineSwitchHandler),
    (r"/rest/api/ohho/map/distance/", MapDistanceHandler),
    (r"/rest/api/ohho/reset/password/", ResetPasswordHandler),
    (r"/rest/api/ohho/update/user/and/cellphone/relation/",
     UpdateUserAndCellphoneRelationHandler),

    (r"/rest/api/ohho/add/user/accuracy/extension/", AddUserAccuracyExtensionHandler),
    (r"/rest/api/ohho/update/cellphone/number/", UpdateCellphoneNumberHandler),

    (r"/rest/api/ohho/add/drink/", AddDrinkHandler),
    (r"/rest/api/ohho/add/smoke/", AddSmokeHandler),
    (r"/rest/api/ohho/add/profession/", AddProfessionHandler),
    (r"/rest/api/ohho/add/industry/", AddIndustryHandler),
    (r"/rest/api/ohho/add/body/type/", AddBodyTypeHandler),
    (r"/rest/api/ohho/add/work/domain/", AddWorkDomainHandler),

    (r"/rest/api/ohho/add/match/condition/", AddMatchConditionHandler),
    (r"/rest/api/ohho/get/match/condition/", GetMatchConditionHandler),
    (r"/rest/api/ohho/match/", MatchHandler),

    (r"/rest/api/ohho/get/device/version/", GetDeviceVersionHandler),
    (r"/rest/api/ohho/add/device/version/", AddDeviceVersionHandler),

    (r"/rest/api/ohho/get/map/positions/", GetMapPositionsHandler),
    (r"/rest/api/ohho/get/user/information/", GetUserInformationHandler),

    (r"/rest/api/ohho/polling/get/apply/state/", PollingGetMatchStateHandler),
    (r"/rest/api/ohho/polling/get/apply/apply/", PollingGetMatchApplyHandler),

    (r"/rest/api/ohho/set/device/use/", SetDeviceUseHandler),
    (r"/rest/api/ohho/get/bound/devices/", GetBoundDevicesHandler),

    (r"/rest/api/ohho/get/basic/data/", GetBasicDataHandler),
    (r"/rest/api/ohho/get/meet/topic/", MeetTopicHandler),
    (r"/rest/api/ohho/get/meet/state/", MeetStateHandler),
    (r"/rest/api/ohho/get/meet/address/", WhereMeetHandler),

]
