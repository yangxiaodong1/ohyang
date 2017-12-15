from ohho.common.db.ohho.user.db_ohho_user_configuration import DBOHHOUserConfiguration
from ohho.common.logic.common.result import Result


class LogicSetMatchSwitch(object):
    def __init__(self):
        self.configuration = DBOHHOUserConfiguration()

    def set_match_switch(self, user_id, is_match):
        configuration = self.configuration.get_by_user(user_id)
        if configuration:
            if is_match:
                success = self.configuration.open_match(configuration)
                if success:
                    result = Result.result_success("open match successfully!")
                else:
                    result = Result.result_failed("open match failed!")
            else:
                success = self.configuration.close_match(configuration)
                if success:
                    result = Result.result_success("close match successfully!")
                else:
                    result = Result.result_failed("close match failed!")
        else:
            data_dict = dict()
            data_dict["user_id"] = user_id
            data_dict["is_switch"] = is_match
            success = self.configuration.add(data_dict)
            if is_match:
                if success:
                    result = Result.result_success("add open match successfully!")
                else:
                    result = Result.result_failed("add open match failed!")
            else:
                if success:
                    result = Result.result_success("add close match successfully!")
                else:
                    result = Result.result_failed("add close match failed!")

        return result
