import os

from ohho.common.logic.common.result import Result
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.db.ohho.user.db_ohho_user_favourite_sport import DBOHHOUserFavouriteSport


class LogicAddUserFavouriteSport(object):
    @staticmethod
    def add_sport(data):
        user_id = data.get("user_id", "")
        sport_id = data.get("sport_id", "")
        user_instance = DBOHHOUser()
        sport_instance = DBOHHOUserFavouriteSport()
        if user_id and sport_id:
            user = user_instance.get_by_id(user_id)
            if user:
                success = sport_instance.add(data)
                if success:
                    result = Result.result_success()
                else:
                    result = Result.result_failed("add failure")
            else:
                result = Result.result_failed("user not exist")
        else:
            result = Result.result_parameters_are_invalid()

        return result

    @staticmethod
    def get_favourite_sport_by_user_id(user_id, base_url):
        """通过user_id 获取到最喜欢的运动"""
        sport_instance = DBOHHOUserFavouriteSport()
        favourite_sport_list = sport_instance.get_favourite_sport_list_by_user_id(user_id)
        data = list()
        if favourite_sport_list:
            for sport in favourite_sport_list:
                temp_data = sport_instance.get_information(sport, base_url)
                data.append(temp_data)
        return data
