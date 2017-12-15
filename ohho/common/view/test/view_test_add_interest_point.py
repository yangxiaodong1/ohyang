from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.view.common.parameters import Post, Get
from ohho.common.logic.common.result import Result
from ohho.common.logic.test.logic_test_add_interest_point import LogicTestAddInterestPoint


class TestAddInterestPointHandler(ViewOHHOBase):
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
        result = Result.result_success()
        return self.response(result)
