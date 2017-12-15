from ohho.common.test.test_base import *


class TestSetLostHandler(TestBase):
    def initialize(self):
        super(TestSetLostHandler, self).initialize(
            SET_LOST_HTML,
            SET_LOST_URL)

