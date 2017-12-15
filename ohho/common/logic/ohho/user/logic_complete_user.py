import os
from PIL import Image
from Tools.ohho_log import OHHOLog
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_datetime import OHHODatetime
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.sensitive import Sensitive
from ohho.common.db.ohho.user.user import User
from ohho.common.logic.ohho.constant import DESCRIPTION_TYPE_I_AM
from ohho.common.logic.ohho.constant import DESCRIPTION_TYPE_I_LIKE
from ohho.common.logic.ohho.constant import DESCRIPTION_TYPE_I_UNLIKE
from ohho.common.logic.ohho.constant import DESCRIPTION_TYPE_I_HOPE


class LogicCompleteUser(object):
    def __init__(self):
        self.user = User()
        self.sensitive = Sensitive()

    def has_sensitive(self, content):
        result = dict()
        has_sensitive = self.sensitive.has_sensitive(content)
        if has_sensitive:
            content_dict = OHHOOperation.json2dict(content)

            extension = content_dict.get("extension", dict())
            if extension:
                result["school"] = self.sensitive.has_sensitive(extension.get("school", ""))
                result["company"] = self.sensitive.has_sensitive(extension.get("company", ""))
                result["nickname"] = self.sensitive.has_sensitive(extension.get("nickname", ""))
                result["favourite_live_city"] = self.sensitive.has_sensitive(extension.get("favourite_live_city", ""))
            else:
                result["school"] = False
                result["company"] = False
                result["nickname"] = False
                result["favourite_live_city"] = False

            I_am = content_dict.get("I_am", dict())
            if I_am:
                result["I_am_first"] = self.sensitive.has_sensitive(I_am.get("first", ""))
                result["I_am_second"] = self.sensitive.has_sensitive(I_am.get("second", ""))
                result["I_am_third"] = self.sensitive.has_sensitive(I_am.get("third", ""))
            else:
                result["I_am_first"] = False
                result["I_am_second"] = False
                result["I_am_third"] = False

            I_like = content_dict.get("I_like", dict())
            if I_like:
                result["I_like_first"] = self.sensitive.has_sensitive(I_like.get("first", ""))
                result["I_like_second"] = self.sensitive.has_sensitive(I_like.get("second", ""))
                result["I_like_third"] = self.sensitive.has_sensitive(I_like.get("third", ""))
            else:
                result["I_like_first"] = False
                result["I_like_second"] = False
                result["I_like_third"] = False

            I_unlike = content_dict.get("I_unlike", dict())
            if I_am:
                result["I_unlike_first"] = self.sensitive.has_sensitive(I_unlike.get("first", ""))
                result["I_unlike_second"] = self.sensitive.has_sensitive(I_unlike.get("second", ""))
                result["I_unlike_third"] = self.sensitive.has_sensitive(I_unlike.get("third", ""))
            else:
                result["I_unlike_first"] = False
                result["I_unlike_second"] = False
                result["I_unlike_third"] = False

            I_hope = content_dict.get("I_hope", dict())
            if I_hope:
                result["I_hope_first"] = self.sensitive.has_sensitive(I_hope.get("first", ""))
                result["I_hope_second"] = self.sensitive.has_sensitive(I_hope.get("second", ""))
                result["I_hope_third"] = self.sensitive.has_sensitive(I_hope.get("third", ""))
            else:
                result["I_hope_first"] = False
                result["I_hope_second"] = False
                result["I_hope_third"] = False
        else:
            return result

    def complete(self, user_id, data, icon0, icon1, icon2, icon3, base_url):
        extension, description, favourite, icons = self.parse_parameter(data)
        try:
            if icons:
                self.add_icon(user_id, icons["icon0_id"], icon0, icons["icon0_is_head_sculpture"], base_url)
                self.add_icon(user_id, icons["icon1_id"], icon1, icons["icon1_is_head_sculpture"], base_url)
                self.add_icon(user_id, icons["icon2_id"], icon2, icons["icon2_is_head_sculpture"], base_url)
                self.add_icon(user_id, icons["icon3_id"], icon3, icons["icon3_is_head_sculpture"], base_url)

            if extension:
                extension["user_id"] = user_id
                user_extension = self.user.user_accuracy_extension.get_by_user(user_id)
                if not user_extension:
                    self.user.user_accuracy_extension.add_without_commit(extension)
                else:
                    self.user.user_accuracy_extension.update_without_commit(user_extension, extension)

            if description:
                I_am = description["I_am"]
                self.add_description(I_am, user_id, DESCRIPTION_TYPE_I_AM)

                I_like = description["I_like"]
                self.add_description(I_like, user_id, DESCRIPTION_TYPE_I_LIKE)

                I_unlike = description["I_unlike"]
                self.add_description(I_unlike, user_id, DESCRIPTION_TYPE_I_UNLIKE)

                I_hope = description["I_hope"]
                self.add_description(I_hope, user_id, DESCRIPTION_TYPE_I_HOPE)

            if favourite:
                books = favourite['books']
                if books:
                    self.delete_favourite(user_id, self.user.user_favourite_book)
                    self.add_favourite(books, self.user.user_favourite_book, user_id)

                movies = favourite['movies']
                if movies:
                    self.delete_favourite(user_id, self.user.user_favourite_movie)
                    self.add_favourite(movies, self.user.user_favourite_movie, user_id)

                musics = favourite['musics']
                if musics:
                    self.delete_favourite(user_id, self.user.user_favourite_music)
                    self.add_favourite(musics, self.user.user_favourite_music, user_id)

                sports = favourite["sports"]
                if sports:
                    self.delete_favourite(user_id, self.user.user_favourite_sport)
                    self.add_favourite(sports, self.user.user_favourite_sport, user_id)
            self.user.user.commit()

            user_extension = self.user.user_accuracy_extension.get_by_user(user_id)
            if user_extension:
                if self.is_primary_OK(user_id):
                    self.user.user_accuracy_extension.update(user_extension, {"able2match": 1})
                else:
                    self.user.user_accuracy_extension.update(user_extension, {"able2match": 0})

            return Result.result_success()
        except Exception as ex:
            OHHOLog.print_log(ex)
            self.user.user.rollback()
            return Result.result_failed("rollback!")

    def add_description(self, obj, user_id, type):
        if obj:
            the_id = obj.get("id", 0)
            del obj["id"]
            obj["user_id"] = user_id
            obj["type"] = type
            if the_id:
                the_object = self.user.user_description.get_by_id(the_id)
                if the_object:
                    self.user.user_description.update_without_commit(the_object, obj)
                else:
                    self.user.user_description.add_without_commit(obj)
            else:
                self.user.user_description.add_without_commit(obj)

    def delete_favourite(self, user_id, instance):
        query = instance.get_query()
        query = instance.get_by_user(query, user_id)
        instance.delete_some_without_commit(query)

    def add_favourite(self, objs, instance, user_id):
        if objs:
            for obj in objs:
                id = obj.get("id", 0)
                del obj["id"]
                obj["user_id"] = user_id
                the_object = instance.get_by_id(id)
                if the_object:
                    index = obj.get("index", 0)
                    if index >= 0:
                        instance.update_without_commit(the_object, obj)
                    else:
                        instance.delete_without_commit(the_object)
                else:
                    instance.add_without_commit(obj)

    def parse_parameter(self, data):
        the_icons = dict()
        data_dict = OHHOOperation.json2dict(data)
        extension = data_dict.get("extension", dict())
        description_I_am = data_dict.get("I_am", dict())
        description_I_like = data_dict.get("I_like", dict())
        description_I_unlike = data_dict.get("I_unlike", dict())
        description_I_hope = data_dict.get("I_hope", dict())

        description = dict()
        description["I_am"] = description_I_am
        description["I_like"] = description_I_like
        description["I_unlike"] = description_I_unlike
        description["I_hope"] = description_I_hope

        favourite_books = data_dict.get("books", list())
        favourite_movies = data_dict.get("movies", list())
        favourite_musics = data_dict.get("musics", list())
        favourite_sports = data_dict.get("sports", list())

        favourite = dict()
        favourite["books"] = favourite_books
        favourite["movies"] = favourite_movies
        favourite["musics"] = favourite_musics
        favourite["sports"] = favourite_sports

        icons = data_dict.get("icons", dict())
        if icons:
            icon0 = icons.get("icon0", dict())
            if icon0:
                icon0_id = icon0.get("id", 0)
                icon0_is_head_sculpture = icon0.get("is_head_sculpture", 0)
            else:
                icon0_id = 0
                icon0_is_head_sculpture = 0

            icon1 = icons.get("icon1", dict())
            if icon1:
                icon1_id = icon0.get("id", 0)
                icon1_is_head_sculpture = icon1.get("is_head_sculpture", 0)
            else:
                icon1_id = 0
                icon1_is_head_sculpture = 0

            icon2 = icons.get("icon2", dict())
            if icon2:
                icon2_id = icon0.get("id", 0)
                icon2_is_head_sculpture = icon2.get("is_head_sculpture", 0)
            else:
                icon2_id = 0
                icon2_is_head_sculpture = 0

            icon3 = icons.get("icon3", dict())
            if icon3:
                icon3_id = icon3.get("id", 0)
                icon3_is_head_sculpture = icon3.get("is_head_sculpture", 0)
            else:
                icon3_id = 0
                icon3_is_head_sculpture = 0

            the_icons["icon0_id"] = icon0_id
            the_icons["icon0_is_head_sculpture"] = icon0_is_head_sculpture
            the_icons["icon1_id"] = icon1_id
            the_icons["icon1_is_head_sculpture"] = icon1_is_head_sculpture
            the_icons["icon2_id"] = icon2_id
            the_icons["icon2_is_head_sculpture"] = icon2_is_head_sculpture
            the_icons["icon3_id"] = icon3_id
            the_icons["icon3_is_head_sculpture"] = icon3_is_head_sculpture
        OHHOLog.print_log(the_icons)
        return extension, description, favourite, the_icons

    def compress_icon(self, file_in, file_out, type="png", width=200):
        img = Image.open(file_in)
        (x, y) = img.size
        height = y * width // x
        out = img.resize((width, height), Image.ANTIALIAS)  # resize image with high-quality
        out.save(file_out, type)

    def add_icon(self, user_id, icon_id, icon, is_head_sculpture, base_url):
        # result = Result.result_failed("default failed")
        # OHHOLog.print_log(icon)
        if icon:
            now = OHHODatetime.get_now()
            path = "static/user/icon/%d/%d/%d/" % (now.year, now.month, now.day)
            os.makedirs(path, exist_ok=True)
            img = icon[0]
            timestamp = OHHODatetime.get_current_timestamp()
            name = str(user_id) + "_" + str(timestamp) + ".png"
            thumbnail_name = str(user_id) + "_" + str(timestamp) + "_thumbnail.png"
            path_name = path + name
            thumbnail_path_name = path + thumbnail_name
            with open(path_name, 'wb') as f:
                f.write(img["body"])
            self.compress_icon(path_name, thumbnail_path_name)

            icon_object = self.user.user_icon.get_by_id(icon_id)
            data = dict()
            data["icon"] = path_name
            data["thumbnail"] = thumbnail_path_name
            data["is_head_sculpture"] = is_head_sculpture

            if icon_object:
                self.user.user_icon.update_without_commit(icon_object, data)
            else:
                data["user_id"] = user_id
                self.user.user_icon.add_without_commit(data)

            result = Result.result_success()
            result["url"] = base_url + path_name
            result["thumbnail_url"] = base_url + thumbnail_path_name
        else:
            result = Result.result_failed("no image file")
            result["url"] = ""
            icon_object = self.user.user_icon.get_by_id(icon_id)
            if icon_object:
                data = dict()
                data["icon"] = ""
                data["thumbnail"] = ""
                data["is_head_sculpture"] = 0
                self.user.user_icon.update_without_commit(icon_object, data)
        OHHOLog.print_log(result)

    def is_primary_OK(self, user_id):
        user = self.user.user.get_by_id(user_id)
        if not (user and user.cellphone and user.country_code_id):
            return False

        extension = self.user.user_accuracy_extension.get_by_user(user_id)
        if not (extension and extension.nickname and extension.sex \
                        and extension.birthday and extension.hometown and extension.height \
                        and extension.occupation_id and extension.position_id and extension.degree_id):
            return False

        description = self.user.user_description.get_user_description_by_user_id(user_id)
        I_am = self.user.user_description.first(self.user.user_description.get_I_am(description))
        I_like = self.user.user_description.first(self.user.user_description.get_I_like(description))
        I_unlike = self.user.user_description.first(self.user.user_description.get_I_unlike(description))
        if not (self.user.user_description.exist_description(I_am) \
                        and self.user.user_description.exist_description(I_like) \
                        and self.user.user_description.exist_description(I_unlike)):
            return False
        return True
