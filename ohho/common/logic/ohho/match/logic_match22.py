from ohho.common.db.ohho.match.db_ohho_match_online import DBOHHOMatchOnline
from ohho.common.db.ohho.user.db_ohho_user_accuracy_extension import DBOHHOUserAccuracyExtension
from ohho.common.db.ohho.user.db_ohho_user_favourite_book import DBOHHOUserFavouriteBook
from ohho.common.db.ohho.user.db_ohho_user_favourite_music import DBOHHOUserFavouriteMusic
from ohho.common.db.ohho.user.db_ohho_user_favourite_movie import DBOHHOUserFavouriteMovie
from ohho.common.db.ohho.user.db_ohho_user_favourite_sport import DBOHHOUserFavouriteSport
from ohho.common.db.ohho.record.db_ohho_record_match_apply import DBOHHORecordMatchApply
from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
from ohho.common.db.ohho.relation.db_ohho_user_and_device_relation import DBOHHOUserAndDeviceRelation
from ohho.common.db.ohho.user.db_ohho_user_configuration import DBOHHOUserConfiguration
from ohho.common.db.record.db_ohho_record_exclude import DBOHHORecordExclude
from ohho.common.logic.common.constant import *
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.record.match_condition import MatchCondition
from ohho.common.logic.common.record.user_and_match_condition import UserAndMatchCondition
from ohho.common.logic.common.device import Device
from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.record.friend import Friend
from ohho.common.logic.common.user import User
from ohho.common.logic.ohho.match.logic_get_match_condition import LogicGetMatchCondition
from ohho.common.logic.common.constant import GET_MAP_POSITION_TIMESTAMP_DELTA
from settings import TEST
from Tools.ohho_log import OHHOLog
from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_geohash import OHHOGeohash
from DB.redis.operation import RedisDB

from ohho.common.logic.common.record.constant import *


