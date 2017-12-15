from Tools.ohho_operation import OHHOOperation
from ohho.common.logic.common.result import Result
from ohho.common.db.ohho.user.user import User


class LogicAddUserBasic(object):
    @staticmethod
    def add_basic(user_id, data):
        extension, description_I_am, description_I_like, description_I_unlike, description_I_hope = LogicAddUserBasic.parse_parameter(
            data)
        user = User()
        success = user.add_basic(user_id, extension,
                                 description_I_am,
                                 description_I_like,
                                 description_I_unlike,
                                 description_I_hope
                                 )
        if success:
            return Result.result_success()
        else:
            return Result.result_failed()

    @staticmethod
    def parse_parameter(data):
        data_dict = OHHOOperation.json2dict(data)
        extension = data_dict.get("extension", dict())
        description_I_am = data_dict.get("I_am", dict())
        description_I_like = data_dict.get("I_like", dict())
        description_I_unlike = data_dict.get("I_unlike", dict())
        description_I_hope = data_dict.get("I_hope", dict())
        return extension, description_I_am, description_I_like, \
               description_I_unlike, description_I_hope
