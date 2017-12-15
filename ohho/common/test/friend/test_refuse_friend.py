from ohho.common.test.test_base import *


class TestRefuseFriendHandler(TestBase):
    def initialize(self):
        super(TestRefuseFriendHandler, self).initialize(
            REFUSE_FRIEND_HTML,
            REFUSE_FRIEND_URL)

