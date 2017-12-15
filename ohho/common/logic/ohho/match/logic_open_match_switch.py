from ohho.common.db.ohho.user.db_ohho_user_configuration import DBOHHOUserConfiguration
from ohho.common.logic.common.result import Result


class LogicOpenMatchSwitch(object):
    def __init__(self):
        self.configuration = DBOHHOUserConfiguration()

    def open_match_switch(self, user_id):
        configuration = self.configuration.get_by_user(user_id)
        if configuration:
            success = self.configuration.open_match(configuration)
            if success:
                result = Result.result_success("open match successfully!")
            else:
                result = Result.result_failed("open match failed!")
        else:
            data_dict = dict()
            data_dict["user_id"] = user_id
            data_dict["is_switch"] = 1
            success = self.configuration.add(data_dict)
            if success:
                result = Result.result_success("add open match successfully!")
            else:
                result = Result.result_failed("add open match failed!")
        return result
