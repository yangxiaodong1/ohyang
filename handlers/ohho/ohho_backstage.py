from ohho.backstage_views import *

handlers = [
    # 后台
    (r"/backstage/login/", BackstageLoginHandler),
    (r"/backstage/logout/", BackstageLogoutHandler),
    (r"/backstage/home/", BackstageHomeHandler),
    (r"/backstage/register/", BackstageRegisterHandler),
    (r"/backstage/reset_password/", BackageResetPasswordHandler),

    (r"/backstage/management/user/list/", BackstageUserListHandler),
    (r"/backstage/management/user/add/", BackstageUserAddHandler),
    (r"/backstage/management/user/detail/", BackstageUserDetailHandler),
    (r"/backstage/management/user/delete/", BackstageUserDeleteHandler),
    (r"/backstage/management/cellphone/list/", BackstageCellphoneListHandler),
    (r"/backstage/management/cellphone/add/", BackstageCellphoneAddHandler),
    (r"/backstage/management/cellphone/detail/", BackstageCellphoneDetailHandler),
    (r"/backstage/management/cellphone/delete/", BackstageCellphoneDeleteHandler),
    (r"/backstage/management/device/list/", BackstageDeviceListHandler),
    (r"/backstage/management/device/add/", BackstageDeviceAddHandler),
    (r"/backstage/management/device/detail/", BackstageDeviceDetailHandler),
    (r"/backstage/management/device/delete/", BackstageDeviceDeleteHandler),
    (r"/backstage/management/device/batch_add/", BackstageDeviceBatchAddHandler),

    (r"/backstage/management/staff/list/", BackstageStaffListHandler),
    (r"/backstage/management/staff/add/", BackstageStaffAddHandler),
    (r"/backstage/management/staff/detail/", BackstageStaffDetailHandler),
    (r"/backstage/management/staff/delete/", BackstageStaffDeleteHandler),

    (r"/backstage/management/relations/home/", BackstageRelationHomeHandler),
    (r"/backstage/management/relations/device/add/", BackstageUserAndDeviceRelationAddHandler),
    (r"/backstage/management/relations/device/detail/", BackstageUserAndDeviceRelationDetailHandler),
    (r"/backstage/management/relations/device/delete/", BackstageUserAndDeviceRelationDeleteHandler),
    (r"/backstage/management/relations/device/list/", BackstageUserAndDeviceRelationListHandler),
    (r"/backstage/management/relations/cellphone/add/", BackstageUserAndCellphoneRelationAddHandler),
    (r"/backstage/management/relations/cellphone/detail/", BackstageUserAndCellphoneRelationDetailHandler),
    (r"/backstage/management/relations/cellphone/delete/", BackstageUserAndCellphoneRelationDeleteHandler),
    (r"/backstage/management/relations/cellphone/list/", BackstageUserAndCellphoneRelationListHandler),
    (r"/backstage/management/relations/im/user/add/", BackstageIMUserAddHandler),
    (r"/backstage/management/relations/im/user/detail/", BackstageIMUserDetailHandler),
    (r"/backstage/management/relations/im/user/delete/", BackstageIMUserDeleteHandler),
    (r"/backstage/management/relations/im/user/list/", BackstageIMUserListHandler),
    (r"/backstage/management/relations/match/condition/add/", BackstageUserAndMatchConditionAddHandler),
    (r"/backstage/management/relations/match/condition/detail/", BackstageUserAndMatchConditionDetailHandler),
    (r"/backstage/management/relations/match/condition/delete/", BackstageUserAndMatchConditionDeleteHandler),
    (r"/backstage/management/relations/match/condition/list/", BackstageUserAndMatchConditionListHandler),

    (r"/backstage/management/base/home/", BackstageBaseHomeHandler),
    (r"/backstage/management/base/drink/list/", BackstageDrinkListHandler),
    (r"/backstage/management/base/drink/add/", BackstageDrinkAddHandler),
    (r"/backstage/management/base/drink/detail/", BackstageDrinkDetailHandler),
    (r"/backstage/management/base/smoke/list/", BackstageSmokeListHandler),
    (r"/backstage/management/base/smoke/add/", BackstageSmokeAddHandler),
    (r"/backstage/management/base/smoke/detail/", BackstageSmokeDetailHandler),
    (r"/backstage/management/base/industry/list/", BackstageIndustryListHandler),
    (r"/backstage/management/base/industry/add/", BackstageIndustryAddHandler),
    (r"/backstage/management/base/industry/detail/", BackstageIndustryDetailHandler),
    (r"/backstage/management/base/profession/list/", BackstageProfessionListHandler),
    (r"/backstage/management/base/profession/add/", BackstageProfessionAddHandler),
    (r"/backstage/management/base/profession/detail/", BackstageProfessionDetailHandler),
    (r"/backstage/management/base/body_type/list/", BackstageBodyTypeListHandler),
    (r"/backstage/management/base/body_type/add/", BackstageBodyTypeAddHandler),
    (r"/backstage/management/base/body_type/detail/", BackstageBodyTypeDetailHandler),
    (r"/backstage/management/base/work_domain/list/", BackstageWorkDomainListHandler),
    (r"/backstage/management/base/work_domain/add/", BackstageWorkDomainAddHandler),
    (r"/backstage/management/base/work_domain/detail/", BackstageWorkDomainDetailHandler),
    (r"/backstage/management/base/match/condition/list/", BackstageMatchConditionListHandler),
    (r"/backstage/management/base/match/condition/add/", BackstageMatchConditionAddHandler),
    (r"/backstage/management/base/match/condition/detail/", BackstageMatchConditionDetailHandler),

    (r"/backstage/management/base/watchword/list/", BackstageWatchwordListHandler),
    (r"/backstage/management/base/watchword/add/", BackstageWatchwordAddHandler),
    (r"/backstage/management/base/watchword/detail/", BackstageWatchwordDetailHandler),

    (r"/backstage/management/base/user_display_configuration/list/", BackstageUserDisplayConfigListHandler),
    (r"/backstage/management/base/user_display_configuration/add/", BackstageUserDisplayConfigAddHandler),
    (r"/backstage/management/base/user_display_configuration/detail/", BackstageUserDisplayConfigDetailHandler),

    (r"/backstage/management/base/sensitive/list/", BackstageSensitiveListHandler),
    (r"/backstage/management/base/sensitive/add/", BackstageSensitiveAddHandler),
    (r"/backstage/management/base/sensitive/detail/", BackstageSensitiveDetailHandler),
    (r"/backstage/management/base/sensitive/delete/", BackstageSensitiveDeleteHandler),

    (r"/backstage/management/base/interest_backstage/list/", BackstageInterestListHandler),
    (r"/backstage/management/base/interest_backstage/add/", BackstageInterestAddHandler),
    (r"/backstage/management/base/interest_backstage/detail/", BackstageInterestDetailHandler),
    (r"/backstage/management/base/interest_backstage/delete/", BackstageInterestDeleteHandler),

    (r"/backstage/management/base/country_code/list/", BackstageCountryCodeListHandler),
    (r"/backstage/management/base/country_code/add/", BackstageCountryCodeAddHandler),
    (r"/backstage/management/base/country_code/detail/", BackstageCountryCodeDetailHandler),
    (r"/backstage/management/base/country_code/delete/", BackstageCountryCodeDeleteHandler),

    (r"/backstage/management/base/hint/list/", BackstageHintListHandler),
    (r"/backstage/management/base/hint/add/", BackstageHintAddHandler),
    (r"/backstage/management/base/hint/detail/", BackstageHintDetailHandler),
    (r"/backstage/management/base/hint/delete/", BackstageHintDeleteHandler),

    # 权限
    (r"/backstage/management/permission/home/", BackstagePermissionHomeHandler),
    (r"/backstage/management/permission/group/list/", BackstageGroupListHandler),
    (r"/backstage/management/permission/group/add/", BackstageGroupAddHandler),
    (r"/backstage/management/permission/group/detail/", BackstageGroupDetailHandler),
    (r"/backstage/management/permission/group/delete/", BackstageGroupDeleteHandler),

    (r"/backstage/management/permission/group/permission/list/", BackstageGroupPageRelationListHandler),
    (r"/backstage/management/permission/group/permission/add/", BackstageGroupPageRelationAddHandler),
    (r"/backstage/management/permission/group/permission/detail/", BackstageGroupPageRelationDetailHandler),
    (r"/backstage/management/permission/group/permission/delete/", BackstageGroupPageRelationDeleteHandler),

    (r"/backstage/management/permission/page/list/", BackstagePageListHandler),
    (r"/backstage/management/permission/page/add/", BackstagePageAddHandler),
    (r"/backstage/management/permission/page/detail/", BackstagePageDetailHandler),
    (r"/backstage/management/permission/page/delete/", BackstagePageDeleteHandler),

    (r"/backstage/management/permission/group/user/relation/add/", BackstageGroupUserRelationAddHandler),
    (r"/backstage/management/permission/group/user/relation/delete/", BackstageGroupUserRelationDeleteHandler),

    (r"/backstage/management/permission/group/staff/relation/add/", BackstageGroupStaffRelationAddHandler),
    (r"/backstage/management/permission/group/staff/relation/delete/", BackstageGroupStaffRelationDeleteHandler),

    (r"/backstage/statistics/user/", BackstageStatisticsUserHandler),
    (r"/backstage/statistics/device/", BackstageStatisticsDeviceHandler),
    (r"/backstage/no/permission/", BackstageNoPermissionHandler),
]
