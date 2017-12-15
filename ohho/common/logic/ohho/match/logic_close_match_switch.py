from ohho.common.db.ohho.user.db_ohho_user_configuration import DBOHHOUserConfiguration
from ohho.common.logic.common.result import Result


class LogicCloseMatchSwitch(object):
    def __init__(self):
        self.configuration = DBOHHOUserConfiguration()

    def close_match_switch(self, user_id):
        configuration = self.configuration.get_by_user(user_id)
        if configuration:
            success = self.configuration.close_match(configuration)
            if success:
                result = Result.result_success("close match successfully!")
            else:
                result = Result.result_failed("close match failed!")
        else:
            data_dict = dict()
            data_dict["user_id"] = user_id
            data_dict["is_switch"] = 0
            success = self.configuration.add(data_dict)

            if success:
                result = Result.result_success("add close match successfully!")
            else:
                result = Result.result_failed("add close match failed!")

        return result
