from Tools.ohho_uuid import OHHOUUID
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
from ohho.common.db.ohho.user.db_ohho_user_accuracy_extension import DBOHHOUserAccuracyExtension
from ohho.common.db.ohho.user.db_ohho_user_configuration import DBOHHOUserConfiguration

from ohho.common.logic.common.imei import IMEI
from ohho.common.logic.common.password import Password
from ohho.common.logic.common.record.friend import Friend
from ohho.common.logic.common.token import Token


from ohho.common.db.ohho.user.db_ohho_user_favourite_book import DBOHHOUserFavouriteBook
from ohho.common.db.ohho.user.db_ohho_user_favourite_movie import DBOHHOUserFavouriteMovie
from ohho.common.db.ohho.user.db_ohho_user_favourite_music import DBOHHOUserFavouriteMusic
from ohho.common.db.ohho.user.db_ohho_user_favourite_sport import DBOHHOUserFavouriteSport
from ohho.common.db.ohho.user.db_ohho_user_icon import DBOHHOUserIcon
from ohho.common.db.ohho.user.db_ohho_user_description import DBOHHOUserDescription
from ohho.common.db.ohho.user.db_ohho_user_impression import DBOHHOUserImpression
from ohho.common.db.ohho.relation.db_ohho_user_and_cellphone_relation import DBOHHOUserAndCellphoneRelation
from ohho.common.db.ohho.relation.db_ohho_user_and_device_imei import DBOHHOUserAndDeviceIMEI
import random
from Tools.ohho_random import OHHORandom
from stressTesting.tools.ohho_random import OhhoRandom
from DB.common.operation import Operation


class LogicAddUserNew(object):
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
        self.user_and_cellphone_relation = DBOHHOUserAndCellphoneRelation()

        self.user_favourite_book = DBOHHOUserFavouriteBook()
        self.user_favourite_movie = DBOHHOUserFavouriteMovie()
        self.user_favourite_sport = DBOHHOUserFavouriteSport()
        self.user_favourite_music = DBOHHOUserFavouriteMusic()
        self.user_icon = DBOHHOUserIcon()
        self.user_description = DBOHHOUserDescription()
        self.user_impression = DBOHHOUserImpression()

        # self.cellphone = 10000000000
        # self.identity_id = 9000000000

    def add_user(self):
        cellphone = 10000000000
        identity_id = 9000000000
        for i in range(10):
            cellphone = cellphone + 1
            identity_id = identity_id + 1
            while self.user.get_by_cellphone(cellphone):
                cellphone = cellphone + 1
            user_id = self.add_user_table(str(cellphone))
            self.add_user_token_table(user_id)
            self.add_user_extension(user_id)
            self.add_user_configuration(user_id)
            # self.add_user_and_cellphone_relation(user_id)
            self.device.set_identity(identity_id)
            while self.device.get_by_identity():
                identity_id = identity_id + 1
            device_id = self.add_device(identity_id)
            self.add_user_and_device_imei(user_id, device_id)
            self.add_user_and_device_relation(user_id, device_id)
            match_condition_id = self.add_match_condition()
            print("match_condition_id:")
            print(match_condition_id)
            self.add_user_match_condition(user_id, match_condition_id)

    def add_device(self, identity_id):
        data = dict()
        data["identity_id"] = identity_id
        self.device.add(data)
        query = self.device.get_query()
        query = self.device.order_by_id_desc(query)
        obj = Operation.first(query)
        return obj.id

    def add_match_condition(self):
        data = dict()
        data["sex"] = OhhoRandom.get_sex()
        data["small_age"] = 0
        data["big_age"] = 150
        data["interest"] = OhhoRandom.get_user_match_interest()
        self.match_condition.add(data)
        query = self.match_condition.get_query()
        query = self.match_condition.order_by_id_desc(query)
        obj = Operation.first(query)
        return obj.id

    def add_user_and_device_relation(self, user_id, device_id):
        data = dict()
        data["user_id"] = user_id
        data["device_id"] = device_id
        self.user_and_device_relation.add(data)

    def add_user_and_device_imei(self, user_id, device_id):
        data = dict()
        data["user_id"] = user_id
        data["device_id"] = device_id
        data["imei"] = OhhoRandom.get_imei()
        self.user_and_device_imei.add(data)

    def add_user_and_cellphone_relation(self, user_id):
        data = dict()
        data["user_id"] = user_id
        data["cellphone_id"] = OhhoRandom.get_cellphone_id()
        self.user_and_cellphone_relation.add(data)

    def add_user_configuration(self, user_id):
        data = dict()
        data["user_id"] = user_id
        data["is_match"] = 1
        data["is_online"] = 1
        self.user_configuration.add(data)

    def add_user_match_condition(self, user_id, match_condition_id):
        data = dict()
        data["user_id"] = user_id
        data["match_condition_id"] = match_condition_id
        self.record_user_and_match_condition.add(data)

    def add_user_extension(self, user_id):
        data = dict()
        data["user_id"] = user_id
        data["sex"] = OhhoRandom.get_sex()
        data["birthday"] = OhhoRandom.get_birthday()
        data["interest"] = OhhoRandom.get_user_interest()
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