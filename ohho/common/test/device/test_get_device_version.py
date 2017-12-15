from ohho.common.test.test_base import *


class TestGetDeviceVersionHandler(TestBase):
    def initialize(self):
        super(TestGetDeviceVersionHandler, self).initialize(
            GET_DEVICE_VERSION_HTML,
            GET_DEVICE_VERSION_URL)


