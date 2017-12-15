from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.view.common.parameters import Post, Get
from ohho.common.logic.common.result import Result
from ohho.common.logic.test.logic_test_add_map_information import LogicTestAddMapInformation
from Tools.ohho_log import OHHOLog


class TestAddMapInformationHandler(ViewOHHOBase):
    def post(self):
        the_request = Post()
        self.set_format(the_request.get_format(self))
        map_information = the_request.get_map_information(self)
        user_id = the_request.get_user_id(self)
        another_user_id = self.get_body_argument("another_user_id", 0)
        timestamp = the_request.get_timestamp(self)
        base_url = the_request.get_base_url(self)
        instance = LogicTestAddMapInformation()
        OHHOLog.print_log(map_information)
        result = instance.add(user_id, another_user_id, map_information, base_url, timestamp)

        return self.response(result)

    def get(self):
        the_request = Get()
        self.set_format(the_request.get_format(self))
        result = Result.result_success()
        return self.response(result)
