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
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.token import Token
from ohho.common.logic.ohho.detail_constant import *
from ohho.common.logic.common.record.constant import VALID_INTERVAL_MILLISECOND_THREE
from DB.redis.operation import RedisDB
from ohho.common.logic.common.constant import *

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
        self.user_and_cellphone_relation = DBOHHOUserAndCellphoneRelation()

        self.user_favourite_book = DBOHHOUserFavouriteBook()
        self.user_favourite_movie = DBOHHOUserFavouriteMovie()
        self.user_favourite_sport = DBOHHOUserFavouriteSport()
        self.user_favourite_music = DBOHHOUserFavouriteMusic()
        self.user_icon = DBOHHOUserIcon()
        self.user_description = DBOHHOUserDescription()
        self.user_impression = DBOHHOUserImpression()

    def add_user(self):
        cellphone = 10000000000
        identity_card = 100000000000000000
        user_query = self.user.get_query()
        user_query = self.user.order_by_id_desc(user_query)
        user_obj = Operation.first(user_query)
        if user_obj:
            cellphone = int(user_obj.cellphone)

        for i in range(100):
            cellphone += 1
            # identity_card += 1
            while self.user.get_by_cellphone(cellphone):
                cellphone = cellphone + 1
            user_id = self.add_user_table(str(cellphone))
            self.add_user_token_table(user_id)
            self.add_user_extension(user_id, identity_card)
            # self.add_user_match_condition(user_id)
            # self.add_user_configuration(user_id)
            # self.add_user_and_cellphone_relation(user_id)
            # self.add_user_and_device_imei(user_id)
            # self.add_user_and_device_relation(user_id)
            # self.add_user_description(user_id)
            # self.add_user_favourite_book(user_id)
            # self.add_user_favourite_movie(user_id)
            # self.add_user_favourite_music(user_id)
            # self.add_user_favourite_sport(user_id)
            # self.add_user_icon(user_id)
            # self.add_user_impression(user_id)

    def add_user_impression(self, user_id):
        data = dict()
        obj = OhhoRandom.get_user_impression()
        data["user_id"] = user_id
        data["another_user_id"] = obj.get("another_user_id", "")
        data["content_id"] = obj.get("content_id", "")
        data["apply_id"] = obj.get("apply_id", "")
        data["type"] = obj.get("type", "")
        self.user_impression.add(data)

    def add_user_icon(self, user_id):
        data = dict()
        obj = OhhoRandom.get_user_icon()
        data["user_id"] = user_id
        data["icon"] = obj.get("icon", "")
        data["is_head_sculpture"] = obj.get("is_head_sculpture", "")
        data["thumbnail"] = obj.get("thumbnail", "")
        self.user_icon.add(data)

    def add_user_favourite_sport(self, user_id):
        data = dict()
        obj = OhhoRandom.get_favourite_sport()
        data["user_id"] = user_id
        data["sport_id"] = obj.get("sport_id", "")
        data["name"] = obj.get("name", "")
        data["description"] = obj.get("description", "")
        data["index"] = obj.get("index", "")
        self.user_favourite_sport.add(data)

    def add_user_favourite_music(self, user_id):
        data = dict()
        obj = OhhoRandom.get_favourite_music()
        data["user_id"] = user_id
        data["music_id"] = obj.get("music_id", "")
        data["name"] = obj.get("name", "")
        data["description"] = obj.get("description", "")
        data["album"] = obj.get("album", "")
        data["publisher"] = obj.get("publisher", "")
        data["singer"] = obj.get("singer", "")
        data["icon"] = obj.get("icon", "")
        data["url"] = obj.get("url", "")
        self.user_favourite_music.add(data)

    def add_user_favourite_movie(self, user_id):
        data = dict()
        obj = OhhoRandom.get_favourite_movie()
        data["user_id"] = user_id
        data["movie_id"] = obj.get("movie_id", "")
        data["name"] = obj.get("name", "")
        data["description"] = obj.get("description", "")
        data["index"] = obj.get("index", "")
        data["casts"] = obj.get("casts", "")
        data["genres"] = obj.get("genres", "")
        data["icon"] = obj.get("icon", "")
        data["url"] = obj.get("url", "")
        self.user_favourite_movie.add(data)

    def add_user_favourite_book(self, user_id):
        data = dict()
        obj = OhhoRandom.get_favourite_book()
        data["user_id"] = user_id
        data["isbn"] = obj.get("isbn", "")
        data["name"] = obj.get("name", "")
        data["description"] = obj.get("description", "")
        data["index"] = obj.get("index", "")
        data["icon"] = obj.get("icon", "")
        data["author"] = obj.get("author", "")
        data["url"] = obj.get("url", "")
        self.user_favourite_book.add(data)

    def add_user_description(self, user_id):
        data = dict()
        data["user_id"] = user_id
        data["type"] = OhhoRandom.get_type()
        data["first"] = OhhoRandom.get_first()
        data["second"] = OhhoRandom.get_second()
        data["third"] = OhhoRandom.get_third()
        self.user_description.add(data)

    def add_user_and_device_relation(self, user_id):
        data = dict()
        data["user_id"] = user_id
        data["device_id"] = OhhoRandom.get_device_id
        self.user_and_device_relation.add(data)

    def add_user_and_device_imei(self, user_id):
        data = dict()
        data["user_id"] = user_id
        data["device_id"] = OhhoRandom.get_device_id
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

    def add_user_match_condition(self, user_id):
        data = dict()
        data["user_id"] = user_id
        data["match_condition_id"] = OhhoRandom.get_match_condition_id()
        self.match_condition.add(data)

    def add_user_extension(self, user_id, identity_card):
        data = dict()
        data["user_id"] = user_id
        data["sex"] = OhhoRandom.get_sex()
        # data["identity_card"] = identity_card
        # data["real_name"] = ""
        data["nickname"] = "宝宝"
        data["birthday"] = OhhoRandom.get_birthday()
        # data["height"] = OhhoRandom.get_height()
        # data["hometown"] = OhhoRandom.get_hometown()
        # data["school"] = OhhoRandom.get_school()
        # data["company"] = OhhoRandom.get_company()
        # data["degree_id"] = OhhoRandom.get_degree_id()
        # data["favourite_live_city"] = OhhoRandom.get_favourite_live_city()
        # data["occupation_id"] = OhhoRandom.get_occupation_id()
        # data["position_id"] = OhhoRandom.get_position_id()

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