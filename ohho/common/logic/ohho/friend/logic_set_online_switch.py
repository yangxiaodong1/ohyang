from ohho.common.db.ohho.user.db_ohho_user_configuration import DBOHHOUserConfiguration
from ohho.common.logic.common.result import Result


class LogicSetOnlineSwitch(object):
    def __init__(self):
        self.configuration = DBOHHOUserConfiguration()

    def set_online_switch(self, user_id, is_online):
        configuration = self.configuration.get_by_user(user_id)
        if configuration:
            if is_online:
                success = self.configuration.open_online(configuration)
                if success:
                    result = Result.result_success("open online successfully!")
                else:
                    result = Result.result_failed("open online failed!")
            else:
                success = self.configuration.close_online(configuration)
                if success:
                    result = Result.result_success("close online successfully!")
                else:
                    result = Result.result_failed("close online failed!")
        else:
            data_dict = dict()
            data_dict["user_id"] = user_id
            data_dict["is_online"] = is_online
            success = self.configuration.add(data_dict)
            if is_online:
                if success:
                    result = Result.result_success("add open online successfully!")
                else:
                    result = Result.result_failed("add open online failed!")
            else:
                if success:
                    result = Result.result_success("add close online successfully!")
                else:
                    result = Result.result_failed("add close online failed!")

        return result
