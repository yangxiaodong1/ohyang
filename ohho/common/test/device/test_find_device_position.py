
from ohho.common.test.test_base import *


class TestFindDevicePositionHandler(TestBase):
    def initialize(self):
        super(TestFindDevicePositionHandler, self).initialize(
            FIND_DEVICE_POSITION_HTML,
            FIND_DEVICE_POSITION_URL)

