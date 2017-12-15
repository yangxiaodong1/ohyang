from ohho.common.test.test_base import *


class TestCompleteUserHandler(TestBase):
    def initialize(self):
        super(TestCompleteUserHandler, self).initialize(
            COMPLETE_USER_HTML,
            COMPLETE_USER_URL,
            enctype="multipart/form-data")
