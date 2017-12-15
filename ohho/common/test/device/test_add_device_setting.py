from ohho.common.test.test_base import *


class TestAddDeviceSettingHandler(TestBase):
    def initialize(self):
        super(TestAddDeviceSettingHandler, self).initialize(
            ADD_DEVICE_SETTING_HTML,
            ADD_DEVICE_SETTING_URL)
