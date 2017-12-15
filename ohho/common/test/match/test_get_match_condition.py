from ohho.common.test.test_base import *


class TestGetMatchConditionHandler(TestBase):
    def initialize(self):
        super(TestGetMatchConditionHandler, self).initialize(
            GET_MATCH_CONDITION_HTML,
            GET_MATCH_CONDITION_URL)
