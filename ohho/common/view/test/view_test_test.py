import tornado.web
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog
from ohho.common.view.common.parameters import Post, Get
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.draw import Draw

from ohho.common.logic.test.logic_test_get_user_by_device import LogicTestGetUserByDevice
from Tools.decorator import authenticate


class TestTestHandler(tornado.web.RequestHandler):
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

    def get(self):
        x_list = [[1, 2, 3], [1, 2, 3]]
        y_list = [[5, 7, 4], [10, 14, 12]]
        label_list = ['First Line', 'Second Line']
        x_label = 'x'
        y_label = 'y'
        title = 'test'
        name = 'test007.png'
        Draw.draw_line(x_list, y_list, label_list, x_label, y_label, title, name)
        result = Result.result_success()
        self.write(OHHOOperation.dict2json(result))
        # the_get = Get()
        # device_identities = the_get.get_device_identities(self)
        # identity_list = device_identities.split(",")
        # result = LogicTestGetUserByDevice.get(identity_list)
        # self.write(OHHOOperation.dict2json(result))
