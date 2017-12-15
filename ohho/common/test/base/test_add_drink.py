from ohho.common.test.test_base import *


class TestAddDrinkHandler(TestBase):
    def initialize(self):
        super(TestAddDrinkHandler, self).initialize(
            ADD_DRINK_HTML,
            ADD_DRINK_URL)
