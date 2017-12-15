from ohho.common.test.test_base import *


class TestRefuseMeetHandler(TestBase):
    def initialize(self):
        super(TestRefuseMeetHandler, self).initialize(
            REFUSE_MEET_HTML,
            REFUSE_MEET_URL)

