from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
from ohho.common.db.ohho.device.db_ohho_device_sensor import DBOHHODeviceSensor
from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User


class LogicCancelMeet(object):
    def __init__(self):
        self.meet = Meet()
        self.user = User()
        self.map = DBOHHOMapInformation()
        self.sensor = DBOHHODeviceSensor()

    def cancel_meet(self, user_id, friend_user_id, apply_id, base_url):
        """
        取消见面
        只要自己申请过见面或自己同意过见 以取消见面
        :param user_id: 用户ID
        :param friend_user_id: 另一用户ID
        :param meet_state: 见面状态 0未见，1见面，2 请求相见，3同意相见，4不同意相见，5 取消见面，默认为0
        :return:
        """

        # information = self.user.get_push_user_information(user_id, apply_id, base_url)
        # information["function"] = "cancel meet"
        # self.user.push_user_information(friend_user_id, PUSH_STATE_TYPE_CANCEL_MEET, information)

        self.meet.add_exclude(user_id, friend_user_id)

        user_map = self.map.get_by_user(user_id)
        friend_map = self.map.get_by_user(friend_user_id)
        user_address = user_map.address if user_map else ""
        friend_user_address = friend_map.address if friend_map else ""

        self.meet.add_meet_end(apply_id, user_id, user_address)
        self.meet.add_meet_end(apply_id, friend_user_id, friend_user_address)

        self.meet.delete_meeting(apply_id, user_id)
        self.meet.delete_meeting(apply_id, friend_user_id)

        # user_map_query = self.map.filter_by_user(user_id)
        # self.map.delete_some(user_map_query)

        # friend_map_query = self.map.filter_by_user(friend_user_id)
        # self.map.delete_some(friend_map_query)

        # user_sensor_query = self.sensor.get_query()
        # user_sensor_query = self.sensor.get_by_user(user_sensor_query, user_id)

        # friend_user_query = self.sensor.get_query()
        # friend_sensor_query = self.sensor.get_by_user(friend_user_query, friend_user_id)

        # self.sensor.delete_some(user_sensor_query)
        # self.sensor.delete_some(friend_sensor_query)

        return Result.result_success()






        # apply = None
        # has_valid_apply = self.meet.has_valid_apply(friend_user_id, user_id)
        # if has_valid_apply:
        #     apply = self.meet.get_apply_by_user_and_friend(friend_user_id, user_id)
        #
        # has_valid_apply = self.meet.has_valid_apply(user_id, friend_user_id)
        # if has_valid_apply:
        #     apply = self.meet.get_apply_by_user_and_friend(user_id, friend_user_id)
        #
        # if apply:
        #     has_agree = self.meet.has_agree(apply.id)
        #     has_refuse = self.meet.has_refuse(apply.id)
        #     if has_agree and not has_refuse:
        #         success = self.meet.add_refuse(apply.id, user_id)
        #         if success:
        #
        #             log_string = "%d cancel %d to meet" % (user_id, friend_user_id)
        #             OHHOLog.print_log(log_string)
        #
        #             message = self.user.get_user_basic_information(user_id, base_url)
        #             self.user.push(log_string, friend_user_id, DEFAULT_IM_USER_ID)
        #             return Result.result_success()
        #         else:
        #             return Result.result_failed()
        #     else:
        #         return Result.result_failed("You have no agreed apply to cancel!")
        # else:
        #     return Result.result_failed("You have no valid apply!")
        #
        # # 推送给friend
        #
        # return result
