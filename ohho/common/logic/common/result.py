from ohho.common.logic.ohho.detail_constant import *


class Result(object):
    @staticmethod
    def get_result(success, code, type, detail):
        result = dict()
        result["success"] = success
        result["code"] = code
        result["type"] = type
        result["detail"] = detail
        return result

    @staticmethod
    def result(code, detail):
        result = dict()
        result["code"] = code
        result["detail"] = detail
        return result

    @staticmethod
    def result_published(detail=PUBLISHED):
        return Result.result(CODE_PUBLISHED, detail)

    @staticmethod
    def result_success(detail=SUCCESS):
        return Result.result(CODE_SUCCESS, detail)

    @staticmethod
    def result_failed(detail=FAILED):
        return Result.result(CODE_FAILED, detail)

    @staticmethod
    def result_exist(detail=USER_EXIST):
        return Result.result(CODE_EXIST, detail)

    @staticmethod
    def does_user_exist(result):
        code = result.get("code", 0)
        return code == CODE_EXIST

    @staticmethod
    def result_not_login(detail=NOT_LOGIN):
        return Result.result(CODE_NOT_LOGIN, detail)

    @staticmethod
    def result_no_permission(detail=NO_PERMISSION):
        return Result.result(CODE_NO_PERMISSION, detail)

    @staticmethod
    def result_not_exist(detail=NOT_EXIST):
        return Result.result(CODE_NOT_EXIST, detail)

    @staticmethod
    def result_parameters_are_invalid(detail=PARAMETERS_ARE_INVALID):
        return Result.result(CODE_PARAMETERS_ARE_INVALID, detail)

    @staticmethod
    def result_exception(detail=EXCEPTION_DETAIL):
        return Result.result(CODE_EXCEPTION, detail)

    @staticmethod
    def result_unsafe(detail=LOGIN_UNSAFE):
        return Result.result(CODE_UNSAFE, detail)

    @staticmethod
    def result_device_used_by_other(detail=USED_BY_OTHER):
        return Result.result(CODE_DEVICE_USED_BY_OTHER, detail)

    @staticmethod
    def result_password_is_incorrect():
        return Result.result(CODE_PASSWORD_IS_INCORRECT, PASSWORD_IS_INCORRECT)

    @staticmethod
    def result_has_valid_meet_apply(detail=HAS_VALID_MEET_APPLY):
        return Result.result(CODE_HAS_VALID_MEET_APPLY, detail)

    @staticmethod
    def result_is_meet(detail=HAS_MET):
        return Result.result(CODE_HAS_MET, detail)

    @staticmethod
    def is_needed(result, needed_code):
        try:
            return result.get("code", 0) == needed_code
        except:
            return False

    @staticmethod
    def is_user_added(result):
        return int(result.get("code", 0)) > 0

    @staticmethod
    def is_not_exist(result):
        return result.get("code", 0) == CODE_NOT_EXIST

    @staticmethod
    def is_relation_added(result):
        return int(result.get("code", 0)) > 0

    @staticmethod
    def is_success(result):
        return Result.is_needed(result, CODE_SUCCESS)

    @staticmethod
    def is_unsafe(result):
        return Result.is_needed(result, CODE_UNSAFE)

    @staticmethod
    def is_device_used_by_other(result):
        return Result.is_needed(result, CODE_DEVICE_USED_BY_OTHER)

    @staticmethod
    def is_password_incorrect(result):
        return Result.is_needed(result, CODE_PASSWORD_IS_INCORRECT)

    @staticmethod
    def is_update_beyond_three_month(result):
        return Result.is_needed(result, CODE_UPDATE_BEYOND_THREE_MONTH)

    @staticmethod
    def result_update_beyond_three_month(detail=UPDATE_BEYOND_THREE_MONTH):
        return Result.result(CODE_UPDATE_BEYOND_THREE_MONTH, detail)
