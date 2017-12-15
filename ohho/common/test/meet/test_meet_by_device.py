from ohho.common.test.test_base import *


class TestMeetByDeviceHandler(TestBase):
    def initialize(self):
        super(TestMeetByDeviceHandler, self).initialize(
            MET_BY_DEVICE_HTML,
            MET_BY_DEVICE_URL)

