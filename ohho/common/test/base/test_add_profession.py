from ohho.common.test.test_base import *


class TestAddProfessionHandler(TestBase):
    def initialize(self):
        super(TestAddProfessionHandler, self).initialize(
            ADD_PROFESSION_HTML,
            ADD_PROFESSION_URL
        )
