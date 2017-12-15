from ohho.common.test.test_base import *


class TestGetUserPersonalInformationHandler(TestBase):
    def initialize(self):
        super(TestGetUserPersonalInformationHandler, self).initialize(
            GET_USER_PERSONAL_INFORMATION_HTML,
            GET_USER_PERSONAL_INFORMATION_URL)

