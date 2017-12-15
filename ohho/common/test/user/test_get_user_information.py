from ohho.common.test.test_base import *


class TestGetUserInformationHandler(TestBase):
    def initialize(self):
        super(TestGetUserInformationHandler, self).initialize(
            GET_USER_INFORMATION_HTML,
            GET_USER_INFORMATION_URL)

