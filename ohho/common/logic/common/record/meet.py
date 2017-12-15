from ohho.common.db.ohho.record.db_ohho_record_match_apply import DBOHHORecordMatchApply
from ohho.common.db.ohho.record.db_ohho_record_match_agree import DBOHHORecordMatchAgree
from ohho.common.db.ohho.record.db_ohho_record_match_duplex_agree import DBOHHORecordMatchDuplexAgree
from ohho.common.db.ohho.record.db_ohho_record_match_refuse import DBOHHORecordMatchRefuse
from ohho.common.db.ohho.record.db_ohho_record_match_meet import DBOHHORecordMatchMeet
from ohho.common.db.ohho.record.db_ohho_record_match_met import DBOHHORecordMatchMet
from ohho.common.db.ohho.record.db_ohho_record_match_meeting import DBOHHORecordMatchMeeting
from ohho.common.db.ohho.record.db_ohho_record_exclude import DBOHHORecordExclude
from ohho.common.db.ohho.record.db_ohho_record_match_meet_end import *

from ohho.common.logic.common.record.constant import *
from ohho.common.logic.common.constant import *
from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_log import OHHOLog
from DB.redis.operation import RedisDB


class Meet(object):
    def __init__(self):
        self.apply = DBOHHORecordMatchApply()
        self.agree = DBOHHORecordMatchAgree()
        self.duplex_agree = DBOHHORecordMatchDuplexAgree()
        self.refuse = DBOHHORecordMatchRefuse()
        self.meet = DBOHHORecordMatchMeet()
        self.met = DBOHHORecordMatchMet()
        self.meeting = DBOHHORecordMatchMeeting()
        self.meet_end = DBOHHORecordMatchMeetEnd()
        self.exclude = DBOHHORecordExclude()

    def get_applies_by_time_delta(self, time_delta=-24):
        now = OHHODatetime.get_utc_now()
        the_datetime = OHHODatetime.get_some_hour_after(now, time_delta)
        query = self.apply.get_query()
        return self.apply.get_great_than_equal_created_at(query, the_datetime)

    def get_apply_id_list_by_user_from_meeting(self, user_id):
        query = self.meeting.get_query()
        query = self.meeting.get_valid(query, True)
        return self.meeting.get_apply_id_list_by_user(query, user_id)

    def is_valid_apply(self, instance):
        return self.apply.is_valid_instance(instance)

    def is_apply_meet_end(self, apply_id):
        return self.meet_end.get_by_apply(apply_id)

    def get_apply_by_id(self, apply_id):
        return self.apply.get_by_id(apply_id)

    def get_meet_by_apply_id(self, apply_id):
        return self.meet.get_by_apply(apply_id)

    def get_apply_state(self, apply):
        if apply:
            # 请求见面结束
            meet_end = self.is_apply_meet_end(apply.id)
            if meet_end:
                # 返回结束状态码
                return meet_end.type

            nearest_refuse = self.refuse.get_nearest_refuse(apply.id)
            if nearest_refuse:
                # 拒绝了
                self.meet_end.add_refuse(apply.id)
                return MEET_END_TYPE_REFUSE
            else:
                is_meet = self.is_meet(apply.one_user_id, apply.another_user_id)
                if is_meet:
                    # 没有拒绝， 见过面了
                    # OHHOLog.print_log("has meet")
                    return APPLY_MEET_BUT_NOT_END
                else:
                    nearest_agree = self.agree.get_nearest_agree(apply.id)
                    if nearest_agree:
                        if self.agree.is_valid_instance(nearest_agree):
                            # OHHOLog.print_log("agree and not meet OK")
                            # 同意啦，没见过面，并且没有过期，没有结束
                            return APPLY_AGREE_BUT_NOT_MEET
                        else:
                            self.meet_end.add_agree_timeout(apply.id)
                            return MEET_END_TYPE_AGREE_TIMEOUT
                    else:
                        is_valid_apply = self.apply.is_valid_instance(apply)
                        if is_valid_apply:
                            # OHHOLog.print_log("OK")
                            # 没有见面，没有同意，没有超时， 有效
                            return APPLY_VALID_NOT_AGREE
                        else:
                            # 没有见面，没有同意，超时啦，无效
                            # OHHOLog.print_log("timeout")
                            self.meet_end.add_apply_timeout(apply.id)
                            return MEET_END_TYPE_APPLY_TIMEOUT
        else:
            # OHHOLog.print_log("no apply!")
            return APPLY_NOT_EXIST

    def has_valid_apply(self, user_id, friend_user_id):
        """
        获取最新的有效申请
        如果拒绝，申请无效；如果见面了，申请无效；否则， 有效。
        :param user_id:
        :param friend_user_id:
        :return:
        """
        apply = self.get_apply_by_user_and_friend(user_id, friend_user_id)
        if apply:
            # meet_end = self.meet_end.get_by_apply(apply.id)
            # if meet_end:
            #     return False

            # OHHOLog.print_log(apply.id)
            nearest_refuse = self.refuse.get_nearest_refuse(apply.id)
            if nearest_refuse:
                # 拒绝了
                # OHHOLog.print_log("refuse")
                return False
            else:
                is_meet = self.is_meet(user_id, friend_user_id)
                if is_meet:
                    # 没有拒绝， 见过面了
                    # OHHOLog.print_log("has meet")
                    return False
                else:
                    nearest_agree = self.agree.get_nearest_agree(apply.id)
                    if nearest_agree:
                        # OHHOLog.print_log("agree and not meet OK")
                        # 同意啦，没见过面，有效
                        return True
                    else:
                        is_valid_apply = self.apply.is_valid_instance(apply)
                        if is_valid_apply:
                            # OHHOLog.print_log("OK")
                            # 没有见面，没有同意，没有超时， 有效
                            return True
                        else:
                            # 没有见面，没有同意，超时啦，无效
                            # OHHOLog.print_log("timeout")
                            return False
        else:
            # OHHOLog.print_log("no apply!")
            pass
        return False

    def has_agree(self, apply_id):
        if self.agree.get_nearest_agree(apply_id):
            return True
        else:
            return False

    def has_refuse(self, apply_id):
        if self.refuse.get_nearest_refuse(apply_id):
            return True
        else:
            return False

    def has_agree_apply(self, user_id):
        applies = self.get_apply_by_user(user_id)
        for apply in applies:
            if self.apply.is_valid_instance(apply):
                agree = self.agree.get_nearest_agree(apply.id)
                refuse = self.refuse.get_nearest_refuse(apply.id)
                if not refuse and agree:
                    return True
        reverse_applies = self.get_apply_by_friend(user_id)
        for apply in reverse_applies:
            if self.apply.is_valid_instance(apply):
                agree = self.agree.get_nearest_agree(apply.id)
                refuse = self.refuse.get_nearest_refuse(apply.id)
                if not refuse and agree:
                    return True
        return False

    def is_meet_by_apply(self, apply_id):
        # if TEST:
        #     return False
        # else:
        apply = self.meet.get_by_apply(apply_id)
        if apply:
            return True
        else:
            return False

    def is_meet(self, user_id, friend_user_id):
        # if TEST:
        #     return False
        # else:
        apply = self.get_apply_by_user_and_friend(user_id, friend_user_id)

        if apply:
            # OHHOLog.print_log(apply.id)
            the_meet = self.meet.get_by_apply(apply.id)
            if the_meet:
                # OHHOLog.print_log(the_meet.id)
                return True
        else:
            apply = self.get_apply_by_user_and_friend(friend_user_id, user_id)
            if apply:
                # OHHOLog.print_log(apply.id)
                the_meet = self.meet.get_by_apply(apply.id)
                if the_meet:
                    # OHHOLog.print_log(the_meet.id)
                    return True
        return False

    def get_apply_by_user(self, user_id):
        query = self.apply.get_query()
        # OHHOLog.print_log(query.count())
        return self.apply.get_by_one_user(query, user_id)

    def get_apply_by_friend(self, friend_user_id):
        query = self.apply.get_query()
        return self.apply.get_by_another_user(query, friend_user_id)

    def get_apply_by_user_and_friend(self, user_id, friend_user_id):
        query = self.get_apply_by_user(user_id)
        # OHHOLog.print_log(query.count())
        # OHHOLog.print_log("user_id=%d" % user_id)
        # OHHOLog.print_log("friend_user_id=%d" % friend_user_id)
        query = self.apply.get_by_another_user(query, friend_user_id)

        query = self.apply.order_by_id_desc(query)
        # OHHOLog.print_log(query.count())
        return self.apply.first(query)

    def get_nearest_apply_without_sequence(self, user_id):
        user = self.get_apply_by_user(user_id)
        user = self.apply.order_by_id_desc(user)
        user_first = self.apply.first(user)
        friend = self.get_apply_by_friend(user_id)
        friend = self.apply.order_by_id_desc(friend)
        friend_first = self.apply.first(friend)
        if user_first and friend_first:
            if user_first.timestamp < friend_first.timestamp:
                return friend_first
            else:
                return user_first
        elif user_first:
            return user_first
        else:
            return friend_first

    def get_nearest_apply_by_user_and_another_user(self, user_id, another_user_id):
        query = self.apply.get_query()
        query = self.apply.get_by_one_user(query, user_id)
        query = self.apply.get_by_another_user(query, another_user_id)
        query = self.apply.order_by_id_desc(query)
        return self.apply.first(query)

    def add_apply(self, user_id, friend_user_id, one_user_match_condition_id=None,
                  another_user_match_condition_id=None):
        data = dict()
        data["one_user_id"] = user_id
        data["another_user_id"] = friend_user_id
        data["one_user_match_condition_id"] = one_user_match_condition_id
        data["another_user_match_condition_id"] = another_user_match_condition_id
        return self.apply.add(data)

    def add_agree(self, apply_id, user_id):
        # OHHOLog.print_log(apply_id)
        # OHHOLog.print_log(user_id)
        data = dict()
        data["apply_id"] = apply_id
        data["user_id"] = user_id
        return self.agree.add(data)

    def add_duplex_agree(self, one_user_dict, another_user_dict, apply_id):
        data = dict()
        data["user_id"] = one_user_dict["user_id"]
        data["user_longitude"] = one_user_dict["longitude"]
        data["user_latitude"] = one_user_dict["latitude"]
        data["user_address"] = one_user_dict["address"]

        data["another_user_id"] = another_user_dict["user_id"]
        data["another_user_longitude"] = another_user_dict["longitude"]
        data["another_user_latitude"] = another_user_dict["latitude"]
        data["another_user_address"] = another_user_dict["address"]

        data["apply_id"] = apply_id
        return self.duplex_agree.add(data)

    def add_refuse(self, apply_id, user_id):
        data = dict()
        data["apply_id"] = apply_id
        data["user_id"] = user_id
        return self.refuse.add(data)

    def add_exclude(self, user_id, exclude_user_id):
        data = dict()
        data["user_id"] = user_id
        data["exclude_user_id"] = exclude_user_id
        return self.exclude.add(data)

    def add_meet(self, one_user_map, apply_id):
        data = one_user_map
        data["apply_id"] = apply_id
        return self.meet.add(data)

    def add_meeting(self, apply_id, user_id, address=None):
        data = dict()
        data["apply_id"] = apply_id
        data["user_id"] = user_id
        if address:
            data["address"] = address
        return self.meeting.add(data)

    def delete_meeting(self, apply_id, user_id):
        instance = self.meeting.get_valid_by_apply_and_user(apply_id, user_id)
        if instance:
            return self.meeting.delete(instance, True)
        return True

    def add_meet_end(self, apply_id, user_id, address):
        data = dict()
        data["apply_id"] = apply_id
        data["user_id"] = user_id
        data["address"] = address
        return self.meet_end.add(data)

    def add_met(self, data):
        return self.met.add(data)

    def get_meet(self, user_id, last_id):
        last_id = int(last_id)
        met_query = self.get_met_list(user_id)
        met_query = self.met.order_by_id_desc(met_query)
        if last_id > 0:
            met_query = self.met.less_than(met_query, last_id)
        return met_query

    def get_meet_user_ids(self, user_id):
        meet1 = self.met.get_by_user(user_id)
        user1_id_list = [m.another_user_id for m in meet1]
        meet2 = self.met.get_by_another_user(user_id)
        user2_id_list = [m.user_id for m in meet2]
        return list(set(user1_id_list + user2_id_list))

    def get_meet_in24hour_user_ids(self, user_id):
        current = OHHODatetime.get_now()
        current_utc = OHHODatetime.beijing2utc(current)
        current_utc_before24hour = OHHODatetime.get_some_hour_after(current_utc, -24)
        query = self.met.get_query()
        query = self.met.get_great_than_equal_created_at(query, current_utc_before24hour)
        query1 = self.met.get_by_user_id(query, user_id)
        user1_id_list = [m.another_user_id for m in query1]
        query2 = self.met.get_by_another_user_id(query, user_id)
        user2_id_list = [m.user_id for m in query2]
        return list(set(user2_id_list + user1_id_list))

    def get_meeting_user_ids(self):
        query = self.meeting.get_query()
        query = self.meeting.get_valid(query, True)
        if self.meeting.is_empty(query):
            return list()
        else:
            return [m.user_id for m in query]

    def is_apply_agreed(self, apply_id, user_id):
        query = self.agree.filter_by_apply(apply_id)
        query = self.agree.filter_by_user(query, user_id)
        nearest = self.agree.get_nearest(query)
        if nearest:
            return True
        return False

    def is_apply_refused(self, apply_id):
        query = self.refuse.filter_by_apply(apply_id)
        if self.refuse.is_empty(query):
            return False
        return True

    def is_apply_agreeable(self, apply, user_id):
        # OHHOLog.print_log(user_id)
        if not apply:
            return False

        # OHHOLog.print_log(user_id)
        is_time_valid = self.apply.is_valid_instance(apply)
        if not is_time_valid:
            return False

        # OHHOLog.print_log(user_id)
        is_self_agreed = self.is_apply_agreed(apply.id, user_id)
        if is_self_agreed:
            return False

        # OHHOLog.print_log(user_id)
        is_refused = self.is_apply_refused(apply.id)
        if is_refused:
            return False

        # OHHOLog.print_log(user_id)
        return True

    def add_duplex_agree2redis(self, user_id, another_user_id, apply_id):
        name1 = REDIS_DUPLEX_AGREE_PREFIX + str(user_id)
        name2 = REDIS_DUPLEX_AGREE_PREFIX + str(another_user_id)
        RedisDB.list_left_push(name1, str(another_user_id) + "," + str(apply_id))
        RedisDB.list_left_push(name2, str(user_id) + "," + str(apply_id))

    def is_apply_in_meeting(self, apply_id, user_id):
        if apply_id and user_id:
            the_meeting = self.meeting.get_valid_by_apply_and_user(apply_id, user_id)
            if the_meeting:
                return True
            else:
                return False
        return False

    def get_another_user_id(self, apply_id, user_id):
        apply = self.apply.get_by_id(apply_id)
        if apply:
            return apply.one_user_id if apply.another_user_id == int(user_id) else apply.another_user_id
        return None

    def is_met(self, apply_id):
        met = self.met.get_by_apply(apply_id)
        if met:
            return True
        else:
            return False

    def is_meet_end(self, apply_id, user_id):
        meet_end = self.meet_end.get_by_apply_and_user(apply_id, user_id)
        if meet_end:
            return True
        else:
            return False

    def get_met_by_users(self, user_id, another_user_id):
        met = self.met.get_by_users(user_id, another_user_id)
        if met:
            return met
        else:
            met = self.met.get_by_users(another_user_id, user_id)
            return met

    def get_user_meet(self, apply_id, friend_user_id):
        return self.meet.get_by_apply_and_user(apply_id, friend_user_id)

    def get_met_list(self, user_id):
        return self.met.get_met_list(user_id)

    def get_user_state_by_user(self, user_id):
        apply_id = 0
        state = PUSH_STATE_TYPE_END_MEET
        query_meet = self.meet.get_valid_and_nearest_by_user(user_id)
        if query_meet:
            apply_id = query_meet.apply_id
            # OHHOLog.print_log(query_meet.apply_id)
            # OHHOLog.print_log(user_id)
            query_meet_end = self.meet_end.get_by_apply_and_user(apply_id, user_id)
            # OHHOLog.print_log(query_meet_end)
            apply = self.apply.get_by_id(apply_id)
            friend_user_id = 0
            if apply:
                friend_user_id = apply.another_user_id if apply.one_user_id == int(user_id) else apply.one_user_id
            friend_meet = self.meet.get_by_apply_and_user(apply_id, friend_user_id)
        else:
            query_meet_end = None
            friend_meet = None
        query_meeting = self.meeting.get_valid_and_nearest_by_user(user_id)

        if query_meeting:
            apply_id = query_meeting.apply_id
            # OHHOLog.print_log(apply_id)
            state = PUSH_STATE_TYPE_MEETING
        elif not query_meet_end:
            if query_meet:
                apply_id = query_meet.apply_id
            if friend_meet and query_meet:
                # OHHOLog.print_log(apply_id)
                # OHHOLog.print_log(friend_meet)
                # OHHOLog.print_log(query_meet)
                state = PUSH_STATE_TYPE_MET
            elif query_meet:
                state = PUSH_STATE_TYPE_SINGLE_MEET

        return state, apply_id

    def get_user_state_by_apply_and_user(self, apply_id, user_id):
        state = PUSH_STATE_TYPE_END_MEET
        apply = self.apply.get_by_id(apply_id)
        friend_user_id = 0
        if apply:
            friend_user_id = apply.another_user_id if apply.one_user_id == int(user_id) else apply.one_user_id
        query_meeting = self.meeting.get_valid_by_apply_and_user(apply_id, user_id)
        if query_meeting:
            state = PUSH_STATE_TYPE_MEETING
        else:
            query_meet = self.meet.get_by_apply_and_user(apply_id, user_id)
            friend_meet = self.meet.get_by_apply_and_user(apply_id, friend_user_id)
            query_meet_end = self.meet_end.get_by_apply_and_user(apply_id, user_id)
            if not query_meet_end:
                if query_meet and friend_meet:
                    state = PUSH_STATE_TYPE_MET
                elif query_meet:
                    state = PUSH_STATE_TYPE_SINGLE_MEET
            else:
                state = PUSH_STATE_TYPE_END_MEET

        return state, apply_id

    def get_user_state(self, user_id, apply_id=0):
        if apply_id:
            state, apply_id = self.get_user_state_by_apply_and_user(apply_id, user_id)
        else:
            state, apply_id = self.get_user_state_by_user(user_id)
        return state, apply_id
