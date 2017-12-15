from ohho.common.db.ohho.user.db_ohho_user_display_configuration import DBOHHOUserDisplayConfiguration
# from DB.mysql.models.ohho.model_ohho_watchword import OHHOWatchword
from ohho.common.logic.common.base.base_class import BaseClass
from DB.common.operation import Operation

class UserDisplayConfiguration(BaseClass):
    """后台用户配置信息"""
    def __init__(self):
        super(UserDisplayConfiguration, self).__init__(DBOHHOUserDisplayConfiguration)