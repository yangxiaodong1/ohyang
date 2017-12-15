from ohho.common.test.test_base import *


class TestRebindCellphoneHandler(TestBase):
    def initialize(self):
        super(TestRebindCellphoneHandler, self).initialize(
            REBIND_CELLPHONE_HTML,
            REBIND_CELLPHONE_URL)
