from ohho.common.test.test_base import *


class TestMeetSendMessageHandler(TestBase):
    def initialize(self):
        super(TestMeetSendMessageHandler, self).initialize(
            MEET_SEND_MESSAGE_HTML,
            MEET_SEND_MESSAGE_URL)
