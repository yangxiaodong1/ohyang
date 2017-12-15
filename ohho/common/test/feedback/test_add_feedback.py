from ohho.common.test.test_base import *


class TestAddFeedbackHandler(TestBase):
    def initialize(self):
        super(TestAddFeedbackHandler, self).initialize(
            ADD_FEEDBACK_HTML,
            ADD_FEEDBACK_URL)
