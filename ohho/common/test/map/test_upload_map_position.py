from ohho.common.test.test_base import *


class TestUploadMapPositionHandler(TestBase):
    def initialize(self):
        super(TestUploadMapPositionHandler, self).initialize(
            UPLOAD_MAP_POSITION_HTML,
            UPLOAD_MAP_POSITION_URL)

