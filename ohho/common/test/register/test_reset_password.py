from ohho.common.test.test_base import *


class TestResetPasswordHandler(TestBase):
    def initialize(self):
        super(TestResetPasswordHandler, self).initialize(
            RESET_PASSWORD_HTML,
            RESET_PASSWORD_URL)