class LogicMatch(object):
    def __init__(self):
        self.device = Device()
        self.user = User()
        self.meet = Meet()
        self.friend = Friend()
        self.map = DBOHHOMapInformation()
        self.match_condition = LogicGetMatchCondition()
        self.condition = MatchCondition()
        self.condition_relation = UserAndMatchCondition()
        self.device_relation = DBOHHOUserAndDeviceRelation()
        self.user_extension = DBOHHOUserAccuracyExtension()
        self.exclude = DBOHHORecordExclude()
        self.configuration = DBOHHOUserConfiguration()
        self.match_apply = DBOHHORecordMatchApply()
        self.favourite_book = DBOHHOUserFavouriteBook()
        self.favourite_movie = DBOHHOUserFavouriteMovie()
        self.favourite_music = DBOHHOUserFavouriteMusic()
        self.favourite_sport = DBOHHOUserFavouriteSport()
        self.match_online = DBOHHOMatchOnline()

    def get_exclude_user_list(self, user_id):
        created_at = OHHODatetime.get_today_start()
        created_at = OHHODatetime.beijing2utc(created_at)
        one_day_before = OHHODatetime.get_some_hour_after(created_at, -24)
        query = self.exclude.get_query()
        query = self.exclude.get_great_than_equal_created_at(query, one_day_before)
        query1 = self.exclude.get_by_user(query, user_id)
        query2 = self.exclude.get_by_exclude_user(query, user_id)
        if self.exclude.is_empty(query1):
            user1_list = list()
        else:
            user1_list = [exclude.exclude_user_id for exclude in query1]

        if self.exclude.is_empty(query1):
            user2_list = list()
        else:
            user2_list = [exclude.user_id for exclude in query2]
        return list(set(user1_list + user2_list))

    def get_exclude_user_list_up224hour(self, user_id):
        query = self.exclude.get_query()
        query1 = self.exclude.get_by_user(query, user_id)
        query2 = self.exclude.get_by_exclude_user(query, user_id)
        if self.exclude.is_empty(query1):
            user1_list = list()
        else:
            user1_list = [exclude.exclude_user_id for exclude in query1]

        if self.exclude.is_empty(query1):
            user2_list = list()
        else:
            user2_list = [exclude.user_id for exclude in query2]
        user_id_list = list(set(user1_list + user2_list))
        user_id_list_before24hour = self.get_exclude_user_list(user_id)
        return OHHOOperation.list_minus_list(user_id_list, user_id_list_before24hour)

    def get_user_ids_by_device_identities(self, device_ids):
        user_id_list = list()
        for identity in device_ids:
            self.device.set_identity(identity)
            device = self.device.device.get_by_identity()
            if device:
                relation = self.device.relation.get_by_device(device.id)
                if relation:
                    user_id_list.append(relation.user_id)
        return list(set(user_id_list))

    def get_condition(self, user_id, name):
        result, query = self.match_condition.get(user_id, name)
        return query

    def get_user_accuracy_extension(self, user_id_list):
        return self.user_extension.get_by_user_list(user_id_list)

    # **************************************************************** VERSION 2 *************************
    def clear_secondary_device(self, device_list):
        result = list()
        for d in device_list:
            d = d.strip()
            if d:
                self.device.set_identity(d)
                device = self.device.get_by_identity()
                if device:
                    relation = self.device_relation.get_by_device(device.id)
                    if relation and relation.type == 1:
                        result.append(d)
        return result

    def match_by_condition_version2(self, user_id, user_id_list):
        # 根据user_id获取配对条件
        # 根据user_id_list获取配对用户列表
        # 根据条件从用户列表中配对

        # result = user_id_list
        # return result

        result = list()
        condition = self.condition_relation.get_nearest_match_relation_by_user(user_id)
        if condition:
            match_condition = self.condition.get_by_id(condition.match_condition_id)
            if match_condition:
                query = self.user_extension.get_by_user_list(user_id_list)

                sex = match_condition.sex
                if sex and sex != 3:
                    query = self.user_extension.get_by_sex(query, sex)

                small_age = match_condition.small_age
                big_age = match_condition.big_age
                if small_age and big_age:
                    this_year = OHHODatetime.get_now().year
                    small_age_year = this_year - small_age
                    big_age_year = this_year - big_age

                    big_age_year_start = str(big_age_year) + "-1-1"
                    date_big_age_year_start = OHHODatetime.string2date(big_age_year_start)
                    small_age_year_end = str(small_age_year) + "-1-1"
                    date_small_age_year_end = OHHODatetime.string2date(small_age_year_end)
                    query = self.user_extension.find_by_birthday(query, date_big_age_year_start,
                                                                 date_small_age_year_end)
                if self.user_extension.is_empty(query):
                    pass
                else:
                    result = [ue.user_id for ue in query]
        return result

    def duplex_match(self, user_id, user_id_list):
        result = list()
        OHHOLog.print_log(user_id_list)
        user_id_list = self.match_by_condition_version2(user_id, user_id_list)
        for uid in user_id_list:
            temp = self.match_by_condition_version2(uid, [user_id])
            if temp:
                result.append(uid)
        return result

    #  compute start
    def compute_online_user(self, user_id_list):
        online_id_list = list()
        for user_id in user_id_list:
            if self.is_match_online(user_id):
                online_id_list.append(user_id)
        return online_id_list

    def compute_favourite_book(self, user_id, another_user_id):
        query = self.favourite_book.get_query()
        user_query = self.favourite_book.get_by_user(query, user_id)
        another_user_query = self.favourite_book.get_by_user(query, another_user_id)
        user_book_isbn = [book.isbn for book in user_query]
        another_user_isbn = [book.isbn for book in another_user_query]
        result = list(OHHOOperation.set_intersect_set(set(user_book_isbn), set(another_user_isbn)))
        return result

    def compute_favourite_movie(self, user_id, another_user_id):
        query = self.favourite_movie.get_query()
        user_query = self.favourite_movie.get_by_user(query, user_id)
        another_user_query = self.favourite_movie.get_by_user(query, another_user_id)
        user_movie_id = [movie.movie_id for movie in user_query]
        another_user_movie_id = [movie.movie_id for movie in another_user_query]
        result = list(OHHOOperation.set_intersect_set(set(user_movie_id), set(another_user_movie_id)))
        return result

    def compute_favourite_music(self, user_id, another_user_id):
        query = self.favourite_music.get_query()
        user_query = self.favourite_music.get_by_user(query, user_id)
        another_user_query = self.favourite_music.get_by_user(query, another_user_id)
        user_music_id = [music.music_id for music in user_query]
        another_user_music_id = [music.music_id for music in another_user_query]
        result = list(OHHOOperation.set_intersect_set(set(user_music_id), set(another_user_music_id)))
        return result

    def compute_favourite_sport(self, user_id, another_user_id):
        query = self.favourite_sport.get_query()
        user_query = self.favourite_sport.get_by_user(query, user_id)
        another_user_query = self.favourite_sport.get_by_user(query, another_user_id)
        user_sport_id = [sport.sport_id for sport in user_query]
        another_user_sport_id = [sport.sport_id for sport in another_user_query]
        result = list(OHHOOperation.set_intersect_set(set(user_sport_id), set(another_user_sport_id)))
        return result

    def compute_get_total_count(self, user_id, another_user_id):
        book = self.compute_favourite_book(user_id, another_user_id)
        movie = self.compute_favourite_movie(user_id, another_user_id)
        music = self.compute_favourite_music(user_id, another_user_id)
        sport = self.compute_favourite_sport(user_id, another_user_id)
        total_length = len(book) + len(movie) + len(music) + len(sport)
        return total_length, book, movie, music, sport

    def compute_main(self, user_id, user_id_list):
        result = 0
        current_length = 0
        online_user_list = self.compute_online_user(user_id_list)
        for another_user_id in online_user_list:
            temp_length, book, movie, music, sport = self.compute_get_total_count(user_id, another_user_id)
            if current_length < temp_length:
                current_length = temp_length
                result = another_user_id
        return result

    # compute end


    def is_in_meeting(self, user_id):
        # 获取见面中表的有效申请列表
        # 只有取消（两方自动结束）和结束时meeting才会结束（和实际的见面后结束有区别）
        return self.meet.get_apply_id_list_by_user_from_meeting(user_id)

    def has_duplex_agree(self, user_id, user_id_list, base_url):
        result = False
        redis_name = REDIS_DUPLEX_AGREE_PREFIX + str(user_id)
        duplex_agree_user_ids = RedisDB.list_get_all(redis_name)
        duplex_agree_user_ids = [RedisDB.to_bytes(data) for data in duplex_agree_user_ids]
        for the_user_id in duplex_agree_user_ids:
            the_user_id = str(the_user_id)
            OHHOLog.print_log(the_user_id)
            some_user_id, apply_id = the_user_id.split(",")
            some_user_id = int(some_user_id)
            apply_id = int(apply_id)
            if some_user_id in user_id_list:
                state = self.meet.get_user_state_by_user(some_user_id)
                if not result and state == PUSH_STATE_TYPE_END_MEET:
                    information = self.user.get_push_user_information(some_user_id, apply_id, base_url)
                    self.user.push_user_information(user_id, PUSH_STATE_TYPE_AGREE_MEET, information)
                    information = self.user.get_push_user_information(user_id, apply_id, base_url)
                    self.user.push_user_information(some_user_id, PUSH_STATE_TYPE_AGREE_MEET, information)

                    # 添加两个人的状态为见面中
                    self.meet.add_meeting(apply_id, user_id)
                    self.meet.add_meeting(apply_id, the_user_id)

                    result = True
                else:
                    RedisDB.list_left_push(redis_name, the_user_id)
        return result

    def is_match_open(self, user_id):
        configuration = self.configuration.get_by_user(user_id)
        return configuration.is_match

    def clear_by_is_match(self, user_id_list):
        result = list()
        for user_id in user_id_list:
            if self.is_match_open(user_id):
                result.append(user_id)
        return result

    def add_apply(self, user_id, match_user_id):
        the_apply = self.meet.get_nearest_apply_by_user_and_another_user(user_id, match_user_id)
        the_reverse_apply = self.meet.get_nearest_apply_by_user_and_another_user(match_user_id, user_id)
        if the_apply or the_reverse_apply:
            is_time_valid = self.meet.is_valid_apply(the_apply)
            reverse_is_time_valid = self.meet.is_valid_apply(the_reverse_apply)
            if is_time_valid or reverse_is_time_valid:
                return None

        relation1 = self.condition_relation.get_nearest_match_relation_by_user(user_id)
        relation2 = self.condition_relation.get_nearest_match_relation_by_user(match_user_id)
        self.meet.add_apply(user_id, match_user_id, relation1.match_condition_id,
                            relation2.match_condition_id)
        return self.meet.get_nearest_apply_by_user_and_another_user(user_id, match_user_id)

    def parse_intersection(self, intersection):
        result = list()
        for the_id in intersection:
            name = self.user.get_interest_name_by_id(the_id)
            if name:
                result.append(name)
        return result

    def push_information(self, to_user_id, user_id, apply_id, base_url):
        information = self.user.get_basic_user_information(user_id, base_url)
        information["apply_id"] = apply_id
        information["user_id"] = user_id
        return self.user.push_user_information(to_user_id, PUSH_STATE_TYPE_APPLY_MEET, information)

    # 清除见面但没有结束的人
    def clear_by_met_not_end(self, user_id_list):
        result = list()
        for user_id in user_id_list:
            state = self.meet.get_user_state_by_user(user_id)
            if state in (PUSH_STATE_TYPE_MEETING, PUSH_STATE_TYPE_SINGLE_MEET, PUSH_STATE_TYPE_MET):
                continue
            result.append(user_id)
        return result

    def clear_by_meet_in24hour(self, user_id, user_id_list):
        meet_in24hour_user_ids = self.meet.get_meet_in24hour_user_ids(user_id)
        OHHOLog.print_log("meet in 24 hour")
        OHHOLog.print_log(meet_in24hour_user_ids)
        return OHHOOperation.list_minus_list(user_id_list, meet_in24hour_user_ids)

    def clear_by_friend(self, user_id, user_id_list):
        friends = self.friend.get_valid_by_account(user_id)
        friend_user_id_list = [f.friend_account_id for f in friends]
        return OHHOOperation.list_minus_list(user_id_list, friend_user_id_list)

    def sorted_by_rules(self, user_id, user_id_list):
        # 24小时内见过面的人
        # 24小时前被拒绝过的或拒绝过我的人
        user_id_not_meet = list()
        user_id_exclude = list()
        user_id_meet = list()
        meet_in24hour_user_ids = self.meet.get_meet_in24hour_user_ids(user_id)
        exclude_before24hour_user_ids = self.get_exclude_user_list_up224hour(user_id)
        for the_user_id in user_id_list:
            if the_user_id in meet_in24hour_user_ids:
                user_id_meet.append(the_user_id)
            elif the_user_id in exclude_before24hour_user_ids:
                user_id_exclude.append(the_user_id)
            else:
                user_id_not_meet.append(the_user_id)
        return user_id_not_meet + user_id_exclude + user_id_meet

    def has_valid_apply(self, user_id):
        valid_timestamp = self.match_apply.get_valid_timestamp()
        query = self.match_apply.get_query()
        query = self.match_apply.get_great_than_equal_timestamp(query, valid_timestamp)
        apply1 = self.match_apply.get_by_one_user(query, user_id)
        apply1 = self.match_apply.order_by_id_desc(apply1)
        apply1_first = self.match_apply.first(apply1)
        apply2 = self.match_apply.get_by_another_user(query, user_id)
        apply2 = self.match_apply.order_by_id_desc(apply2)
        apply2_first = self.match_apply.first(apply2)

        if apply1_first and apply2_first:
            the_apply = apply1_first if apply1_first.timestamp > apply2_first.timestamp else apply2_first
        elif apply1_first:
            the_apply = apply1_first
        else:
            the_apply = apply2_first

        return self.meet.is_the_apply_valid(the_apply), the_apply.id if the_apply else 0

    def clear_outdated_user(self):
        timestamp = OHHODatetime.get_current_timestamp()
        timestamp = timestamp - 1 * 60 * 1000
        query = self.match_online.get_query()
        delete_query = self.match_online.get_less_than_timestamp(query, timestamp)
        success = self.match_online.delete_some(delete_query)
        if success:
            OHHOLog.print_log(Result.result_success("clear online outdated user"))
        else:
            OHHOLog.print_log(Result.result_failed("clear online outdated user"))

    def update_match_online(self, user_id):
        timestamp = OHHODatetime.get_current_timestamp()
        instance = self.match_online.get_by_user(user_id)
        if instance:
            success = self.match_online.update(instance, {"timestamp": timestamp})
            if success:
                OHHOLog.print_log(Result.result_success("update online for user %d" % (int(user_id))))
            else:
                OHHOLog.print_log(Result.result_failed("update online for user %d" % (int(user_id))))
        else:
            success = self.match_online.add({"user_id": user_id})
            if success:
                OHHOLog.print_log(Result.result_success("add online for user %d" % (int(user_id))))
            else:
                OHHOLog.print_log(Result.result_failed("add online for user %d" % (int(user_id))))

    def is_match_online(self, user_id):
        instance = self.match_online.get_by_user(user_id)
        if instance:
            return True
        else:
            return False

    def has_nickname(self, user_id):
        user_extension = self.user_extension.get_by_user(user_id)
        if user_extension and user_extension.nickname:
            return True
        else:
            return False

    def match_version22(self, user_id, device_list_string, base_url, identity_id=None):
        # 查看本人是否打开了配对开关
        # 查看本人状态是否在见面中
        # 查看本人状态是否是有有效的配对
        # 清除不是交友设备的设备（type=1是交友设备）
        # 根据device_list得到用户id_list
        # 过滤掉今天匹配并不中意的人
        # 过滤掉未打开匹配开关的人
        # 过滤掉正在见面的人
        # 过滤掉已经见面但还没有结束的人
        # 过滤掉24小时内见过面的人
        # 过滤掉是好友的人
        # 根据性别和年龄区间筛选用户列表，根据条件找出符合条件的用户列表
        # 从符合条件的用户列表中依次根据用户ID获取配对条件， 根据配对条件看当前用户是否符合条件
        # 将第一个符合条件的用户添加到申请表中，并向两个人发送推送（推送对方的个人信息和推送的类型，这里是申请见面）
        user_id = int(user_id)
        self.clear_outdated_user()
        self.update_match_online(user_id)

        if not self.has_nickname(user_id):
            return Result.result_failed("please add nickname firstly!")

        if user_id and identity_id:
            OHHOLog.print_log(user_id)
            OHHOLog.print_log(identity_id)
            self.device.set_identity(identity_id)
            device = self.device.get_by_identity()
            if device:
                relations = self.device_relation.get_valid_by_device(device.id)
                the_relation = self.device_relation.first(relations)
                if the_relation and the_relation.user_id == user_id:
                    pass
                else:
                    information = "no device and user relation, you have no right to match!"
                    OHHOLog.print_log(information)
                    # return Result.result_failed(information)
            else:
                information = "no such device, you have no right to match!"
                OHHOLog.print_log(information)
                # return Result.result_failed(information)
        else:
            if user_id:
                information = "user %d is invalid, you have no right to match!" % user_id
                OHHOLog.print_log(information)
                # return Result.result_failed(information)
            else:
                information = "user or device is invalid, you have no right to match!"
                OHHOLog.print_log(information)
                # return Result.result_failed(information)

        is_match = self.is_match_open(user_id)
        if not is_match:
            OHHOLog.print_log("%d match switch closed!" % user_id)
            return Result.result_failed("please open match switch!")

        if self.is_in_meeting(user_id):
            OHHOLog.print_log("%d is in meeting" % user_id)
            return Result.result_failed("you are still in meeting!")
        OHHOLog.print_log("%d is not in meeting" % user_id)

        has_valid_apply, the_apply_id = self.has_valid_apply(user_id)
        if has_valid_apply:
            return Result.result_failed("you have matched with somebody: %d" % the_apply_id)
        OHHOLog.print_log("%d has no valid apply" % user_id)

        exclude_user_id_list = self.get_exclude_user_list(user_id)

        device_list = device_list_string.split(",")
        if "" in device_list:
            device_list.remove("")
        OHHOLog.print_log("source:")
        OHHOLog.print_log(device_list)
        device_list = self.clear_secondary_device(device_list)
        OHHOLog.print_log("clear secondary device:")
        OHHOLog.print_log(device_list)
        user_id_list = list()
        for identity in device_list:
            self.device.set_identity(identity)
            relation = self.device.get_relation_by_device()
            if relation:
                user_id_list.append(relation.user_id)
        OHHOLog.print_log("get user list")
        OHHOLog.print_log(user_id_list)
        OHHOLog.print_log("exclude user id list")
        OHHOLog.print_log(exclude_user_id_list)
        if user_id_list:
            user_id_list = OHHOOperation.list_minus_list(user_id_list, exclude_user_id_list)
            OHHOLog.print_log("clear exclude user")
            OHHOLog.print_log(user_id_list)

            user_id_list = self.clear_by_is_match(user_id_list)
            OHHOLog.print_log("clear match switch close user")
            OHHOLog.print_log(user_id_list)

            OHHOLog.print_log("clear self user")
            if user_id in user_id_list:
                user_id_list.remove(user_id)
            OHHOLog.print_log(user_id_list)
        else:
            return Result.result_success()

        if user_id_list:
            meeting_user_id_list = self.meet.get_meeting_user_ids()
            OHHOLog.print_log("meeting user id list")
            OHHOLog.print_log(meeting_user_id_list)
            user_id_list = OHHOOperation.list_minus_list(user_id_list, meeting_user_id_list)
            OHHOLog.print_log("clear meeting user")
            OHHOLog.print_log(user_id_list)
        else:
            return Result.result_success()

        if user_id_list:
            user_id_list = self.clear_by_met_not_end(user_id_list)
            OHHOLog.print_log("clear met but not end")
            OHHOLog.print_log(user_id_list)
        else:
            return Result.result_success()

        if user_id_list:
            user_id_list = self.clear_by_meet_in24hour(user_id, user_id_list)
            OHHOLog.print_log("clear meet in 24 hours")
            OHHOLog.print_log(user_id_list)
        else:
            return Result.result_success()

        if user_id_list:
            user_id_list = self.clear_by_friend(user_id, user_id_list)
            OHHOLog.print_log("clear friend")
            OHHOLog.print_log(user_id_list)
        else:
            return Result.result_success()

        if user_id_list:
            has_duplex_agree = self.has_duplex_agree(user_id, user_id_list, base_url)
            if has_duplex_agree:
                return Result.result_success()
            else:
                user_id_list = self.duplex_match(user_id, user_id_list)
                OHHOLog.print_log(user_id_list)

                if user_id_list:
                    match_user_id = self.compute_main(user_id, user_id_list)
                    # OHHOLog.print_log("matched user list:")
                    # OHHOLog.print_log(matched_user_list)
                    #
                    # matched_user_list = self.sorted_by_rules(user_id, matched_user_list)
                    # user_tuple = matched_user_list[0]
                    # match_user_id = user_tuple[2]
                    # primary = user_tuple[3]
                    # secondary = user_tuple[4]
                    if match_user_id:
                        the_apply = self.add_apply(user_id, match_user_id)
                        if the_apply:
                            OHHOLog.print_log(self.push_information(user_id, match_user_id, the_apply.id, base_url))
                            OHHOLog.print_log(self.push_information(match_user_id, user_id, the_apply.id, base_url))
                        else:
                            OHHOLog.print_log("has valid apply!")
            return Result.result_success()
