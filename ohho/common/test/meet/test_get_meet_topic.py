from ohho.common.test.test_base import *


class TestGetMeetTopicHandler(TestBase):
    def initialize(self):
        super(TestGetMeetTopicHandler, self).initialize(
            GET_MEET_TOPIC_HTML,
            GET_MEET_TOPIC_URL,
            action_method="GET"
        )
