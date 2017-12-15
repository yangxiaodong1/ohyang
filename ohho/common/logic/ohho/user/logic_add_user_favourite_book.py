import os

from ohho.common.logic.common.result import Result
from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.db.ohho.user.db_ohho_user_favourite_book import DBOHHOUserFavouriteBook


# from DB.common.operation import


class LogicAddUserFavouriteBook(object):
    @staticmethod
    def add_book(data):
        user_id = data.get("user_id", "")
        isbn = data.get("isbn", "")  # 国际图书编码
        user_instance = DBOHHOUser()
        book_instance = DBOHHOUserFavouriteBook()
        if user_id and isbn:
            user = user_instance.get_by_id(user_id)
            if user:
                success = book_instance.add(data)
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
    def get_favourite_book_by_user_id(user_id, base_url):
        """通过user_id 获取到最喜欢的书籍"""
        book_instance = DBOHHOUserFavouriteBook()
        favourite_book_list = book_instance.get_favourite_book_list_by_user_id(user_id)
        data = list()
        if favourite_book_list:
            for book in favourite_book_list:
                temp_data = book_instance.get_information(book, base_url)
                data.append(temp_data)

        return data
