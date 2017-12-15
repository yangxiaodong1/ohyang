from ohho.common.test.test_base import *


class TestRegisterHandler(TestBase):
    def initialize(self):
        super(TestRegisterHandler, self).initialize(
            REGISTER_HTML,
            REGISTER_URL)

