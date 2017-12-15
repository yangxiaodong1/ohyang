from ohho.common.test.test_base import *


class TestAddCancelMeetFeedbackHandler(TestBase):
    def initialize(self):
        super(TestAddCancelMeetFeedbackHandler, self).initialize(
            ADD_CANCEL_MEET_FEEDBACK_HTML,
            ADD_CANCEL_MEET_FEEDBACK_URL)
