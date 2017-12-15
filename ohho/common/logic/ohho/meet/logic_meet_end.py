from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.constant import *
from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
from ohho.common.db.ohho.device.db_ohho_device_sensor import DBOHHODeviceSensor
from settings import DEFAULT_IM_USER_ID
from Tools.ohho_log import OHHOLog


class LogicMeetEnd(object):
    def __init__(self):
        self.meet = Meet()
        self.user = User()
        self.map = DBOHHOMapInformation()
        self.sensor = DBOHHODeviceSensor()

    def push_information(self, to_user_id, user_id, apply_id, type, base_url):
        information = self.user.get_meet_end_user_information(user_id, apply_id, base_url)
        information["function"] = "meet end"
        return self.user.push_user_information(to_user_id, type, information)

    def delete_map(self, user_id):
        query = self.map.filter_by_user(user_id)
        self.map.delete_some(query)

    def delete_sensor(self, user_id):
        query = self.sensor.get_query()
        query = self.sensor.get_by_user(query, user_id)
        self.sensor.delete_some(query)

    def delete_meeting(self, apply_id, user_id):
        if self.meet.is_apply_in_meeting(apply_id, user_id):
            self.meet.delete_meeting(apply_id, user_id)

    def meet_end(self, user_id, friend_user_id, apply_id, base_url):
        apply_id = int(apply_id)
        if apply_id:
            the_map = self.map.get_by_user(user_id)
            if the_map:
                address = the_map.address
            else:
                address = ""
            self.meet.add_meet_end(apply_id, user_id, address)

            type = PUSH_STATE_TYPE_END_MEET
            is_meet_end = self.meet.is_meet_end(apply_id, friend_user_id)
            if not is_meet_end:
                self.push_information(friend_user_id, user_id, apply_id, type, base_url)
            # information = dict()
            # information["function"] = "meet end"
            # self.user.push_user_information(friend_user_id, PUSH_STATE_TYPE_END_MEET, information)

            # self.delete_map(user_id)
            # self.delete_map(friend_user_id)
            # self.delete_sensor(user_id)
            # self.delete_sensor(friend_user_id)

            self.delete_meeting(apply_id, user_id)
            # self.delete_meeting(apply_id, friend_user_id)

            return Result.result_success()
        else:
            return Result.result_failed("apply_is is %d" % (int(apply_id)))

            #
            # information = self.user.get_push_user_information(friend_user_id)
            # self.user.push_user_information(user_id, PUSH_STATE_TYPE_MET, information)
            # information = self.user.get_push_user_information(user_id)
            # self.user.push_user_information(friend_user_id, PUSH_STATE_TYPE_MET, information)
            #
            # user_map = self.map.get_by_user(user_id)
            # friend_user_map = self.map.get_by_user(friend_user_id)
            # data = dict()
            # data["user_id"] = user_id
            # data["another_user_id"] = friend_user_id
            # data["apply_id"] = apply_id
            # data["user_address"] = user_map.address
            # data["friend_user_map"] = friend_user_map.address
            # data["type"] = 0
            # self.meet.add_met(data)
