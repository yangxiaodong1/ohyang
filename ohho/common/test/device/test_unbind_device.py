from ohho.common.test.test_base import *


class TestUnbindDeviceHandler(TestBase):
    def initialize(self):
        super(TestUnbindDeviceHandler, self).initialize(
            UNBIND_DEVICE_HTML,
            UNBIND_DEVICE_URL)
