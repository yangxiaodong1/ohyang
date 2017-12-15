from ohho.common.test.test_base import *


class TestAddUserAccuracyExtensionHandler(TestBase):
    def initialize(self):
        super(TestAddUserAccuracyExtensionHandler, self).initialize(
            ADD_USER_EXTENSION_HTML,
            ADD_USER_EXTENSION_URL)

