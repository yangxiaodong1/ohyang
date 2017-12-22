
from ohho.common.view.backstage.management.permission.group_staff_relation.group_staff_relation_add import \
    BackstageGroupStaffRelationAddHandler
from ohho.common.view.backstage.management.permission.group_staff_relation.group_staff_relation_delete import \
    BackstageGroupStaffRelationDeleteHandler

from ohho.common.view.backstage.management.staff_list import BackstageStaffListHandler
from ohho.common.view.backstage.management.staff_add import BackstageStaffAddHandler
from ohho.common.view.backstage.management.staff_detail import BackstageStaffDetailHandler
from ohho.common.view.backstage.management.staff_delete import BackstageStaffDeleteHandler

from ohho.common.view.backstage.management.permission.group_user_relation.group_user_relation_add import \
    BackstageGroupUserRelationAddHandler
from ohho.common.view.backstage.management.permission.group_user_relation.group_user_relation_delete import \
    BackstageGroupUserRelationDeleteHandler

from ohho.common.view.backstage.management.permission.page.page_add import BackstagePageAddHandler
from ohho.common.view.backstage.management.permission.page.page_detail import BackstagePageDetailHandler
from ohho.common.view.backstage.management.permission.page.page_list import BackstagePageListHandler
from ohho.common.view.backstage.management.permission.page.page_delete import BackstagePageDeleteHandler

from ohho.common.view.backstage.management.permission.home import BackstagePermissionHomeHandler
from ohho.common.view.backstage.management.permission.group.group_add import BackstageGroupAddHandler
from ohho.common.view.backstage.management.permission.group.group_detail import BackstageGroupDetailHandler
from ohho.common.view.backstage.management.permission.group.group_list import BackstageGroupListHandler
from ohho.common.view.backstage.management.permission.group.group_delete import BackstageGroupDeleteHandler

from ohho.common.view.backstage.management.base.country_code.country_code_add import BackstageCountryCodeAddHandler
from ohho.common.view.backstage.management.base.country_code.country_code_detail import \
    BackstageCountryCodeDetailHandler
from ohho.common.view.backstage.management.base.country_code.country_code_list import BackstageCountryCodeListHandler
from ohho.common.view.backstage.management.base.country_code.country_code_delete import \
    BackstageCountryCodeDeleteHandler

from ohho.common.view.backstage.backstage_reset_password import BackageResetPasswordHandler
from ohho.common.view.backstage.register import BackstageRegisterHandler

from ohho.common.view.backstage.management.base.interest_backstage.interest_add import BackstageInterestAddHandler
from ohho.common.view.backstage.management.base.interest_backstage.interest_detail import BackstageInterestDetailHandler
from ohho.common.view.backstage.management.base.interest_backstage.interest_list import BackstageInterestListHandler
from ohho.common.view.backstage.management.base.interest_backstage.interest_delete import BackstageInterestDeleteHandler

from ohho.common.view.backstage.management.base.sensitive_backstage.sensitive_add import BackstageSensitiveAddHandler
from ohho.common.view.backstage.management.base.sensitive_backstage.sensitive_detail import \
    BackstageSensitiveDetailHandler
from ohho.common.view.backstage.management.base.sensitive_backstage.sensitive_list import BackstageSensitiveListHandler
from ohho.common.view.backstage.management.base.sensitive_backstage.sensitive_delete import \
    BackstageSensitiveDeleteHandler

from ohho.common.view.backstage.management.base.user_display_configuration.user_display_config_list import \
    BackstageUserDisplayConfigListHandler
from ohho.common.view.backstage.management.base.user_display_configuration.user_display_config_add import \
    BackstageUserDisplayConfigAddHandler
from ohho.common.view.backstage.management.base.user_display_configuration.user_display_config_detail import \
    BackstageUserDisplayConfigDetailHandler

from ohho.common.view.backstage.management.base.watchword.watchword_list import BackstageWatchwordListHandler
from ohho.common.view.backstage.management.base.watchword.watchword_detail import BackstageWatchwordDetailHandler
from ohho.common.view.backstage.management.base.watchword.wathcword_add import BackstageWatchwordAddHandler

from ohho.common.view.backstage.home import BackstageHomeHandler
from ohho.common.view.backstage.login import BackstageLoginHandler
from ohho.common.view.backstage.logout import BackstageLogoutHandler

from ohho.common.view.backstage.management.user_list import BackstageUserListHandler
from ohho.common.view.backstage.management.user_add import BackstageUserAddHandler
from ohho.common.view.backstage.management.user_detail import BackstageUserDetailHandler
from ohho.common.view.backstage.management.user_delete import BackstageUserDeleteHandler
from ohho.common.view.backstage.management.cellphone_list import BackstageCellphoneListHandler
from ohho.common.view.backstage.management.cellphone_add import BackstageCellphoneAddHandler
from ohho.common.view.backstage.management.cellphone_detail import BackstageCellphoneDetailHandler
from ohho.common.view.backstage.management.cellphone_delete import BackstageCellphoneDeleteHandler
from ohho.common.view.backstage.management.device_list import BackstageDeviceListHandler
from ohho.common.view.backstage.management.device_add import BackstageDeviceAddHandler
from ohho.common.view.backstage.management.device_detail import BackstageDeviceDetailHandler
from ohho.common.view.backstage.management.device_delete import BackstageDeviceDeleteHandler
from ohho.common.view.backstage.management.device_batch_add import BackstageDeviceBatchAddHandler

