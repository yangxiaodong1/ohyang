from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
from ohho.common.db.ohho.user.db_ohho_user_impression import DBOHHOUserImpression
from ohho.common.db.ohho.user.db_ohho_user_accuracy_extension import DBOHHOUserAccuracyExtension
from ohho.common.logic.common.user import User


class EncounterStrategy(object):
    def __init__(self, user_id):
        self.user_id = user_id
        self.user = User()
        self.map = DBOHHOMapInformation()
        self.impression = DBOHHOUserImpression()
        self.extension = DBOHHOUserAccuracyExtension()

    def get_impression(self):
        return self.impression.get_user_impression_list_by_user_id(self.user_id)

    def get_sex(self):
        extension = self.extension.get_by_user(self.user_id)
        if extension and extension.sex:
            return '男孩纸' if extension.sex == 1 else '女孩纸'
        return "X孩纸"

    def get_age(self):
        extension = self.extension.get_by_user(self.user_id)
        if extension and extension.birthday:
            return self.user.get_age_display(extension.birthday)
        return "XX后"

    def get_occupation(self):
        extension = self.extension.get_by_user(self.user_id)
        if extension and extension.occupation:
            return extension.occupation.name
        return "XX"

    def get_position(self):
        extension = self.extension.get_by_user(self.user_id)
        if extension and extension.position:
            return extension.position.name
        return "XX"

    def get_character(self):
        pass

    def get_favourite(self):
        pass

    def get_near_pois(self, longitude, latitude):
        pass

    def get_default(self):
        pass

    def get_end_words(self):
        pass
