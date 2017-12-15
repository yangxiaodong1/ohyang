from ohho.common.test.test_base import *


class TestAddWorkDomainHandler(TestBase):
    def initialize(self):
        super(TestAddWorkDomainHandler, self).initialize(
            ADD_WORK_DOMAIN_HTML,
            ADD_WORK_DOMAIN_URL)
