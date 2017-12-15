from ohho.common.test.test_base import *


class TestAddExcludeHandler(TestBase):
    def initialize(self):
        super(TestAddExcludeHandler, self).initialize(
            ADD_EXCLUDE_HTML,
            ADD_EXCLUDE_URL)
