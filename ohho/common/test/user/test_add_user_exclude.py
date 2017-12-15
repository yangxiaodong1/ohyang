from ohho.common.test.test_base import *


class TestAddUserExcludeHandler(TestBase):
    def initialize(self):
        super(TestAddUserExcludeHandler, self).initialize(
            ADD_USER_EXCLUDE_HTML,
            ADD_USER_EXCLUDE_URL)
