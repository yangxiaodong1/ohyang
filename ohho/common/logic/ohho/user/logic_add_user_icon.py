import os

from Tools.ohho_datetime import OHHODatetime
from ohho.common.logic.common.result import Result
from ohho.common.db.ohho.user.db_ohho_user_icon import DBOHHOUserIcon
from ohho.common.logic.common.im.netease.update_user_info import UpdateUserInfo


class LogicAddUserIcon(object):
    @staticmethod
    def add_user_icon(user_id, image_file, base_url, image_sequence):
        image_sequence = int(image_sequence)
        now = OHHODatetime.get_now()
        path = "static/user/icon/%d/%d/%d/" % (now.year, now.month, now.day)
        os.makedirs(path, exist_ok=True)
        if image_file:
            img = image_file[0]
            timestamp = OHHODatetime.get_current_timestamp()
            name = str(user_id) + "_" + str(timestamp) + ".png"
            path_name = path + name
            with open(path_name, 'wb') as f:
                f.write(img["body"])
            result = Result.result_success()
            instance = DBOHHOUserIcon()
            user_icon = instance.get_by_user(user_id)
            if user_icon:
                if image_sequence == 0:
                    instance.update(user_icon, {"first": path_name})
                elif image_sequence == 1:
                    instance.update(user_icon, {"second": path_name})
                elif image_sequence == 2:
                    instance.update(user_icon, {"third": path_name})
                else:
                    instance.update(user_icon, {"fourth": path_name})
            else:
                if image_sequence == 0:
                    instance.add({"first": path_name, "user_id": user_id})
                elif image_sequence == 1:
                    instance.add({"second": path_name, "user_id": user_id})
                elif image_sequence == 2:
                    instance.add({"third": path_name, "user_id": user_id})
                else:
                    instance.add({"fourth": path_name, "user_id": user_id})

            result["url"] = base_url + path_name

            UpdateUserInfo.update_user_info(user_id, icon=base_url + path_name)
        else:
            result = Result.result_failed("no image file")
            result["url"] = ""
        return result

    @staticmethod
    def get_user_icon_by_user_id(user_id, base_url):
        """通过user_id 获取到用户头像"""
        user_icon_instance = DBOHHOUserIcon()
        user_icon_list = user_icon_instance.get_by_user(user_id)
        data = list()
        if user_icon_list:
            user_icon_list = user_icon_list if len(user_icon_list) <= 4 else user_icon_list[:4]
            for user_ico in user_icon_list:
                temp_data = user_icon_instance.get_information(user_ico, base_url)
                data.append(temp_data)

        return data
