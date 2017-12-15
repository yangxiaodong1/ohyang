from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.view.common.parameters import Post, Get
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.test.logic_test_add_interest_point import LogicTestAddInterestPoint


class TestShowUserBasicInformation(ViewOHHOBase):
    def post(self):
        the_request = Post()
        self.set_format(the_request.get_format(self))
        data = self.request.body
        instance = LogicTestAddInterestPoint()

        result = instance.add(data)
        return self.response(result)

    def get(self):
        the_request = Get()
        self.set_format(the_request.get_format(self))
        user_id = the_request.get_user_id(self)
        base_url = the_request.get_base_url(self)

        user = User()
        data = user.get_basic_user_information(user_id, base_url)

        result = Result.result_success()
        result["data"] = data
        return self.response(result)
