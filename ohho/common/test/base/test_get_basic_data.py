from ohho.common.test.test_base import *


class TestGetBasicDataHandler(TestBase):
    def initialize(self):
        super(TestGetBasicDataHandler, self).initialize(
            GET_BASIC_DATA_HTML,
            GET_BASIC_DATA_URL,
            action_method="GET"
        )
