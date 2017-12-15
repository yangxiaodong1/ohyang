from ohho.common.test.test_base import *


class StressTestAddUserHandler(TestBase):
    def initialize(self):
        super(StressTestAddUserHandler, self).initialize(
            STRESS_TESTING_ADD_USER_HTML,
            STRESS_TESTING_ADD_USER_URL)