from ohho.common.test.test_base import *


class TestAddUserIconHandler(TestBase):
    def initialize(self):
        super(TestAddUserIconHandler, self).initialize(
            ADD_USER_ICON_HTML,
            ADD_USER_ICON_URL,
            enctype="multipart/form-data",
        )
