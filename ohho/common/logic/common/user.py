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

DEFAULT_ICON = "static/image/timg.jpg"
DEFAULT_NICKNAME = "xiaobai"

FRIEND_RELATION_NO_RELATION = 0
FRIEND_RELATION_FRIEND = 1
FRIEND_RELATION_BLACK = 2
FRIEND_RELATION_MY_VALID_APPLY = 3
FRIEND_RELATION_MY_VALID_APPLIED = 4


class User(object):
    def __init__(self, username=None):
        self.username = username
        self.user = DBOHHOUser()
        # self.user_icon = DBOHHOUserIcon()
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
        self.friend = Friend()
        self.apply = DBOHHORecordMatchApply()
        self.country_code = DBOHHOCountryCode()

        self.user_favourite_book = DBOHHOUserFavouriteBook()
        self.user_favourite_movie = DBOHHOUserFavouriteMovie()
        self.user_favourite_sport = DBOHHOUserFavouriteSport()
        self.user_favourite_music = DBOHHOUserFavouriteMusic()
        self.user_icon = DBOHHOUserIcon()
        self.user_description = DBOHHOUserDescription()
        self.user_impression = DBOHHOUserImpression()

    def get_age(self, birthday):
        if birthday:
            now = OHHODatetime.get_now()
            now_year = OHHODatetime.get_year(now)
            birthday_year = OHHODatetime.get_year(birthday)
            return now_year - birthday_year + 1
        else:
            return -1

    def clear_user_geo_position(self, user_id):
        user = self.get_by_id(user_id)
        if user:
            longitude = -1
            latitude = -1
            RedisDB.geo_add(REDIS_GEO_POSITION, longitude, latitude, user.username)
            return True
        else:
            return False

    def add_user_geo_position(self, longitude, latitude, username):
        RedisDB.geo_add(REDIS_GEO_POSITION, longitude, latitude, username)

    def set_user_map_information(self, username, information):
        RedisDB.hash_set(REDIS_MAP_INFORMATION, username, information)

    def get_user_map_information_from_redis(self, username):
        return RedisDB.hash_get(REDIS_MAP_INFORMATION, username)

    def get_user_map_information(self, user_id):
        result = dict()
        user = self.get_by_id(user_id)
        if user:
            result["user_id"] = user_id
            result["longitude"] = 0
            result["latitude"] = 0
            result["address"] = ""
            data = RedisDB.hash_get(REDIS_MAP_INFORMATION, user.username)
            OHHOLog.print_log(data)
            data_dict = RedisDB.data2dict(data)
            OHHOLog.print_log(data_dict)
            if data_dict:
                result["user_id"] = user_id
                result["longitude"] = float(data_dict["longitude"])
                result["latitude"] = float(data_dict["latitude"])
                result["address"] = data_dict["address"]
            return result
        else:
            return dict()

    def get_nearby_users(self, user_id):
        result = list()
        user = self.get_by_id(user_id)
        if user:
            user_position = RedisDB.geo_position(REDIS_GEO_POSITION, user.username)
            if user_position:
                temp = RedisDB.geo_radius(REDIS_GEO_POSITION, user_position[0][0], user_position[0][1], 2, unit="km",
                                          withcoord=True)
                if temp:
                    for t in temp:
                        name = t[0]
                        longitude = t[1][0]
                        latitude = t[1][1]
                        if name == user.username or longitude <= 0 or latitude <= 0:
                            continue
                        else:
                            result.append(name)
        return list(set(result))

    def get_user_id_by_username(self, username):
        user = self.get_by_username(username)
        if user:
            return user.id
        else:
            return 0

    def get_country_code(self, country_code):
        return self.country_code.get_by_country_code(country_code)

    def get_country_code_id(self, country_code):
        country_code_object = self.country_code.get_by_country_code(country_code)
        return country_code_object.id if country_code_object else 0

    def get_country_code_by_id(self, country_code_id):
        return self.country_code.get_country_code_by_id(country_code_id)

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password.set_password(password)

    def get_password(self):
        return self.password.password

    def set_user_password(self, instance, password):
        if instance and password:
            self.password.set_password(password)
            encryption_password = self.password.encryption()
            user_dict = {"password": encryption_password}
            return self.user.update(instance, user_dict)
        else:
            return False

    def add_user(self, password, cellphone=None, country_code="+86"):
        username = self.username
        if username and password and country_code:
            self.password.set_password(password)
            encryption_password = self.password.encryption()
            user = self.user.get_by_username(username)
            country_code_object = self.get_country_code(country_code)
            if country_code_object:
                exist_cellphone = self.get_by_country_code_and_cellphone(country_code_object.id, cellphone)
            else:
                return Result.result_failed("country code is invalid!")
            if user:
                return Result.result_failed("username exists!")
                # if self.user.is_valid(user, True):
                #     return Result.result_exist(USER_EXIST)
                # else:
                #     restore_success = self.user.restore(user)
                #     change_password_success = self.user.update(user, {"password": encryption_password})
                #     if restore_success and change_password_success:
                #         return Result.result_success(RESTORE_USER_SUCCESS)
                #     else:
                #         return Result.result_exist(RESTORE_USER_FAILED)
            elif exist_cellphone:
                return Result.result_failed("cellphone exist!")
            else:
                data = dict()
                data["username"] = username
                data["password"] = encryption_password
                data["cellphone"] = cellphone
                data["country_code_id"] = country_code_object.id
                data["last_login"] = OHHODatetime.get_utc_now()
                # OHHOLog.print_log(data)
                # OHHOLog.print_log(country_code)
                # obj_country_code = self.country_code.get_by_country_code(country_code)
                # if obj_country_code:
                #     OHHOLog.print_log(obj_country_code.id)
                #     data["country_code_id"] = obj_country_code.id
                # else:
                #     OHHOLog.print_log("no such country code %s" % (country_code))
                success = self.user.add(data)
                if success:
                    return Result.result_success()
                else:
                    return Result.result_failed()
        else:
            return Result.result_parameters_are_invalid()

    def get_user(self):
        if self.username:
            return self.user.get_by_username(self.username)
        else:
            return None

    def does_user_exist(self):
        if self.username:
            user = self.user.get_by_username(self.username)
            if user:
                return True
        return False

    def update_user(self, instance, data):
        return self.user.update(instance, data)

    def add_token(self):
        user = self.get_user()
        if user:
            if self.token.get(user.id):
                return Result.result_success(TOKEN_EXIST)
            else:
                success = self.token.add(user.id)
                if success:
                    return Result.result_success()
                else:
                    return Result.result_failed()
        else:
            return Result.result_failed(USER_NOT_EXIST)

    def get_token(self):
        user = self.get_user()
        if user:
            return self.token.get(user.id)
        else:
            return ""

    def add_user_extension(self, user_id, user_extension_dict):
        if not user_id:
            result = Result.result_parameters_are_invalid()
        else:
            extension = self.user_extension.get_by_user(user_id)
            if extension and user_extension_dict:
                success = self.user_extension.update(extension, user_extension_dict)
                if success:
                    result = Result.result_success(UPDATE_USER_SUCCESS)
                else:
                    result = Result.result_failed(UPDATE_USER_FAILED)
            else:
                user_extension_dict["user_id"] = user_id
                OHHOLog.print_log(user_extension_dict)
                success = self.user_extension.add(user_extension_dict)
                if success:
                    result = Result.result_success()
                else:
                    result = Result.result_failed()

        return result

    def get(self, username):
        return self.user.get_by_username(username)

    def get_by_country_code_and_cellphone(self, country_code_id, cellphone):
        return self.user.get_by_country_code_and_cellphone(country_code_id, cellphone)

    def delete(self, instance):
        return self.user.delete(instance)

    def restore(self, instance):
        return self.user.restore(instance)

    def get_by_id(self, user_id):
        return self.user.get_by_id(user_id)

    def get_by_username(self, username):
        return self.user.get_by_username(username)

    def get_by_cellphone_from_query(self, cellphone):
        query = self.user.get_query()
        return self.user.get_by_cellphone_from_query(query, cellphone)

    def find_by_cellphone(self, cellphone):
        query = self.user.get_query()
        return self.user.find_by_cellphone(query, cellphone)

    def get_by_cellphone(self, cellphone):
        return self.user.get_by_cellphone(cellphone)

    def get_user_extension_by_user(self, user_id):
        return self.user_extension.get_by_user(user_id)

    def get_valid(self, query):
        return self.user.get_valid(query)

    def get_by_country_code(self, query, country_code_id):
        return self.user.get_by_country_code(query, country_code_id)

    def get_invalid(self, query):
        return self.user.get_invalid(query)

    def init_user_extension(self, user_id):
        data = dict()
        data["user_id"] = user_id
        success = self.user_extension.add(data)
        if success:
            return self.get_user_extension_by_user(user_id)
        else:
            return None

    def check_threemonth_isvalid(self, instance):
        if instance:
            timestamp = OHHODatetime.get_current_timestamp()
            if instance.timestamp + VALID_INTERVAL_MILLISECOND_THREE < timestamp:
                return False
            else:
                return True
        else:
            return False

    def check_user_only_by_user(self, username, code, country_code_id):
        if username and code:
            user = self.user.get_by_country_code_and_cellphone(country_code_id, username)
            if user:
                if self.check_threemonth_isvalid(user):
                    country_code_obj = self.country_code.get_by_id(country_code_id)
                    if country_code_obj:
                        cellphone_number = country_code_obj.country_code + username
                        check = Code.check_code(cellphone_number, code)
                        if check:
                            token = self.token.get(user.id)
                            if token:
                                self.user.update(user, dict({"last_login": OHHODatetime.get_utc_now()}))
                                result = Result.result_success(USER_LOGIN)
                            else:
                                token = self.token.add(user.id)
                                if token:
                                    result = Result.result_success()
                                else:
                                    result = Result.result_failed()
                        else:
                            result = Result.result_failed("code is incorrect!")
                    else:
                        result = Result.result_failed("country_code not exist")

                else:
                    # result = Result.result_failed("only login by password")
                    result = Result.result_update_beyond_three_month()
            else:
                result = Result.result_not_exist(USER_NOT_EXIST)
        else:
            result = Result.result_parameters_are_invalid()
        return result

    def check_user(self, username, password, country_code_id):
        if username and password:
            user = self.user.get_by_country_code_and_cellphone(country_code_id, username)
            self.password.set_password(password)
            encryption_password = self.password.encryption()
            if user:
                if user.password == encryption_password:
                    token = self.token.get(user.id)
                    if not token:
                        token = self.token.add(user.id)
                    if token:
                        self.user.update(user, dict({"last_login": OHHODatetime.get_utc_now()}))
                        result = Result.result_success()
                    else:
                        result = Result.result_failed()
                else:
                    result = Result.result_password_is_incorrect()
            else:
                result = Result.result_not_exist(USER_NOT_EXIST)
        else:
            result = Result.result_parameters_are_invalid()
        return result

    def reset_password(self, username, password, country_code):
        if username and password:
            self.password.set_password(password)
            encryption_password = self.password.encryption()
            country_code_obj = self.get_country_code(country_code)
            user = self.user.get_by_country_code_and_cellphone(country_code_obj.id, username)
            if user:
                update_user = self.user.update(user, {"password": encryption_password})
                if update_user:
                    result = Result.result_success()
                else:
                    result = Result.result_failed()
            else:
                result = Result.result_not_exist(USER_NOT_EXIST)
        else:
            result = Result.result_parameters_are_invalid()
        return result

    @staticmethod
    def get_meet_user_information(user_id):
        user = DBOHHOUser.get_by_id(user_id)
        if user:
            data = DBOHHOUser.get_information(user)
        else:
            data = dict()
        return data

    def check_user4backstage(self, username, password, country_code):
        if username and password and country_code:
            country_code_obj = self.country_code.get_by_country_code(country_code)
            country_code_id = country_code_obj.id if country_code_obj else 0
            user = self.user.get_by_country_code_and_cellphone(country_code_id, username)
            self.password.set_password(password)
            encryption_password = self.password.encryption()
            if user:
                if user.password == encryption_password:
                    return True, user.username
                else:
                    return False, user.username
        return False, None

    def get_all(self):
        return self.user.get_query()

    def find_by_username(self, username):
        return self.user.find_by_username(username)

    def get_some_users(self, query, offset, limit):
        return self.user.get_some(query, offset, limit)

    def get_default_nickname(self, instance):
        return instance.nickname if instance.nickname else DEFAULT_NICKNAME

    def get_default_icon(self, instance, base_url=None):
        # OHHOLog.print_log(instance)
        # OHHOLog.print_log(base_url)
        if instance.source_icon and base_url:
            return base_url + instance.icon
        else:
            return base_url + DEFAULT_ICON

    def get_user_basic_information(self, user_id, base_url):
        user = self.get_by_id(user_id)
        result = dict()
        result["user_id"] = user_id
        if user:
            # user_head_sculpture_icon = self.user_icon.get_user_head_sculpture(user_id)
            # if user_head_sculpture_icon:
            #     result["source_icon"] = self.get_default_icon(user_head_sculpture_icon, base_url)

            user_accuracy_extension = self.user_extension.get_by_user(user_id)
            if user_accuracy_extension:
                result["source_icon"] = self.get_default_icon(user_accuracy_extension, base_url)
                result["nickname"] = self.get_default_nickname(user_accuracy_extension)

            device = self.get_primary_device_by_user(user_id)
            if device:
                result["device_identity_id"] = device.identity_id
                result["device_mac_address"] = device.mac_address

            # map = self.map.get_by_user(user_id)
            map_information = self.get_user_map_information_from_redis(user.username)
            # if map_information:
            #     del map_information["id"]
            result = OHHOOperation.dict_add_dict(result, map_information)
        return result

    def get_friend_relation(self, user_id, friend_user_id):

        black = self.friend.get_black_by_user_and_friend(user_id, friend_user_id)
        friend = self.friend.get_friend_by_user_and_friend(user_id, friend_user_id)
        apply = self.friend.get_apply_by_user_and_friend(user_id, friend_user_id)
        apply_reverse = self.friend.get_apply_by_user_and_friend(friend_user_id, user_id)
        relation = FRIEND_RELATION_NO_RELATION
        if friend:
            OHHOLog.print_log(user_id)
            OHHOLog.print_log(friend_user_id)
            OHHOLog.print_log(friend.id)
            relation = FRIEND_RELATION_FRIEND
        elif black:
            relation = FRIEND_RELATION_BLACK
        elif self.friend.is_valid_apply(apply):
            relation = FRIEND_RELATION_MY_VALID_APPLY
        elif self.friend.is_valid_apply(apply_reverse):
            relation = FRIEND_RELATION_MY_VALID_APPLIED
        my_apply_id = apply.id if apply else 0
        my_applied_id = apply_reverse.id if apply_reverse else 0
        return relation, my_apply_id, my_applied_id

    def get_friend_information(self, user_id, friend_user_id, apply_id=0, base_url=None):
        user = self.user.get_by_id(friend_user_id)
        result = dict()
        if user and user.state:
            user_accuracy_extension = self.user_extension.get_by_user(friend_user_id)
            result["user_id"] = friend_user_id
            user_icon = self.user_icon.get_user_head_sculpture(friend_user_id)
            result["icon"] = base_url + user_icon.icon if user_icon else ""
            if user_accuracy_extension:
                # result["icon"] = self.get_default_icon(user_accuracy_extension, base_url)
                result["nickname"] = self.get_default_nickname(user_accuracy_extension)

            # user_icon = self.user_icon.get_user_head_sculpture(friend_user_id)
            # if user_icon:
            #     result["icon"] = self.get_default_icon(user_icon, base_url)

            result["relation"], result["friend_apply_id"], result["friend_reverse_apply_id"] = self.get_friend_relation(
                user_id, friend_user_id)
        return result

    def push_duplex_agree_interest(self, information, user_id, friend_user_id):
        # result = list()
        primary_list = list()
        secondary_list = list()
        condition = self.get_condition(friend_user_id)
        OHHOLog.print_log(friend_user_id)
        if condition:
            OHHOLog.print_log("has condition")
            OHHOLog.print_log(condition.interest)
            primary_interest_list = condition.interest.split(",")

            user_extension = self.user_extension.get_by_user(user_id)
            # if user_extension and user_extension.interest:
            if user_extension:
                interest = user_extension.interest
                interest_dict = OHHOOperation.json2dict(interest)
                for key, value in interest_dict.items():
                    temp_list = list()
                    if key in ("other",):
                        temp_list = value
                    else:
                        for interest_id in value:
                            name = self.get_interest_name_by_id(interest_id)
                            if name:
                                temp_list.append(name)
                    if key in primary_interest_list:
                        primary_list += temp_list
                    else:
                        secondary_list += temp_list
        else:
            OHHOLog.print_log("no condition")
        information["all_interest"] = primary_list + secondary_list

        return information

    def get_age_display(self, birthday):
        OHHOLog.print_log(birthday)
        year = birthday.year
        if year < 1960:
            return "60前"
        elif year < 1965:
            return "60后"
        elif year < 1970:
            return "65后"
        elif year < 1975:
            return "70后"
        elif year < 1980:
            return "75后"
        elif year < 1985:
            return "80后"
        elif year < 1990:
            return "85后"
        elif year < 1995:
            return "90后"
        elif year < 2000:
            return "95后"
        else:
            return "00后"

    def get_height_display(self, height):
        if height < 150:
            return "<150cm"
        elif height < 155:
            return "150cm+"
        elif height < 160:
            return "155cm+"
        elif height < 165:
            return "160cm+"
        elif height < 170:
            return "165cm+"
        elif height < 175:
            return "170cm+"
        elif height < 180:
            return "175cm+"
        elif height < 185:
            return "180cm+"
        elif height < 190:
            return "185cm+"
        elif height < 195:
            return "190cm+"
        else:
            return "195cm+"

    def get_basic_user_information(self, user_id, base_url):
        result = dict()
        user = self.user.get_by_id(user_id)
        if user:
            device = self.get_primary_device_by_user(user_id)
            if device:
                result["device_identity_id"] = device.identity_id
                result["device_mac_address"] = device.mac_address
            else:
                result["device_identity_id"] = ""
                result["device_mac_address"] = ""

            user_extension = self.user_extension.get_by_user(user_id)
            if user_extension:
                if user_extension.sex:
                    result["sex"] = user_extension.sex
                else:
                    result["sex"] = 0

                if user_extension.nickname:
                    result["nickname"] = user_extension.nickname
                else:
                    result["nickname"] = "unknown"

                if user_extension.birthday:
                    result["birthday"] = self.get_age_display(user_extension.birthday)
                else:
                    result["birthday"] = "unknown"

                if user_extension.height:
                    result["height"] = self.get_height_display(user_extension.height)
                else:
                    result["height"] = "unknown"

                if user_extension.occupation_id:
                    occupation = self.interest.get_by_id(user_extension.occupation_id)
                    if occupation:
                        result["occupation"] = occupation.name
                    else:
                        result["occupation"] = "unknown"

                if user_extension.degree_id:
                    degree = self.interest.get_by_id(user_extension.degree_id)
                    if degree:
                        result["degree"] = degree.name
                    else:
                        result["degree"] = "unknown"

            user_icon = self.user_icon.get_user_head_sculpture(user_id)
            if user_icon:
                result["icon"] = base_url + user_icon.thumbnail
            else:
                result["icon"] = ""

            I_am = self.user_description.get_I_am_by_user_id(user_id)
            result["I_am"] = I_am.first + I_am.second + I_am.third

            I_like = self.user_description.get_I_like_by_user_id(user_id)
            result["I_like"] = I_like.first + I_like.second + I_like.third

            I_unlike = self.user_description.get_I_unlike_by_user_id(user_id)
            result["I_unlike"] = I_unlike.first + I_unlike.second + I_unlike.third

            impression_list = self.get_user_impression_by_user_id(user_id)
            result["impression"] = impression_list

        return result
        # result = dict()
        # user = self.user.get_by_id(user_id)
        # if user:
        #     result["username"] = user.username
        #     result["user_id"] = user.id
        #     user_extension = self.user_extension.get_by_user(user_id)
        #     if user_extension:
        #         result["source_icon"] = self.get_default_icon(user_extension, base_url)
        #         result["nickname"] = self.get_default_nickname(user_extension)
        #         # user_icon = self.user_icon.get_user_head_sculpture(user_id)
        #         # if user_icon:
        #         #     result["source_icon"] = self.get_default_icon(user_icon, base_url)
        # return result

    def get_match_user_information(self, user_id, apply_id, base_url):
        try:
            user_id = int(user_id)
            apply_id = int(apply_id)
            result = self.get_basic_user_information(user_id, base_url)
            result["apply_id"] = apply_id
        except Exception as ex:
            OHHOLog.print_log(ex)
            result = dict()
        return result

    def get_duplex_agree_user_information(self, user_id, apply_id, base_url):
        try:
            user_id = int(user_id)
            apply_id = int(apply_id)
            result = self.get_basic_user_information(user_id, base_url)
            device = self.get_primary_device_by_user(user_id)
            # OHHOLog.print_log(user_id)
            # OHHOLog.print_log(device)
            # OHHOLog.print_log(apply_id)
            if device:
                result["device_mac_address"] = device.mac_address
                result["device_identity_id"] = device.identity_id

            apply = self.apply.get_by_id(apply_id)
            if apply:
                # OHHOLog.print_log("get all_interest")
                friend_user_id = apply.one_user_id if apply.another_user_id == int(user_id) else apply.another_user_id
                result = self.push_duplex_agree_interest(result, user_id, friend_user_id)
                # OHHOLog.print_log(result)
            result["apply_id"] = apply_id
        except Exception as ex:
            OHHOLog.print_log(ex)
            result = dict()
        return result

    def get_meeting_user_information(self, user_id, apply_id, base_url):
        try:
            user_id = int(user_id)
            apply_id = int(apply_id)
            result = self.get_basic_user_information(user_id, base_url)
            result["apply_id"] = apply_id
            device = self.get_primary_device_by_user(user_id)
            if device:
                result["device_mac_address"] = device.mac_address
                result["device_identity_id"] = device.identity_id
        except Exception as ex:
            OHHOLog.print_log(ex)
            result = dict()
        OHHOLog.print_log(result)
        return result

    def get_met_user_information(self, user_id, apply_id, base_url):
        try:
            user_id = int(user_id)
            apply_id = int(apply_id)
            result = self.get_basic_user_information(user_id, base_url)
            result["apply_id"] = apply_id
            device = self.get_primary_device_by_user(user_id)
            if device:
                result["device_mac_address"] = device.mac_address
                result["device_identity_id"] = device.identity_id
        except Exception as ex:
            OHHOLog.print_log(ex)
            result = dict()
        return result

    def get_meet_end_user_information(self, user_id, apply_id, base_url):
        result = dict()
        result["apply_id"] = apply_id
        return result

    def get_cancel_meet_user_information(self, user_id, apply_id, base_url):
        try:
            user_id = int(user_id)
            apply_id = int(apply_id)
            result = self.get_basic_user_information(user_id, base_url)
            result["apply_id"] = apply_id
        except Exception as ex:
            OHHOLog.print_log(ex)
            result = dict()
        return result

    def get_refuse_meet_user_information(self, user_id, apply_id, base_url):
        try:
            user_id = int(user_id)
            apply_id = int(apply_id)
            result = self.get_basic_user_information(user_id, base_url)
            result["apply_id"] = apply_id
        except Exception as ex:
            OHHOLog.print_log(ex)
            result = dict()
        return result

    def get_push_user_information(self, user_id, apply_id, base_url):
        result = self.get_user_information(user_id, base_url)
        apply = self.apply.get_by_id(apply_id)
        if apply:
            friend_user_id = apply.one_user_id if apply.another_user_id == int(user_id) else apply.another_user_id
            result = self.push_duplex_agree_interest(result, user_id, friend_user_id)
        result["apply_id"] = apply_id
        result["current_time"] = OHHODatetime.get_now_string()
        del result["interest"]
        del result["created_at"]
        del result["changed_at"]
        del result["timestamp"]
        del result["real_name"]
        del result["identity_card"]
        del result["current_time"]

        OHHOLog.print_log(OHHODatetime.get_now_string())
        return result

    def get_favourite_book_by_user_id(self, user_id, base_url):
        """通过user_id 获取到最喜欢的书籍"""
        favourite_book_list = self.user_favourite_book.get_favourite_book_list_by_user_id(user_id)
        data = list()
        if favourite_book_list:
            for book in favourite_book_list:
                temp_data = self.user_favourite_book.get_information(book, base_url)
                data.append(temp_data)

        return data

    def get_favourite_movie_by_user_id(self, user_id, base_url):
        """通过user_id 获取到最喜欢的电影"""
        favourite_movie_list = self.user_favourite_movie.get_favourite_movie_list_by_user_id(user_id)
        data = list()
        if favourite_movie_list:
            for movie in favourite_movie_list:
                temp_data = self.user_favourite_movie.get_information(movie, base_url)
                data.append(temp_data)

        return data

    def get_favourite_sport_by_user_id(self, user_id, base_url):
        """通过user_id 获取到最喜欢的运动"""
        favourite_sport_list = self.user_favourite_sport.get_favourite_sport_list_by_user_id(user_id)
        data = list()
        if favourite_sport_list:
            for sport in favourite_sport_list:
                temp_data = self.user_favourite_sport.get_information(sport, base_url)
                data.append(temp_data)
        return data

    def get_favourite_music_by_user_id(self, user_id, base_url):
        """通过user_id 获取到最喜欢的音乐"""
        favourite_music_list = self.user_favourite_music.get_favourite_music_list_by_user_id(user_id)
        data = list()
        if favourite_music_list:
            for music in favourite_music_list:
                temp_data = self.user_favourite_music.get_information(music, base_url)
                data.append(temp_data)
        return data

    def get_user_icon_by_user_id(self, user_id, base_url):
        """通过user_id 获取到用户头像"""
        user_icon_list = self.user_icon.get_by_user(user_id)
        data = list()
        if user_icon_list:
            user_icon_list = user_icon_list if len(user_icon_list) <= 4 else user_icon_list[:4]
            for user_ico in user_icon_list:
                temp_data = self.user_icon.get_information(user_ico, base_url)
                data.append(temp_data)

        return data

    def get_description(self, user_id):
        query_i_am = self.user_description.get_I_am_by_user_id(user_id)
        query_i_like = self.user_description.get_I_like_by_user_id(user_id)
        query_i_unlike = self.user_description.get_I_unlike_by_user_id(user_id)
        query_i_hope = self.user_description.get_I_hope_by_user_id(user_id)

        return query_i_am, query_i_like, query_i_unlike, query_i_hope

    def get_user_description_by_user_id(self, user_id, base_url):
        """通过user_id 获取到用户描述"""
        user_description_list = self.user_description.get_user_description_by_user_id(user_id)
        query_i_am, query_i_like, query_i_unlike, query_i_hope = self.get_description(user_id)
        data = dict()
        if user_description_list:
            temp_i_am_data = self.user_description.get_information(query_i_am, base_url)
            temp_i_like_data = self.user_description.get_information(query_i_like, base_url)
            temp_i_unlike_data = self.user_description.get_information(query_i_unlike, base_url)
            temp_i_hope_data = self.user_description.get_information(query_i_hope, base_url)

            data["I_am"] = temp_i_am_data
            data["I_like"] = temp_i_like_data
            data["I_unlike"] = temp_i_unlike_data
            data["I_hope"] = temp_i_hope_data

        return data

    def get_user_impression_by_user_id(self, user_id, base_url=""):
        """通过user_id 获取到用户印象"""
        type = 0
        user_impression_list = self.user_impression.get_user_impression(user_id, type)
        data = list()
        if user_impression_list:
            for impression in user_impression_list:
                temp_data = dict()
                temp_instance = self.user_impression.get_by_id(impression.id)
                temp_data["count"] = impression.count_content
                temp_data["name"] = temp_instance.content.name
                data.append(temp_data)
        return data

    def get_accuracy_extension_by_user_id(self, user_id, base_url):
        """通过user_id 获取到额外的信息"""
        user = self.user.get_by_id(user_id)
        user_extension = self.user_extension.get_by_user_id_only_one(user_id)
        device = self.get_primary_device_by_user(user_id)
        data = dict()
        if user_extension:
            data = self.user_extension.get_information(user_extension, base_url)
            if data:
                if data["height"]:
                    data["height"] = int(data["height"])
            if user_extension.occupation_id:
                data["occupation_name"] = user_extension.occupation.name
            else:
                data["occupation_name"] = ""

            if user_extension.position_id:
                data["position_name"] = user_extension.position.name
            else:
                data["position_name"] = ""
            if user_extension.degree_id:
                data["degree_name"] = user_extension.degree.name
            else:
                data["degree_name"] = ""

            if user_extension.birthday:
                data["zodiac"] = self.get_zodiac(user_extension.birthday)
                data["age"] = self.get_age(user_extension.birthday)
        data["state"] = 0
        data["state"] = user.state
        data["user_id"] = user_id
        country_code_id = user.country_code_id
        if country_code_id:
            country_code_object = self.country_code.get_by_id(country_code_id)
            data["country_code"] = country_code_object.country_code if country_code_object else 0
        else:
            data["country_code"] = "+86"

        token = self.token.get(user_id)
        if token:
            data["token"] = token.token
        else:
            data["token"] = ""
        query = self.im_user.get_query()
        query = self.im_user.get_by_account(query, user_id)
        im_user = self.im_user.first(query)
        if im_user:
            data["im_token"] = im_user.token
        else:
            RefreshToken.create_or_update(user_id)
            query = self.im_user.get_query()
            query = self.im_user.get_by_account(query, user_id)
            im_user = self.im_user.first(query)
            if im_user:
                data["im_token"] = im_user.token
            else:
                data["im_token"] = ""
        if device:
            data["device_identity_id"] = device.identity_id
            data["device_mac_address"] = device.mac_address

            imei = self.imei.get_by_device(device.id)
            if imei:
                data["imei"] = imei.imei

        configuration = self.user_configuration.get_by_user(user_id)
        if configuration:
            data["is_online"] = configuration.is_online
            data["is_match"] = configuration.is_match

        return data

    def get_user_information(self, user_id, base_url=None):
        result = dict()
        if user_id:
            user = self.user.get_by_id(user_id)
            if user and user.state:
                favourite_book_data = self.get_favourite_book_by_user_id(user_id, base_url)
                favourite_movie_data = self.get_favourite_movie_by_user_id(user_id, base_url)
                favourite_sport_data = self.get_favourite_sport_by_user_id(user_id, base_url)
                favourite_music_data = self.get_favourite_music_by_user_id(user_id, base_url)
                user_icon_data = self.get_user_icon_by_user_id(user_id, base_url)
                user_description_data = self.get_user_description_by_user_id(user_id, base_url)
                user_impression_data = self.get_user_impression_by_user_id(user_id, base_url)
                user_accuracy_extension_data = self.get_accuracy_extension_by_user_id(user_id,
                                                                                      base_url)
                result["books"] = favourite_book_data
                result["movies"] = favourite_movie_data
                result["sports"] = favourite_sport_data
                result["musics"] = favourite_music_data
                result["icons"] = user_icon_data
                result["descriptions"] = user_description_data
                result["impression"] = user_impression_data
                result["extension"] = user_accuracy_extension_data

                OHHOLog.print_log("user_personal_information_result")
                OHHOLog.print_log(result)
        return result

    def get_user_information4friend(self, user_id, base_url=None):
        user = self.user.get_by_id(user_id)
        result = dict()
        device = self.get_primary_device_by_user(user_id)
        map = self.map.get_by_user(user_id)

        if user and user.state:
            result["state"] = 0
            user_accuracy_extension = self.user_extension.get_by_user(user_id)
            if user_accuracy_extension:
                result = self.user_extension.get_information(user_accuracy_extension, base_url)
                result["state"] = user.state
                if user_accuracy_extension.birthday:
                    result["zodiac"] = self.get_zodiac(user_accuracy_extension.birthday)
                interest_dict = self.user_extension.parse_interest(user_accuracy_extension)
                # interest_dict = self.parse_interest(interest_dict)

                result = OHHOOperation.dict_add_dict(result, interest_dict)

            match_condition_relation = self.record_user_and_match_condition.get_nearest_by_user(user.id)
            if match_condition_relation and match_condition_relation.match_condition_id:
                match_condition = self.match_condition.get_by_id(match_condition_relation.match_condition_id)
                if match_condition and match_condition.interest:
                    result["primary"] = OHHOOperation.json2dict(match_condition.interest)
                else:
                    result["primary"] = list()
            else:
                result["primary"] = list()

            country_code_id = user.country_code_id
            if country_code_id:
                country_code_object = self.country_code.get_by_id(country_code_id)
                result["country_code"] = country_code_object.country_code if country_code_object else 0
            else:
                result["country_code"] = "+86"

            result["username"] = user.cellphone
            result["unique_username"] = user.username
            token = self.token.get(user_id)
            # OHHOLog.print_log(user_id)
            if token:
                result["token"] = token.token
            else:
                result["token"] = ""
            query = self.im_user.get_query()
            query = self.im_user.get_by_account(query, user_id)
            im_user = self.im_user.first(query)
            if im_user:
                result["im_token"] = im_user.token
            else:
                # OHHOLog.print_log("add im token")
                RefreshToken.create_or_update(user_id)
                query = self.im_user.get_query()
                query = self.im_user.get_by_account(query, user_id)
                im_user = self.im_user.first(query)
                if im_user:
                    result["im_token"] = im_user.token
                else:
                    result["im_token"] = ""

            if device:
                result["device_identity_id"] = device.identity_id
                result["device_mac_address"] = device.mac_address

                imei = self.imei.get_by_device(device.id)
                # imei = self.imei.first(imeis)
                if imei:
                    result["imei"] = imei.imei

            configuration = self.user_configuration.get_by_user(user_id)
            if configuration:
                result["is_online"] = configuration.is_online
                result["is_match"] = configuration.is_match
            if map:
                result["longitude"] = float(map.longitude)
                result["latitude"] = float(map.latitude)
            else:
                result["longitude"] = 0
                result["latitude"] = 0

        user_icon = self.user_icon.get_user_head_sculpture(user_id)
        result["icon"] = base_url + user_icon.thumbnail if user_icon else ""

        return result

    def get_primary_device_by_user(self, user_id):
        query = self.user_and_device_relation.get_query()
        query = self.user_and_device_relation.get_valid(query)
        query = self.user_and_device_relation.get_by_user(query, user_id)
        query = self.user_and_device_relation.get_by_is_lost(query, False)
        query = self.user_and_device_relation.get_by_type(query, 1)
        query = self.user_and_device_relation.order_by_id_desc(query)
        relation = self.user_and_device_relation.first(query)
        if relation:
            return self.device.get_by_id(relation.device_id)
        else:
            return None

    def get_relation_by_user(self, user_id, type=1, is_lost=False):
        query = self.user_and_device_relation.get_query()
        query = self.user_and_device_relation.get_valid(query)
        query = self.user_and_device_relation.get_by_user(query, user_id)
        query = self.user_and_device_relation.get_by_type(query, type)
        query = self.user_and_device_relation.get_by_is_lost(query, is_lost)
        query = self.user_and_device_relation.order_by_id_desc(query)
        return query

    def get_nearest_device_by_user(self, user_id, type=1, is_lost=False):
        query = self.get_relation_by_user(user_id, type, is_lost)
        relation = self.user_and_device_relation.first(query)
        if relation:
            return self.device.get_by_id(relation.device_id)
        else:
            return None

    def push(self, message, to_user_id, from_user_id="ohho"):
        OHHOLog.print_log(to_user_id)
        OHHOLog.print_log(from_user_id)
        OHHOLog.print_log(message)
        OHHOLog.print_log("from user %s to user %d" % (str(from_user_id), int(to_user_id)))
        body = message
        # body["current_time"] = OHHODatetime.get_now_string()
        # body["msg"] = message
        return SendMessage.send_attach_message(from_user_id, to_user_id, OHHOOperation.dict2json(body))

    def push_user_information(self, to_user_id, type, information):
        """
        将一个人A的信息推送给另一人B
        :param to_user_id: 推送给谁（B）
        :param user_id: （A）
        :param type: 推送的类型：1，申请见面；2，同意见面；3.取消见面；4.拒绝见面；5. 见面中；
        11.申请好友；12. 同意好友；13.拒绝好友；14.删除好友
        :return:
        """
        data = dict()
        data["type"] = type
        data["information"] = information
        message = OHHOOperation.dict2json(data)
        OHHOLog.print_log(message)
        return self.push(message, to_user_id)

    def get_condition(self, user_id):
        condition_relation = self.record_user_and_match_condition.get_nearest_by_user(user_id)
        if condition_relation:
            condition = self.match_condition.get_by_id(condition_relation.match_condition_id)
        else:
            condition = None
        return condition

    def add_new_condition(self, user_id):
        relation = self.record_user_and_match_condition.get_nearest_by_user(user_id)
        if relation:
            return relation.match_condition_id
        else:
            timestamp = OHHODatetime.get_current_timestamp()
            string_timestamp = str(timestamp)
            self.match_condition.add({"interest": string_timestamp})
            condition = self.match_condition.get_nearest_by_interest(string_timestamp)
            if condition:
                try:
                    self.record_user_and_match_condition.add({"user_id": user_id, "match_condition_id": condition.id})
                    self.match_condition.update(condition, {"interest": ""})
                    OHHOLog.print_log(condition.id)
                    return condition.id
                except Exception as ex:
                    OHHOLog.print_log(ex)
                    return 0
            OHHOLog.print_log("create condition failed")
            return 0

    def get_zodiac(self, birthday):
        month = birthday.month
        day = birthday.day
        if month == 1:
            if day <= 19:
                return "魔羯座"
            else:
                return "水瓶座"
        elif month == 2:
            if day <= 18:
                return "水瓶座"
            else:
                return "双鱼座"
        elif month == 3:
            if day <= 20:
                return "双鱼座"
            else:
                return "白羊座"
        elif month == 4:
            if day <= 19:
                return "白羊座"
            else:
                return "金牛座"
        elif month == 5:
            if day <= 20:
                return "金牛座"
            else:
                return "双子座"
        elif month == 6:
            if day <= 21:
                return "双子座"
            else:
                return "巨蟹座"
        elif month == 7:
            if day <= 22:
                return "巨蟹座"
            else:
                return "狮子座"
        elif month == 8:
            if day <= 22:
                return "狮子座"
            else:
                return "处女座"
        elif month == 9:
            if day <= 22:
                return "处女座"
            else:
                return "天秤座"
        elif month == 10:
            if day <= 23:
                return "天秤座"
            else:
                return "天蝎座"
        elif month == 11:
            if day <= 22:
                return "天蝎座"
            else:
                return "射手座"
        elif month == 12:
            if day <= 21:
                return "射手座"
            else:
                return "魔羯座"

    def get_interest_name_by_id(self, the_id):
        the_id = int(the_id)
        obj = self.interest.get_by_id(the_id)
        if obj:
            return obj.name
        else:
            return ""

    def parse_interest(self, interest_dict):
        result = dict()
        for key, value in interest_dict.items():
            if key == "other":
                result[key] = value
            else:
                result[key] = list()
                for the_id in value:
                    name = self.get_interest_name_by_id(the_id)
                    if name:
                        result[key].append(name)
        return result

    def set_map_by_is_online(self, information, to_user_id, user_id):
        information["is_online"] = 1
        configuration = self.user_configuration.get_by_user(user_id)
        if configuration:
            if not configuration.is_online:
                # information["longitude"] = 0
                # information["latitude"] = 0
                information["is_online"] = 0
        return information

    def set_map_by_exclude(self, information, to_user_id, user_id):
        information["is_exclude"] = 0
        extension = self.get_user_extension_by_user(user_id)
        exclude = ""
        exclude_list = list()
        if extension:
            exclude = extension.exclude
        if exclude:
            exclude_list = exclude.split(",")
        if exclude_list:
            exclude_list = [int(e) for e in exclude_list]
            if int(to_user_id) in exclude_list:
                # information["longitude"] = 0
                # information["latitude"] = 0
                information["is_exclude"] = 1

        return information

    def get_user_and_friend_relation(self, user_id, friend_id):
        """获取用户和对方朋友关系是不是 朋友关系"""
        query = self.im_user_relation.get_query()
        query = self.im_user_relation.get_by_account(query, user_id)
        query = self.im_user_relation.get_by_friend(query, friend_id)
        return self.im_user_relation.get_all(query)


if __name__ == "__main__":
    pass
