from ohho.common.test.test_base import *


class TestIsDeviceValidHandler(TestBase):
    def initialize(self):
        super(TestIsDeviceValidHandler, self).initialize(
            IS_DEVICE_VALID_HTML,
            IS_DEVICE_VALID_URL)

