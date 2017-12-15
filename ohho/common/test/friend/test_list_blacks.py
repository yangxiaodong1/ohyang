from ohho.common.test.test_base import *


class TestListBlacksHandler(TestBase):
    def initialize(self):
        super(TestListBlacksHandler, self).initialize(
            LIST_BLACKS_HTML,
            LIST_BLACKS_URL)
