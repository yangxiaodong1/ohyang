from DB.redis.operation import RedisDB
# from ohho.common.db.ohho.user.db_ohho_user import DBOHHOUser
from ohho.common.db.ohho.user.db_ohho_staff import DBOHHOStaff
from ohho.common.db.ohho.user.db_ohho_staff_token import DBOHHOStaffToken
from ohho.common.view.common.parameters import Post, Headers, Get
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.permission.permission import OHHOPermission
from ohho.common.logic.common.token import Token
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog
from Tools.ohho_datetime import OHHODatetime
from functools import wraps


def statistic(func):
    @wraps(func)
    def _statistic(self):
        result = func(self)
        name = "statistic"
        key = self.__class__.__name__ + "_" + func.__name__
        count = RedisDB.hash_get(name, key)
        if not count:
            count = 0
        else:
            count = int(count)
        count += 1
        RedisDB.hash_set(name, key, count)
        return result

    return _statistic


def backstage_authenticate(func):
    @wraps(func)
    def _backstage_authenticate(self):
        OHHOLog.print_log("backstage authentication start")
        if self.current_user:
            OHHOLog.print_log("backstage authentication current user:" + str(self.current_user))
            user_instance = DBOHHOStaff()
            user = user_instance.get_by_username(self.current_user)
            token_instance = DBOHHOStaffToken()
            if user:
                OHHOLog.print_log("backstage authentication user")
                user_id = user.id
                token_from_db = token_instance.get_by_user_id(user_id)
                if token_from_db:
                    current_timestamp = OHHODatetime.get_current_timestamp()
                    if token_from_db.timestamp and current_timestamp - token_from_db.timestamp > 20 * 60 * 1000:
                        OHHOLog.print_log("backstage authentication timeout")
                        OHHOLog.print_log(current_timestamp)
                        OHHOLog.print_log(token_from_db.timestamp)
                        token_instance.delete(token_from_db)
                        self.clear_cookie("username")
                        return self.redirect("/backstage/login/")
                    else:
                        OHHOLog.print_log("backstage authentication success")
                        token_instance.update(token_from_db, dict())
                        result = func(self)
                else:
                    self.clear_cookie("username")
                    return self.redirect("/backstage/login/")
            else:
                self.clear_cookie("username")
                return self.redirect("/backstage/login/")
        else:
            OHHOLog.print_log("backstage authentication no username")
            return self.redirect("/backstage/login/")
        return result

    return _backstage_authenticate
    # return self.write(OHHOOperation.dict2json(Result.result_not_login()))
    # elif method == "GET":
    #     the_get = Get()
    #     the_header = Headers()
    #     user_id = the_get.get_user_id(self)
    #     user_id = user_id if user_id else the_header.get_user_id(self)
    #     token = the_get.get_token(self)
    #     token = token if token else the_header.get_token(self)
    #
    #     token_from_db = token_instance.get(user_id)
    #
    #     if token_from_db and token_from_db.token == token:
    #         result = func(self)
    #     else:
    #         return self.write(OHHOOperation.dict2json(Result.result_not_login()))
    # else:
    #     result = func(self)


def authenticate(func):
    @wraps(func)
    def _authenticate(self):
        method = self.request.method
        token_instance = Token()
        if method == "POST":
            the_post = Post()
            the_header = Headers()
            user_id = the_post.get_user_id(self)
            user_id = user_id if user_id else the_header.get_user_id(self)
            token = the_post.get_token(self)
            token = token if token else the_header.get_token(self)

            token_from_db = token_instance.get(user_id)
            if token_from_db and token_from_db.token == token:
                result = func(self)
            else:
                return self.write(OHHOOperation.dict2json(Result.result_not_login()))
        elif method == "GET":
            the_get = Get()
            the_header = Headers()
            user_id = the_get.get_user_id(self)
            user_id = user_id if user_id else the_header.get_user_id(self)
            token = the_get.get_token(self)
            token = token if token else the_header.get_token(self)

            token_from_db = token_instance.get(user_id)

            if token_from_db and token_from_db.token == token:
                result = func(self)
            else:
                return self.write(OHHOOperation.dict2json(Result.result_not_login()))
        else:
            result = func(self)
        return result

    return _authenticate


def execute_time(func):
    def _execute_time(self):
        start_time = OHHODatetime.get_current_timestamp()
        result = func(self)
        end_time = OHHODatetime.get_current_timestamp()
        OHHOLog.print_log(end_time)
        OHHOLog.print_log(start_time)
        OHHOLog.print_log(end_time - start_time)
        return result

    return _execute_time


def permission(func):
    def _permission(self):
        username = self.current_user
        if not username:
            return self.write(OHHOOperation.dict2json(Result.result_not_login()))
        else:
            class_name = self.__class__.__name__
            if class_name.endswith("AddHandler"):
                the_type = "AddHandler"
            elif class_name.endswith("ListHandler"):
                the_type = "ListHandler"
            elif class_name.endswith("DetailHandler"):
                the_type = "DetailHandler"
            elif class_name.endswith("DeleteHandler"):
                the_type = "DeleteHandler"
            else:
                the_type = ""

            if the_type:
                the_type_length = len(the_type)
                name = class_name[:-the_type_length]
                permission_instance = OHHOPermission()
                page = permission_instance.get_or_create_page_from_permission(name)

                flag = True
                permission = permission_instance.get_the_page_permission_from_permission(username, page)
                OHHOLog.print_log(username)
                OHHOLog.print_log(page.id)
                OHHOLog.print_log(permission)
                print(permission)
                if the_type == "AddHandler":
                    if permission["insert"]:
                        pass
                    else:
                        flag = False
                elif the_type == "ListHandler":
                    if permission["select"]:
                        pass
                    else:
                        flag = False
                elif the_type == "DetailHandler":
                    if permission["update"]:
                        pass
                    else:
                        flag = False
                elif the_type == "DeleteHandler":
                    if permission["delete"]:
                        pass
                    else:
                        flag = False
                else:
                    flag = False
                if not flag:
                    result = Result.result_no_permission()
                    return self.redirect(
                        "/backstage/no/permission/?code=" + str(result.get("code", 0)) + "&data=" + str(
                            result.get("detail", "")))
                result = func(self)
                return result

    return _permission
