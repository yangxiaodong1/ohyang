from ohho.common.test.test_base import *


class TestGetDeviceSettingHandler(TestBase):
    def initialize(self):
        super(TestGetDeviceSettingHandler, self).initialize(
            GET_DEVICE_SETTING_HTML,
            GET_DEVICE_SETTING_URL)


