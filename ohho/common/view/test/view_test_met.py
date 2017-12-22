import tornado.web
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog
from ohho.common.view.common.parameters import Post, Get
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.record.meet import Meet
# from ohho.common.logic.common.draw import Draw

from ohho.common.logic.test.logic_test_get_user_by_device import LogicTestGetUserByDevice
from Tools.decorator import authenticate


class TestMetHandler(tornado.web.RequestHandler):
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
        the_get = Get()
        user_id = the_get.get_user_id(self)
        friend_user_id = the_get.get_friend_id(self)
        is_delete = the_get.get_delete(self)
        user = User()
        meet = Meet()
        the_user = user.get_by_id(user_id)
        the_friend = user.get_by_id(friend_user_id)
        if is_delete:
            met_instance = meet.get_met_by_users(user_id, friend_user_id)
            success = meet.met.delete(met_instance)
            if success:
                result = Result.result_success("delete successfully!")
            else:
                result = Result.result_failed("delete failed!")
        else:
            if the_user and the_friend:

                success = meet.add_apply(user_id, friend_user_id)
                if success:
                    apply = meet.get_apply_by_user_and_friend(user_id, friend_user_id)
                    if apply:
                        data = dict()
                        data["apply_id"] = apply.id
                        data["user_id"] = user_id
                        data["another_user_id"] = friend_user_id
                        success = meet.add_met(data)
                        if success:
                            result = Result.result_success("add successfully!")
                        else:
                            result = Result.result_failed("add met failed!")
                    else:
                        result = Result.result_failed("get apply failed!")
                else:
                    result = Result.result_failed("add apply failed!")
            else:
                result = Result.result_failed("user does not exist!")

        self.write(OHHOOperation.dict2json(result))


        # x_list = [[1, 2, 3], [1, 2, 3]]
        # y_list = [[5, 7, 4], [10, 14, 12]]
        # label_list = ['First Line', 'Second Line']
        # x_label = 'x'
        # y_label = 'y'
        # title = 'test'
        # name = 'test007.png'
        # Draw.draw_line(x_list, y_list, label_list, x_label, y_label, title, name)
        # result = Result.result_success()
        # self.write(OHHOOperation.dict2json(result))
