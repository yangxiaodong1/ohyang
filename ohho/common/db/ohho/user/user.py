from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.db.ohho.user.db_ohho_user_accuracy_extension import DBOHHOUserAccuracyExtension
from ohho.common.db.ohho.user.db_ohho_user_description import DBOHHOUserDescription
from ohho.common.db.ohho.user.db_ohho_user_favourite_book import DBOHHOUserFavouriteBook
from ohho.common.db.ohho.user.db_ohho_user_favourite_movie import DBOHHOUserFavouriteMovie
from ohho.common.db.ohho.user.db_ohho_user_favourite_music import DBOHHOUserFavouriteMusic
from ohho.common.db.ohho.user.db_ohho_user_favourite_sport import DBOHHOUserFavouriteSport
from ohho.common.db.ohho.user.db_ohho_user_icon import DBOHHOUserIcon
from ohho.common.db.ohho.user.db_ohho_user_impression import DBOHHOUserImpression
from DB.common.operation import Operation
from Tools.ohho_log import OHHOLog


class User(object):
    def __init__(self, index=0):
        self.user = DBOHHOUser(index)
        self.user_accuracy_extension = DBOHHOUserAccuracyExtension(index)
        self.user_description = DBOHHOUserDescription(index)
        self.user_favourite_book = DBOHHOUserFavouriteBook(index)
        self.user_favourite_movie = DBOHHOUserFavouriteMovie(index)
        self.user_favourite_music = DBOHHOUserFavouriteMusic(index)
        self.user_favourite_sport = DBOHHOUserFavouriteSport(index)
        self.user_icon = DBOHHOUserIcon(index)
        self.user_impression = DBOHHOUserImpression(index)

    def add_some(self, instance, data):
        if instance and data:
            instance.add_without_commit(data)

    def add_extension(self, data):
        self.add_some(self.user_accuracy_extension, data)

    def add_description(self, data):
        self.add_some(self.user_description, data)

    def add_book(self, data):
        self.add_some(self.user_favourite_book, data)

    def add_movie(self, data):
        self.add_some(self.user_favourite_movie, data)

    def add_music(self, data):
        self.add_some(self.user_favourite_music, data)

    def add_sport(self, data):
        self.add_some(self.user_favourite_sport, data)

    def add_icon(self, data):
        self.add_some(self.user_icon, data)

    def add_impression(self, data):
        self.add_some(self.user_impression, data)

    def add_basic(self, user_id, extension,
                  description_I_am,
                  description_I_like,
                  description_I_unlike,
                  description_I_hope):
        try:
            user_extension = self.user_accuracy_extension.get_by_user(user_id)
            if user_extension:
                self.user_accuracy_extension.update_without_commit(user_extension, extension)
            else:
                self.add_extension(extension)

            query = self.user_description.get_query()
            user_description = self.user_description.get_by_user(query, user_id)

            if description_I_am:
                I_am = self.user_description.get_I_am(user_description)
                I_am = self.user_description.order_by_id_desc(I_am)
                I_am = self.user_description.first(I_am)
                if I_am:
                    self.user_description.update_without_commit(I_am, description_I_am)
                else:
                    self.user_description.add_I_am(description_I_am)

            if description_I_like:
                I_like = self.user_description.get_I_like(query)
                I_like = self.user_description.order_by_id_desc(I_like)
                I_like = self.user_description.first(I_like)
                if I_like:
                    self.user_description.update_without_commit(I_like, description_I_like)
                else:
                    self.user_description.add_I_like(description_I_like)

            if description_I_unlike:
                I_unlike = self.user_description.get_I_unlike(query)
                I_unlike = self.user_description.order_by_id_desc(I_unlike)
                I_unlike = self.user_description.first(I_unlike)
                if I_unlike:
                    self.user_description.update_without_commit(I_unlike, description_I_unlike)
                else:
                    self.user_description.add_I_unlike(description_I_unlike)

            if description_I_hope:
                I_hope = self.user_description.get_I_hope(query)
                I_hope = self.user_description.order_by_id_desc(I_hope)
                I_hope = self.user_description.first(I_hope)
                if I_hope:
                    self.user_description.update_without_commit(I_hope, description_I_hope)
                else:
                    self.user_description.add_I_hope_she_is(description_I_hope)

            return Operation.commit()
        except Exception as ex:
            OHHOLog.print_log(ex)
            return False

            # def add(self,
            #         extension=dict(),
            #         description=dict(),
            #         book=dict(),
            #         movie=dict(),
            #         music=dict(),
            #         sport=dict(),
            #         icon=dict(),
            #         impression=dict()):
            #     try:
            #         if extension:
            #             self.add_extension(extension)
            #         if description:
            #             self.add_description(description)
            #         if book:
            #             self.add_book(book)
            #         if movie:
            #             self.add_movie(movie)
            #         if music:
            #             self.add_music(music)
            #         if sport:
            #             self.add_sport(sport)
            #         if icon:
            #             self.add_icon(icon)
            #         if impression:
            #             self.add_impression(impression)
            #         return Operation.commit()
            #     except Exception as ex:
            #         OHHOLog.print_log(ex)
            #         Operation.rollback()
            #         return False


if __name__ == "__main__":
    pass
