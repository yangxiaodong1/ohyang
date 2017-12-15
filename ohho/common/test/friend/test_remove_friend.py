from ohho.common.test.test_base import *


class TestRemoveFriendHandler(TestBase):
    def initialize(self):
        super(TestRemoveFriendHandler, self).initialize(
            REMOVE_FRIEND_HTML,
            REMOVE_FRIEND_URL)
