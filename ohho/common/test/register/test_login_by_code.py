from ohho.common.test.test_base import *


class TestLoginByCodeHandler(TestBase):
    def initialize(self):
        super(TestLoginByCodeHandler, self).initialize(
            LOGIN_BY_CODE_HTML,
            LOGIN_BY_CODE_URL)