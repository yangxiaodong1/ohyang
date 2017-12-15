from ohho.common.test.test_base import *


class TestMeetEndHandler(TestBase):
    def initialize(self):
        super(TestMeetEndHandler, self).initialize(
            END_MEET_HTML,
            END_MEET_URL)
