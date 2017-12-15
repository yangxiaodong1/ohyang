from ohho.common.test.test_base import *


class TestLogoutHandler(TestBase):
    def initialize(self):
        super(TestLogoutHandler, self).initialize(
            LOGOUT_HTML,
            LOGOUT_URL)

