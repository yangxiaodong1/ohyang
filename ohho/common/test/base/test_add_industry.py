from ohho.common.test.test_base import *


class TestAddIndustryHandler(TestBase):
    def initialize(self):
        super(TestAddIndustryHandler, self).initialize(
            ADD_INDUSTRY_HTML,
            ADD_INDUSTRY_URL)
