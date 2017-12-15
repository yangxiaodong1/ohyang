from ohho.common.test.test_base import *


class TestMeetHandler(TestBase):
    def initialize(self):
        super(TestMeetHandler, self).initialize(
            MEET_HTML,
            MEET_URL)
