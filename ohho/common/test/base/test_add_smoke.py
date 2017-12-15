from ohho.common.test.test_base import *


class TestAddSmokeHandler(TestBase):
    def initialize(self):
        super(TestAddSmokeHandler, self).initialize(
            ADD_SMOKE_HTML,
            ADD_SMOKE_URL)
