import os

from Tools.ohho_datetime import OHHODatetime
from ohho.common.logic.common.result import Result
from ohho.common.db.ohho.user.db_ohho_user_accuracy_extension import DBOHHOUserAccuracyExtension
from ohho.common.logic.common.im.netease.update_user_info import UpdateUserInfo


class LogicAddUserExclude(object):
    @staticmethod
    def add_user_exclude(user_id, exclude_user_ids):
        extension = DBOHHOUserAccuracyExtension()
        user = extension.get_by_user(user_id)
        if user:
            success = extension.update(user, {"exclude": exclude_user_ids})
            if success:
                return Result.result_success("update successfully!")
            else:
                return Result.result_failed("update failed!")
        else:
            success = extension.add({"user_id": user_id, "exclude": exclude_user_ids})
            if success:
                return Result.result_success("add successfully!")
            else:
                return Result.result_failed("add failed!")

    @staticmethod
    def add_one_user_exclude(user_id, exclude_user_id):
        extension = DBOHHOUserAccuracyExtension()
        user = extension.get_by_user(user_id)
        if user:
            exclude = user.exclude
            exclude += "," + str(exclude_user_id)
            success = extension.update(user, {"exclude": exclude})
            if success:
                return Result.result_success("update successfully!")
            else:
                return Result.result_failed("update failed!")
        else:
            success = extension.add({"user_id": user_id, "exclude": exclude_user_id})
            if success:
                return Result.result_success("add successfully!")
            else:
                return Result.result_failed("add failed!")

    @staticmethod
    def delete_one_user_exclude(user_id, exclude_user_id):
        extension = DBOHHOUserAccuracyExtension()
        user = extension.get_by_user(user_id)
        if user:
            exclude = user.exclude
            exclude_user_id_list = exclude.split(",")
            exclude_user_id_list = [int(e) for e in exclude_user_id_list]
            if int(exclude_user_id) in exclude_user_id_list:
                exclude_user_id_list.remove(exclude_user_id)
                exclude_string = ",".join(exclude_user_id_list)
                success = extension.update(user, {"exclude": exclude_string})
                if success:
                    return Result.result_success("update successfully!")
                else:
                    return Result.result_failed("update failed!")
            else:
                return Result.result_success("no such user in your exclude!")
        else:
            return Result.result_failed("no such user extension!")
