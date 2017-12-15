from ohho.common.test.test_base import *


class TestVersion2MatchHandler(TestBase):
    def initialize(self):
        super(TestVersion2MatchHandler, self).initialize(
            VERSION2_MATCH_HTML,
            VERSION2_MATCH_URL)

