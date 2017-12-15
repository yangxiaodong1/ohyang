from ohho.common.test.test_base import *


class TestUpdateDeviceSettingHandler(TestBase):
    def initialize(self):
        super(TestUpdateDeviceSettingHandler, self).initialize(
            UPDATE_DEVICE_SETTING_HTML,
            UPDATE_DEVICE_SETTING_URL)

