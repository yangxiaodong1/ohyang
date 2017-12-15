from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
from ohho.common.db.ohho.user.db_ohho_user_configuration import DBOHHOUserConfiguration
from ohho.common.db.ohho.record.db_ohho_record_match_apply import DBOHHORecordMatchApply
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.constant import *
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_log import OHHOLog
from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_geohash import OHHOGeohash
from DB.redis.operation import RedisDB


class LogicUploadMapPosition(object):
    def __init__(self):
        self.map = DBOHHOMapInformation()
        self.user = User()
        self.meet = Meet()
        self.apply = DBOHHORecordMatchApply()
        self.user_configuration = DBOHHOUserConfiguration()

    def push_information(self, map_information, to_user_id, user_id, the_type, apply_id, base_url):
        information = self.user.get_meeting_user_information(user_id, apply_id, base_url)
        information = OHHOOperation.dict_add_dict(information, map_information)
        information["is_blue_tooth"] = 0

        information = self.user.set_map_by_exclude(information, to_user_id, user_id)
        information = self.user.set_map_by_is_online(information, to_user_id, user_id)
        created_at = information.get("created_at", None)
        if created_at:
            del information["created_at"]

        changed_at = information.get("changed_at", None)
        if changed_at:
            del information["changed_at"]
        return self.user.push_user_information(to_user_id, the_type, information)

    def return_map_information(self, friend_user_id):
        # timestamp = int(timestamp)
        result = dict()
        result["is_timeout"] = 0
        user = self.user.get_by_id(friend_user_id)
        if user:
            # map_information = RedisDB.hash_get(REDIS_MAP_INFORMATION, user.username)
            map_information = self.user.get_user_map_information_from_redis(user.username)
            # OHHOLog.print_log(map_information)
            map_information_dict = RedisDB.data2dict(map_information)

            map_information_dict["longitude"] = float(map_information_dict["longitude"])
            map_information_dict["latitude"] = float(map_information_dict["latitude"])
            map_information_dict["altitude"] = float(map_information_dict["altitude"])
            map_information_dict["accuracy"] = float(map_information_dict["accuracy"])
            # map_information_dict["speed"] = float(map_information_dict["speed"])
            map_information_dict["angle"] = float(map_information_dict["angle"])
            map_information_dict["satellite_number"] = int(map_information_dict["satellite_number"])

            now = OHHODatetime.get_current_timestamp()
            # OHHOLog.print_log(map_information_dict)
            # OHHOLog.print_log(now)
            # OHHOLog.print_log(map_information_dict["timestamp"])
            # OHHOLog.print_log(now - map_information_dict["timestamp"])
            if map_information_dict["timestamp"] > 0 and now - map_information_dict["timestamp"] > 30000:
                result["is_timeout"] = 1
                result["timestamp"] = now
                result["last_timestamp"] = map_information_dict["timestamp"]
            else:
                information = dict()
                information["user_id"] = friend_user_id
                information["latitude"] = float(map_information_dict["latitude"])
                information["longitude"] = float(map_information_dict["longitude"])
                information["accuracy"] = float(map_information_dict["accuracy"])
                information["supplier"] = map_information_dict["supplier"]
                if map_information_dict.get("floor", None):
                    information["floor"] = map_information_dict["floor"]
                information["address"] = map_information_dict["address"]
                information["timestamp"] = now
            result["information"] = map_information_dict

        return result

    # def upload_map_position(self, user_id, map_information, apply_id, base_url, timestamp=0):
    #     # 上传地图坐标，只保存最新的坐标
    #     information = dict()
    #     if map_information:
    #         longitude = float(map_information.get("longitude", 0))
    #         latitude = float(map_information.get("latitude", 0))
    #         geohash_code = OHHOGeohash.get(latitude, longitude, 6)
    #         map_information["geohash_code"] = geohash_code
    #
    #     instance = self.map.get_by_user(user_id)
    #     if instance:
    #         self.map.update(instance, map_information)
    #     else:
    #         map_information["user_id"] = user_id
    #         self.map.add(map_information)
    #
    #
    #     self_state, apply_id = self.meet.get_user_state_by_apply_and_user(apply_id, user_id)
    #     friend_user_id = self.meet.get_another_user_id(apply_id, user_id)
    #     friend_state, apply_id = self.meet.get_user_state_by_apply_and_user(apply_id, friend_user_id)
    #
    #     if friend_state == PUSH_STATE_TYPE_MEETING:
    #         result = self.push_information(map_information, friend_user_id, user_id, self_state, apply_id,
    #                                        base_url)
    #         OHHOLog.print_log(result)
    #         information = self.return_map_information(friend_user_id, timestamp)
    #         if information.get("information", ""):
    #             information["information"]["apply_id"] = int(apply_id)
    #
    #     result = Result.result_success()
    #     result["data"] = information
    #     return result


    def upload_map_position(self, user_id, map_information, apply_id, base_url, timestamp=0):
        # 上传地图坐标，只保存最新的坐标
        information = dict()
        user = self.user.get_by_id(user_id)
        if user:
            # OHHOLog.print_log("has user")
            if map_information:
                # OHHOLog.print_log(map_information)
                longitude = float(map_information.get("longitude", 0))
                latitude = float(map_information.get("latitude", 0))
                geohash_code = OHHOGeohash.get(latitude, longitude, 6)
                map_information["geohash_code"] = geohash_code
                map_information["timestamp"] = OHHODatetime.get_current_timestamp()
                map_information["user_id"] = user_id
                # OHHOLog.print_log(map_information)
                self.user.set_user_map_information(user.username, map_information)
                self.user.add_user_geo_position(longitude, latitude, user.username)
                self.map.add(map_information)

        self_state, apply_id = self.meet.get_user_state_by_apply_and_user(apply_id, user_id)
        friend_user_id = self.meet.get_another_user_id(apply_id, user_id)
        friend_state, apply_id = self.meet.get_user_state_by_apply_and_user(apply_id, friend_user_id)
        self_state, apply_id = self.meet.get_user_state_by_apply_and_user(apply_id, user_id)

        # if friend_state == PUSH_STATE_TYPE_MEETING or self_state == PUSH_STATE_TYPE_MEETING:
        # result = self.push_information(map_information, friend_user_id, user_id, self_state, apply_id,
        #                                base_url)
        # OHHOLog.print_log(result)

        if friend_state == PUSH_STATE_TYPE_END_MEET or self_state == PUSH_STATE_TYPE_END_MEET:
            information["information"] = {"apply_id": int(apply_id)}
        else:
            information = self.return_map_information(friend_user_id)
            if information.get("information", ""):
                information["information"]["apply_id"] = int(apply_id)
            else:
                information["information"] = {"apply_id": int(apply_id)}

        result = Result.result_success()
        result["data"] = information
        return result
