
from ohho.common.test.test_base import *


class TestGetBoundDeviceHandler(TestBase):
    def initialize(self):
        super(TestGetBoundDeviceHandler, self).initialize(
            GET_BOUND_DEVICES_HTML,
            GET_BOUND_DEVICES_URL)

