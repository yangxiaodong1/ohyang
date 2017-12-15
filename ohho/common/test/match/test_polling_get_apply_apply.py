from ohho.common.test.test_base import *


class TestPollingGetApplyApplyHandler(TestBase):
    def initialize(self):
        super(TestPollingGetApplyApplyHandler, self).initialize(
            POLLING_GET_APPLY_HTML,
            POLLING_GET_APPLY_URL)

