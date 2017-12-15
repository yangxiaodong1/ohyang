from ohho.common.test.test_base import *


class TestPollingGetApplyStateHandler(TestBase):
    def initialize(self):
        super(TestPollingGetApplyStateHandler, self).initialize(
            POLLING_GET_APPLIED_HTML,
            POLLING_GET_APPLIED_URL)

