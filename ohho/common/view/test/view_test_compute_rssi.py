from ohho.common.view.view_ohho_base import ViewOHHOBase
from Tools.ohho_log import OHHOLog
from ohho.common.view.common.parameters import Post, Get
from ohho.common.logic.common.result import Result
from ohho.common.logic.test.logic_test_compute_rssi import LogicTestComputeRssi


class TestComputeRssiHandler(ViewOHHOBase):
    def post(self):
        the_request = Post()
        self.set_format(the_request.get_format(self))
        phone = self.get_body_argument("phone", "")
        distance = self.get_body_argument("distance", None)
        timestamp = self.get_body_argument("timestamp", None)

        instance = LogicTestComputeRssi()
        result = instance.add(timestamp, phone, distance)
        return self.response(result)

    def get(self):
        the_request = Get()
        self.set_format(the_request.get_format(self))
        result = Result.result_success()
        return self.response(result)
