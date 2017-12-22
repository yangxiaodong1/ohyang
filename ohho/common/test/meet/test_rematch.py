from ohho.common.test.test_base import *


class TestRematchHandler(TestBase):
    def initialize(self):
        super(TestRematchHandler, self).initialize(
            REMATCH_HTML,
            REMATCH_URL)
