from Tools.ohho_log import OHHOLog
# from ohho.common.logic.common.user import User
from ohho.common.logic.common.user import User

from ohho.common.db.ohho.user.db_ohho_user_description import DBOHHOUserDescription
from ohho.common.db.ohho.user.db_ohho_user_impression import DBOHHOUserImpression
from ohho.common.db.ohho.user.db_ohho_user_accuracy_extension import DBOHHOUserAccuracyExtension


class LogicGetUserAccuracyExtension(object):
    @staticmethod
    def get_user_impression_by_user_id(user_id, base_url=""):
        """通过user_id 获取到用户印象"""
        user_impression_instance = DBOHHOUserImpression()
        user_impression_list = user_impression_instance.get_user_impression(user_id)
        data = list()
        if user_impression_list:
            for impression in user_impression_list:
                temp_data = dict()
                temp_instance = user_impression_instance.get_by_id(impression.id)
                # temp_data["content_id"] = impression.content_id
                temp_data["count"] = impression.count_content
                temp_data["name"] = temp_instance.content.name
                data.append(temp_data)
        return data

    @staticmethod
    def get_description(user_id):
        user_description_instance = DBOHHOUserDescription()
        query_i_am = user_description_instance.get_I_am_by_user_id(user_id)
        query_i_like = user_description_instance.get_I_like_by_user_id(user_id)
        query_i_unlike = user_description_instance.get_I_unlike_by_user_id(user_id)
        query_i_hope = user_description_instance.get_I_hope_by_user_id(user_id)

        return query_i_am, query_i_like, query_i_unlike, query_i_hope

    @staticmethod
    def get_user_description_by_user_id(user_id, base_url):
        """通过user_id 获取到用户描述"""
        user_description_instance = DBOHHOUserDescription()
        user_description_list = user_description_instance.get_user_description_by_user_id(user_id)
        query_i_am, query_i_like, query_i_unlike, query_i_hope = LogicGetUserAccuracyExtension.get_description(user_id)
        data = dict()
        if user_description_list:
            temp_i_am_data = user_description_instance.get_information(query_i_am, base_url)
            temp_i_like_data = user_description_instance.get_information(query_i_like, base_url)
            temp_i_unlike_data = user_description_instance.get_information(query_i_unlike, base_url)
            temp_i_hope_data = user_description_instance.get_information(query_i_hope, base_url)

            data["i_am"] = temp_i_am_data
            data["i_like"] = temp_i_like_data
            data["i_unlike"] = temp_i_unlike_data
            data["i_hope"] = temp_i_hope_data

        return data

    @staticmethod
    def get_accuracy_extension_by_user_id(user_id, base_url):
        """通过user_id 获取到额外的信息"""
        user_accuracy_extension_instance = DBOHHOUserAccuracyExtension()
        user_extension = user_accuracy_extension_instance.get_by_user_id_only_one(user_id)
        data = dict()
        if user_extension:
            # for user_extension in user_accuracy_extension_list:
            data = user_accuracy_extension_instance.get_information(user_extension, base_url)
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

        OHHOLog.print_log("user_accuracy_extension_data")
        OHHOLog.print_log(data)

        return data

    @staticmethod
    def get_personal_page_extension_by_user_id(user_id, base_url):
        """通过user_id 获取到额外的信息(个人主页的信息)"""
        user = User()
        user_accuracy_extension_instance = DBOHHOUserAccuracyExtension()
        user_extension = user_accuracy_extension_instance.get_by_user_id_only_one(user_id)
        data = dict()
        if user_extension:
            data = user_accuracy_extension_instance.get_information(user_extension, base_url)
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
                data["age"] = user.get_age(user_extension.birthday)
                data["zodiac"] = user.get_zodiac(user_extension.birthday)

        OHHOLog.print_log("user_accuracy_extension_data")
        OHHOLog.print_log(data)

        return data


if __name__ == "__main__":
    pass