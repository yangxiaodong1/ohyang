from ohho.common.test.test_base import *


class TestGetMeetStateHandler(TestBase):
    def initialize(self):
        super(TestGetMeetStateHandler, self).initialize(
            GET_MEET_STATE_HTML,
            GET_MEET_STATE_URL)
