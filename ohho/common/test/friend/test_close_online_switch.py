from ohho.common.test.test_base import *


class TestCloseOnlineSwitchHandler(TestBase):
    def initialize(self):
        super(TestCloseOnlineSwitchHandler, self).initialize(
            CLOSE_ONLINE_SWITCH_HTML,
            CLOSE_ONLINE_SWITCH_URL)

