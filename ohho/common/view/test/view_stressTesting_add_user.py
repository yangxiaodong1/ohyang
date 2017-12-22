from ohho.common.view.view_ohho_base import ViewOHHOBase
from ohho.common.view.common.parameters import Post, Get

from stressTesting.logic.logic_add_user import LogicAddUser
from Tools.decorator import execute_time
class StressTestingAddUserHandler(ViewOHHOBase):
    @execute_time
    def post(self):
        the_request = Post()
        instance = LogicAddUser()
        self.set_format(the_request.get_format(self))
        number = self.get_body_argument("number", "")
        if number:
            pass
        else:
            number = 10

        # instance.add_user1(int(number))
        instance.add_user_commit_all(int(number))

        return self.write(str(number))

    def get(self):
        the_request = Get()

        return self.write("get")
