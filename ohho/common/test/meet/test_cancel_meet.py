from ohho.common.test.test_base import *


class TestCancelMeetHandler(TestBase):
    def initialize(self):
        super(TestCancelMeetHandler, self).initialize(
            CANCEL_MEET_HTML,
            CANCEL_MEET_URL)

