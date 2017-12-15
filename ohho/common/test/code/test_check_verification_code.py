from ohho.common.test.test_base import *


class TestCheckVerificationCodeHandler(TestBase):
    def initialize(self):
        super(TestCheckVerificationCodeHandler, self).initialize(
            CHECK_VERIFICATION_CODE_HTML,
            CHECK_VERIFICATION_CODE_URL,
            action_method="GET"
        )
