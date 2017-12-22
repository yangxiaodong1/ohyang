import tornado.web
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog
from ohho.common.view.common.parameters import Post, Get
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from Tools.ohho_uuid import OHHOUUID
from Tools.decorator import execute_time
from tornado import gen


class TestAddNewUserHandler(tornado.web.RequestHandler):
    def post(self):
        # name = self.get_body_argument("user_name", None)
        result = dict()
        # base_url = the_post.get_base_url(self)
        user = User()
        user_id = 4
        friend_user_id = 13
        log_string = "1234567890"
        OHHOLog.print_log(log_string)
        # message = user.get_user_basic_information(user_id, base_url)
        user.push(log_string, friend_user_id, user_id)
        # return Result.result_success()

        self.write(OHHOOperation.dict2json(result))
        # self.write("This is a %s method, %s is not supported" % ("get", "post"))

    @execute_time
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        @gen.coroutine
        def add_new_user(password, cellphone, country_code="+86"):
            username = OHHOUUID.get_uuid1_string()
            user = User()
            user.set_username(username)
            OHHOLog.print_log(user.add_user(password, cellphone, country_code))
            the_user = user.get_by_username(username)
            if the_user:
                result = Result.result_success()
                result["user_id"] = the_user.id
            else:
                result = Result.result_failed()
                result["user_id"] = 0
            return result

        password = '111111'
        # cellphone = 0

        for i in range(10000):
            OHHOLog.print_log(i)
            gen.Task(add_new_user, password, i)
            # yield add_new_user(password, i)
        OHHOLog.print_log("end")
        self.write(Result.result_success())
        self.finish()