from ohho.common.view.backstage.management.relations.home import BackstageRelationHomeHandler
from ohho.common.view.backstage.management.relations.user_and_device_add import BackstageUserAndDeviceRelationAddHandler
from ohho.common.view.backstage.management.relations.user_and_device_detail import \
    BackstageUserAndDeviceRelationDetailHandler
from ohho.common.view.backstage.management.relations.user_and_device_delete import \
    BackstageUserAndDeviceRelationDeleteHandler

from ohho.common.view.backstage.management.relations.user_and_device_list import \
    BackstageUserAndDeviceRelationListHandler
from ohho.common.view.backstage.management.relations.user_and_cellphone_add import \
    BackstageUserAndCellphoneRelationAddHandler
from ohho.common.view.backstage.management.relations.user_and_cellphone_detail import \
    BackstageUserAndCellphoneRelationDetailHandler

from ohho.common.view.backstage.management.relations.user_and_cellphone_delete import \
    BackstageUserAndCellphoneRelationDeleteHandler
from ohho.common.view.backstage.management.relations.user_and_cellphone_list import \
    BackstageUserAndCellphoneRelationListHandler

from ohho.common.view.backstage.management.relations.im_user_add import \
    BackstageIMUserAddHandler
from ohho.common.view.backstage.management.relations.im_user_detail import \
    BackstageIMUserDetailHandler
from ohho.common.view.backstage.management.relations.im_user_delete import \
    BackstageIMUserDeleteHandler
from ohho.common.view.backstage.management.relations.im_user_list import \
    BackstageIMUserListHandler

from ohho.common.view.backstage.management.relations.user_and_match_condition_add import \
    BackstageUserAndMatchConditionAddHandler
from ohho.common.view.backstage.management.relations.user_and_match_condition_detail import \
    BackstageUserAndMatchConditionDetailHandler
from ohho.common.view.backstage.management.relations.user_and_match_condition_delete import \
    BackstageUserAndMatchConditionDeleteHandler
from ohho.common.view.backstage.management.relations.user_and_match_condition_list import \
    BackstageUserAndMatchConditionListHandler

from ohho.common.view.backstage.management.base.home import BackstageBaseHomeHandler
from ohho.common.view.backstage.management.base.hint.hint_list import BackstageHintListHandler
from ohho.common.view.backstage.management.base.hint.hint_add import BackstageHintAddHandler
from ohho.common.view.backstage.management.base.hint.hint_detail import BackstageHintDetailHandler
from ohho.common.view.backstage.management.base.hint.hint_delete import BackstageHintDeleteHandler

from ohho.common.view.backstage.management.base.drink.drink_add import BackstageDrinkAddHandler
from ohho.common.view.backstage.management.base.drink.drink_list import BackstageDrinkListHandler
from ohho.common.view.backstage.management.base.drink.drink_detail import BackstageDrinkDetailHandler
from ohho.common.view.backstage.management.base.smoke.smoke_add import BackstageSmokeAddHandler
from ohho.common.view.backstage.management.base.smoke.smoke_list import BackstageSmokeListHandler
from ohho.common.view.backstage.management.base.smoke.smoke_detail import BackstageSmokeDetailHandler
from ohho.common.view.backstage.management.base.profession.profession_add import BackstageProfessionAddHandler
from ohho.common.view.backstage.management.base.profession.profession_list import BackstageProfessionListHandler
from ohho.common.view.backstage.management.base.profession.profession_detail import BackstageProfessionDetailHandler
from ohho.common.view.backstage.management.base.industry.industry_add import BackstageIndustryAddHandler
from ohho.common.view.backstage.management.base.industry.industry_list import BackstageIndustryListHandler
from ohho.common.view.backstage.management.base.industry.industry_detail import BackstageIndustryDetailHandler
from ohho.common.view.backstage.management.base.body_type.body_type_add import BackstageBodyTypeAddHandler
from ohho.common.view.backstage.management.base.body_type.body_type_list import BackstageBodyTypeListHandler
from ohho.common.view.backstage.management.base.body_type.body_type_detail import BackstageBodyTypeDetailHandler
from ohho.common.view.backstage.management.base.work_domain.work_domain_add import BackstageWorkDomainAddHandler
from ohho.common.view.backstage.management.base.work_domain.work_domain_list import BackstageWorkDomainListHandler
from ohho.common.view.backstage.management.base.work_domain.work_domain_detail import BackstageWorkDomainDetailHandler
from ohho.common.view.backstage.management.base.match_condition.match_condition_add import \
    BackstageMatchConditionAddHandler
from ohho.common.view.backstage.management.base.match_condition.match_condition_list import \
    BackstageMatchConditionListHandler
from ohho.common.view.backstage.management.base.match_condition.match_condition_detail import \
    BackstageMatchConditionDetailHandler

from ohho.common.view.backstage.management.permission.group_page_relation.group_page_relation_list import \
    BackstageGroupPageRelationListHandler
from ohho.common.view.backstage.management.permission.group_page_relation.group_page_relation_add import \
    BackstageGroupPageRelationAddHandler
from ohho.common.view.backstage.management.permission.group_page_relation.group_page_relation_delete import \
    BackstageGroupPageRelationDeleteHandler
from ohho.common.view.backstage.management.permission.group_page_relation.group_page_relation_detail import \
    BackstageGroupPageRelationDetailHandler

from ohho.common.view.backstage.statistics.user import *
from ohho.common.view.backstage.statistics.device import *
from ohho.common.view.backstage.no_permission import *
