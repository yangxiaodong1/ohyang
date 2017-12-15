from ohho.common.test.test_base import *


class TestGetUserPersonalPageHandler(TestBase):
    def initialize(self):
        super(TestGetUserPersonalPageHandler, self).initialize(
            GET_USER_PERSONAL__HTML,
            GET_USER_PERSONAL_PAGE_URL)

