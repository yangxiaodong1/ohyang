import os

from ohho.common.logic.common.result import Result
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.db.ohho.user.db_ohho_user_favourite_movie import DBOHHOUserFavouriteMovie


class LogicAddUserFavouriteMovie(object):
    @staticmethod
    def add_movie(data):
        user_id = data.get("user_id", "")
        movie_id = data.get("movie_id", "")
        user_instance = DBOHHOUser()
        movie_instance = DBOHHOUserFavouriteMovie()
        if user_id and movie_id:
            user = user_instance.get_by_id(user_id)
            if user:
                success = movie_instance.add(data)
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
    def get_favourite_movie_by_user_id(user_id, base_url):
        """通过user_id 获取到最喜欢的电影"""
        movie_instance = DBOHHOUserFavouriteMovie()
        favourite_movie_list = movie_instance.get_favourite_movie_list_by_user_id(user_id)
        data = list()
        if favourite_movie_list:
            for movie in favourite_movie_list:
                temp_data = movie_instance.get_information(movie, base_url)
                data.append(temp_data)

        return data
