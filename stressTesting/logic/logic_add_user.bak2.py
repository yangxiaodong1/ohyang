from Tools.ohho_uuid import OHHOUUID
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_log import OHHOLog
from Tools.ohho_operation import OHHOOperation
from ohho.common.db.ohho.base.db_ohho_country_code import DBOHHOCountryCode
from ohho.common.db.ohho.base.db_ohho_interest import DBOHHOInterest
from ohho.common.db.ohho.device.db_ohho_device import DBOHHODevice
from ohho.common.db.ohho.im.db_ohho_im_user import DBOHHOIMUser
from ohho.common.db.ohho.im.db_ohho_im_user_relation import DBOHHOIMUserRelation
from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
from ohho.common.db.ohho.record.db_ohho_record_match_apply import DBOHHORecordMatchApply
from ohho.common.db.ohho.record.db_ohho_record_match_condition import DBOHHORecordMatchCondition
from ohho.common.db.ohho.record.db_ohho_record_user_and_match_condition import DBOHHORecordUserAndMatchCondition
from ohho.common.db.ohho.relation.db_ohho_user_and_device_relation import DBOHHOUserAndDeviceRelation
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
# from ohho.common.db.ohho.user.db_ohho_user_icon import DBOHHOUserIcon
from ohho.common.db.ohho.user.db_ohho_user_accuracy_extension import DBOHHOUserAccuracyExtension
from ohho.common.db.ohho.user.db_ohho_user_configuration import DBOHHOUserConfiguration
from ohho.common.logic.common.code import Code
from ohho.common.logic.common.im.netease.refresh_token import RefreshToken
from ohho.common.logic.common.im.netease.send_message import SendMessage
from ohho.common.logic.common.imei import IMEI
from ohho.common.logic.common.password import Password
from ohho.common.logic.common.record.friend import Friend
from ohho.common.logic.common.token import Token

from ohho.common.db.ohho.relation.db_ohho_user_and_device_imei import DBOHHOUserAndDeviceIMEI
from Tools.ohho_random import OHHORandom
from stressTesting.tools.ohho_random import OhhoRandom
from DB.common.operation import Operation



class LogicAddUser(object):
    def __init__(self):
        self.user = DBOHHOUser()
        self.user_and_device_relation = DBOHHOUserAndDeviceRelation()
        self.password = Password()
        self.token = Token()
        self.user_extension = DBOHHOUserAccuracyExtension()
        self.interest = DBOHHOInterest()
        self.map = DBOHHOMapInformation()
        self.device = DBOHHODevice()
        self.record_user_and_match_condition = DBOHHORecordUserAndMatchCondition()
        self.match_condition = DBOHHORecordMatchCondition()
        self.im_user = DBOHHOIMUser()
        self.im_user_relation = DBOHHOIMUserRelation()
        self.user_configuration = DBOHHOUserConfiguration()
        self.imei = IMEI()
        self.user_and_device_imei = DBOHHOUserAndDeviceIMEI()
        self.friend = Friend()
        self.apply = DBOHHORecordMatchApply()
        self.country_code = DBOHHOCountryCode()

    def add_user(self, number=10):
        cellphone = 10000000000
        # identity_card = 100000000000000000
        user_query = self.user.get_query()
        user_query = self.user.order_by_id_desc(user_query)
        user_obj = Operation.first(user_query)
        if user_obj:
            if user_obj.cellphone:
                cellphone = int(user_obj.cellphone)
        i = 0
        while i <= number:
            i += 1
            cellphone += 1
            while self.user.get_by_cellphone(str(cellphone)):
                cellphone = cellphone + 1
            user_id = self.add_user_table(str(cellphone))
            self.add_user_token_table(user_id)
            self.add_user_extension(user_id)

        print("for end")
        print("end")

    def add_func(self, number, cellphone):



    def add_user_extension(self, user_id):
        data = dict()
        data["user_id"] = user_id
        data["sex"] = OhhoRandom.get_sex()
        # data["identity_card"] = identity_card
        # data["real_name"] = ""
        data["nickname"] = "宝宝"
        data["birthday"] = OhhoRandom.get_birthday()

        self.user_extension.add(data)

    def add_user_token_table(self, user_id):
        token = OHHORandom.get_nonce()
        token_dict = dict()
        token_dict["user_id"] = user_id
        token_dict["token"] = token
        self.token.token.add(token_dict)

    def add_user_table(self, cellphone="00000000000"):
        """添加用户 参数 """
        data = dict()
        password = "666666"
        country_code_id = 159
        username = OHHOUUID.get_uuid1_string()
        self.password.set_password(password)
        encryption_password = self.password.encryption()
        data["username"] = username
        data["password"] = encryption_password
        data["cellphone"] = cellphone
        data["country_code_id"] = country_code_id
        self.user.add(data)
        user = self.user.get_by_username(username)
        return user.id