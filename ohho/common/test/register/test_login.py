from ohho.common.test.test_base import *


class TestLoginHandler(TestBase):
    def initialize(self):
        super(TestLoginHandler, self).initialize(
            LOGIN_HTML,
            LOGIN_URL)


