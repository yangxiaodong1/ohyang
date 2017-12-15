from ohho.common.test.test_base import *


class TestSendVerificationCodeHandler(TestBase):
    def initialize(self):
        super(TestSendVerificationCodeHandler, self).initialize(
            SEND_VERIFICATION_CODE_HTML,
            SEND_VERIFICATION_CODE_URL)


