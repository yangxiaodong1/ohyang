from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_log import OHHOLog
from Tools.ohho_operation import OHHOOperation
from ohho.common.db.ohho.base.db_ohho_country_code import DBOHHOCountryCode
from ohho.common.db.ohho.base.db_ohho_interest import DBOHHOInterest


from ohho.common.db.ohho.user.db_ohho_staff import DBOHHOStaff
from ohho.common.db.ohho.user.db_ohho_staff_accuracy_extension import DBOHHOStaffAccuracyExtension
from ohho.common.logic.common.code import Code

from ohho.common.logic.common.password import Password
from ohho.common.logic.common.result import Result
from ohho.common.logic.ohho.detail_constant import *
from ohho.common.logic.common.record.constant import VALID_INTERVAL_MILLISECOND_THREE
from DB.redis.operation import RedisDB
from ohho.common.logic.common.constant import *


DEFAULT_ICON = "static/image/timg.jpg"
DEFAULT_NICKNAME = "xiaobai"

FRIEND_RELATION_NO_RELATION = 0
FRIEND_RELATION_FRIEND = 1
FRIEND_RELATION_BLACK = 2
FRIEND_RELATION_MY_VALID_APPLY = 3
FRIEND_RELATION_MY_VALID_APPLIED = 4


class Staff(object):
    def __init__(self, username=None):
        self.username = username
        self.staff = DBOHHOStaff()
        self.password = Password()
        self.staff_extension = DBOHHOStaffAccuracyExtension()
        self.interest = DBOHHOInterest()
        self.country_code = DBOHHOCountryCode()


    def get_age(self, birthday):
        if birthday:
            now = OHHODatetime.get_now()
            now_year = OHHODatetime.get_year(now)
            birthday_year = OHHODatetime.get_year(birthday)
            return now_year - birthday_year + 1
        else:
            return -1



    def get_staff_id_by_username(self, username):
        staff = self.get_by_username(username)
        if staff:
            return staff.id
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

    def set_staff_password(self, instance, password):
        if instance and password:
            self.password.set_password(password)
            encryption_password = self.password.encryption()
            user_dict = {"password": encryption_password}
            return self.staff.update(instance, user_dict)
        else:
            return False

    def add_staff(self, password, cellphone=None, country_code="+86"):
        username = self.username
        if username and password and country_code:
            self.password.set_password(password)
            encryption_password = self.password.encryption()
            user = self.staff.get_by_username(username)
            country_code_object = self.get_country_code(country_code)
            if country_code_object:
                exist_cellphone = self.get_by_country_code_and_cellphone(country_code_object.id, cellphone)
            else:
                return Result.result_failed("country code is invalid!")
            if user:
                return Result.result_failed("username exists!")
            elif exist_cellphone:
                return Result.result_failed("cellphone exist!")
            else:
                data = dict()
                data["username"] = username
                data["password"] = encryption_password
                data["cellphone"] = cellphone
                data["country_code_id"] = country_code_object.id
                data["last_login"] = OHHODatetime.get_utc_now()

                success = self.staff.add(data)
                if success:
                    return Result.result_success()
                else:
                    return Result.result_failed()
        else:
            return Result.result_parameters_are_invalid()

    def get_user(self):
        if self.username:
            return self.staff.get_by_username(self.username)
        else:
            return None

    def does_user_exist(self):
        if self.username:
            user = self.staff.get_by_username(self.username)
            if user:
                return True
        return False

    def update_staff(self, instance, data):
        return self.staff.update(instance, data)



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
        return self.staff.get_by_country_code_and_cellphone(country_code_id, cellphone)

    def delete(self, instance):
        return self.staff.delete(instance)

    def restore(self, instance):
        return self.staff.restore(instance)

    def get_by_id(self, user_id):
        return self.staff.get_by_id(user_id)

    def get_by_username(self, username):
        return self.staff.get_by_username(username)

    def get_by_cellphone_from_query(self, cellphone):
        query = self.staff.get_query()
        return self.staff.get_by_cellphone_from_query(query, cellphone)

    def find_by_cellphone(self, cellphone):
        query = self.staff.get_query()
        return self.staff.find_by_cellphone(query, cellphone)

    def get_by_cellphone(self, cellphone):
        return self.staff.get_by_cellphone(cellphone)

    def get_user_extension_by_user(self, user_id):
        return self.user_extension.get_by_user(user_id)

    def get_valid(self, query):
        return self.staff.get_valid(query)

    def get_by_country_code(self, query, country_code_id):
        return self.staff.get_by_country_code(query, country_code_id)

    def get_invalid(self, query):
        return self.staff.get_invalid(query)





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

    def get_all(self):
        return self.staff.get_query()

    def find_by_username(self, username):
        return self.staff.find_by_username(username)

    def get_some_staffs(self, query, offset, limit):
        return self.staff.get_some(query, offset, limit)

    def get_default_nickname(self, instance):
        return instance.nickname if instance.nickname else DEFAULT_NICKNAME




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




if __name__ == "__main__":
    pass
