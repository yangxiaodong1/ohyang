from ohho.common.db.ohho.device.db_ohho_device import DBOHHODevice
from ohho.common.db.ohho.relation.db_ohho_user_and_device_relation import DBOHHOUserAndDeviceRelation
from ohho.common.db.ohho.user.db_ohho_user_display_configuration import DBOHHOUserDisplayConfiguration

from ohho.common.logic.common.bluetooth import Bluetooth
from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.user import User
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.constant import *

MEET_DISTANCE = 5


class LogicBluetoothPosition(object):
    def __init__(self):
        self.blue_tooth = Bluetooth()
        self.meet = Meet()
        self.user = User()
        self.device = DBOHHODevice()
        self.relation = DBOHHOUserAndDeviceRelation()
        self.display_configuration = DBOHHOUserDisplayConfiguration()

    def get_display_instance(self, distance):
        instance = self.display_configuration.get_nearest_distance(distance)
        return instance

    def get_information(self, user_extension, instance):
        information = dict()
        if instance.has_sex:
            information["sex"] = user_extension.sex

        return information

    def get_push_data_by_distance(self, user_id, apply_id, distance, base_url):
        user_extension = self.user.user_extension.get_by_user(user_id)
        instance = self.get_display_instance(distance)
        information = dict()
        if user_extension and instance:
            information = self.get_information(user_extension, instance)
        return information

    def bluetooth_position(self, user_id, identity_id, rssi, distance, apply_id, base_url):
        the_meeting = self.meet.is_apply_in_meeting(apply_id, user_id)
        if the_meeting:
            friend_user_id = self.meet.get_another_user_id(apply_id, user_id)
            is_friend_end = self.meet.is_meet_end(apply_id, friend_user_id)
            is_friend_met = self.meet.is_met(apply_id)

            if is_friend_met:
                the_type = PUSH_STATE_TYPE_MET
                information = self.get_push_data_by_distance(user_id, apply_id, distance, base_url)
                information["is_blue_tooth"] = 1
                self.user.push_user_information(friend_user_id, the_type, information)

                information = self.get_push_data_by_distance(friend_user_id, apply_id, distance, base_url)
                information["is_blue_tooth"] = 1
                self.user.push_user_information(user_id, the_type, information)

                return Result.result_success("met!")

            if not is_friend_end and not is_friend_met:
                if self.meet.is_met(apply_id):
                    the_type = PUSH_STATE_TYPE_MET
                elif self.meet.is_meet_end(apply_id, user_id):
                    the_type = PUSH_STATE_TYPE_END_MEET
                else:
                    the_type = PUSH_STATE_TYPE_MEETING
                information = self.get_push_data_by_distance(user_id, apply_id, distance, base_url)
                information["is_blue_tooth"] = 1
                self.user.push_user_information(friend_user_id, the_type, information)

                self.device.set_identity(identity_id)
                device = self.device.get_by_identity()
                if device:
                    self.blue_tooth.add_sensor(user_id, device.id, rssi, distance)
        return Result.result_success()
