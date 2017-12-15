from ohho.common.test.test_base import *


class TestGetUserAndDeviceIMEIHandler(TestBase):
    def initialize(self):
        super(TestGetUserAndDeviceIMEIHandler, self).initialize(
            GET_USER_AND_DEVICE_IMEI_HTML,
            GET_USER_AND_DEVICE_IMEI_URL)


