from ohho.common.test.test_base import *


class TestAddBodyTypeHandler(TestBase):
    def initialize(self):
        super(TestAddBodyTypeHandler, self).initialize(
            ADD_BODY_TYPE_HTML,
            ADD_BODY_TYPE_URL)
