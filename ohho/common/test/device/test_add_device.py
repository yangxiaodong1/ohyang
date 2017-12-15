
from ohho.common.test.test_base import *


class TestAddDeviceHandler(TestBase):
    def initialize(self):
        super(TestAddDeviceHandler, self).initialize(
            ADD_DEVICE_HTML,
            ADD_DEVICE_URL)
