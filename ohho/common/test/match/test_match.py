from ohho.common.test.test_base import *


class TestMatchHandler(TestBase):
    def initialize(self):
        super(TestMatchHandler, self).initialize(
            MATCH_HTML,
            MATCH_URL)

