from ohho.common.test.test_base import *


class TestGetUserByDeviceHandler(TestBase):
    def initialize(self):
        super(TestGetUserByDeviceHandler, self).initialize(
            GET_USER_BY_DEVICE_HTML,
            GET_USER_BY_DEVICE_URL)

