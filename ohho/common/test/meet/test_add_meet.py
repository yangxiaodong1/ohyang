from ohho.common.test.test_base import *


class TestAddMeetHandler(TestBase):
    def initialize(self):
        super(TestAddMeetHandler, self).initialize(
            ADD_MEET_HTML,
            ADD_MEET_URL)
