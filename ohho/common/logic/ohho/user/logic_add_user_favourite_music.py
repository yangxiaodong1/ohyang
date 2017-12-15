import os
from ohho.common.logic.common.result import Result
from ohho.common.db.ohho.user.db_ohho_user_favourite_music import DBOHHOUserFavouriteMusic
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser


class LogicAddUserFavouriteMusic(object):
    @staticmethod
    def add_music(data):
        user_id = data.get("user_id", "")
        music_id = data.get("music_id", "")
        user_instance = DBOHHOUser()
        music_instance = DBOHHOUserFavouriteMusic()
        if user_id and music_id:
            user = user_instance.get_by_id(user_id)
            if user:
                success = music_instance.add(data)
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
    def get_favourite_music_by_user_id(user_id, base_url):
        """通过user_id 获取到最喜欢的音乐"""
        music_instance = DBOHHOUserFavouriteMusic()
        favourite_music_list = music_instance.get_favourite_music_list_by_user_id(user_id)
        data = list()
        if favourite_music_list:
            for music in favourite_music_list:
                temp_data = music_instance.get_information(music, base_url)
                data.append(temp_data)

        return data
