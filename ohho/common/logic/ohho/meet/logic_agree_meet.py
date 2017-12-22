from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.result import Result
from ohho.common.logic.common.user import User
from ohho.common.logic.common.constant import *
from ohho.common.db.ohho.base.db_ohho_interest import DBOHHOInterest
from Tools.ohho_log import OHHOLog
from Tools.ohho_operation import OHHOOperation
from Tools.ohho_datetime import OHHODatetime
from DB.redis.operation import RedisDB


class LogicAgreeMeet(object):
    def __init__(self):
        self.meet = Meet()
        self.user = User()
        self.interest = DBOHHOInterest()

    def get_name_by_id_from_interest(self, interest_id):
        return self.user.get_interest_name_by_id(interest_id)

    def push_agree(self, to_user_id, user_id, apply_id, base_url, function, type):
        information = self.user.get_basic_user_information(user_id, base_url)
        temp = self.meet.get_countdown(apply_id)
        OHHOLog.print_log(temp)
        information = OHHOOperation.dict_add_dict(information, temp)

        information["apply_id"] = apply_id
        information["function"] = function
        return self.user.push_user_information(to_user_id, type, information)

    def agree_meet(self, user_id, friend_user_id, apply_id, base_url):
        """
        同意见面
        1. 两个人都没有同意的申请
        2. 对方有有效的申请
        :param user_id: 用户ID
        :param friend_user_id: 另一用户ID
        :return:
        """
        user_id = int(user_id)
        friend_user_id = int(friend_user_id)
        apply_id = int(apply_id)

        function = "agree meet"
        apply = self.meet.get_apply_by_id(apply_id)

        result = Result.result_success()
        result["current_timestamp"] = OHHODatetime.get_current_timestamp()

        if apply:
            # 是否有有效的申请
            is_apply_agreeable = self.meet.is_apply_agreeable(apply, user_id)
            if is_apply_agreeable:
                # 本人同意见面
                self.meet.add_agree(apply_id, user_id)

                # 获取另一人的user_id
                another_user_id = apply.one_user_id if apply.another_user_id == user_id else apply.another_user_id
                # 另一人是否同意
                is_another_agreed = self.meet.is_apply_agreed(apply_id, another_user_id)

                if is_another_agreed:
                    OHHOLog.print_log("another agreed: %d" % (another_user_id))
                    one_user_map_data = self.user.get_user_map_information(user_id)
                    another_user_map_data = self.user.get_user_map_information(another_user_id)
                    if one_user_map_data and another_user_map_data:
                        self.meet.add_duplex_agree(one_user_map_data, another_user_map_data, apply_id)
                    # 另一人是否有空（是否见面结束）
                    # is_another_not_free = self.meet.get_apply_id_list_by_user_from_meeting(another_user_id)
                    state, nothing_id = self.meet.get_user_state(another_user_id)
                    OHHOLog.print_log("user state: %d" % (int(state)))
                    if state != PUSH_STATE_TYPE_END_MEET:

                        OHHOLog.print_log("the user is %d, and he is busy" % (another_user_id))
                        OHHOLog.print_log("and his state is %d" % state)
                        # 没空 就把对方的ID写入到双方都同意的redis缓存中
                        self.meet.add_duplex_agree2redis(user_id, another_user_id, apply_id)
                        # self.meet.add_duplex_agree2redis(another_user_id, str(user_id) + "," + str(apply_id))
                    else:
                        OHHOLog.print_log("both agree")
                        # 有空 向双方发送推送
                        type = PUSH_STATE_TYPE_AGREE_MEET
                        OHHOLog.print_log("push %d to %d, apply id is %d" % (another_user_id, user_id, apply_id))
                        result = self.push_agree(user_id, another_user_id, apply_id, base_url, function, type)
                        OHHOLog.print_log(result)

                        OHHOLog.print_log("push %d to %d, apply id is %d" % (user_id, another_user_id, apply_id))
                        result = self.push_agree(another_user_id, user_id, apply_id, base_url, function, type)
                        OHHOLog.print_log(result)

                        # 添加两个人的状态为见面中
                        self.meet.add_meeting(apply_id, user_id)
                        self.meet.add_meeting(apply_id, another_user_id)
                else:
                    OHHOLog.print_log("single agree")
                    type = PUSH_STATE_TYPE_SINGLE_AGREE_MEET
                    OHHOLog.print_log("push %d to %d, apply id is %d" % (user_id, another_user_id, apply_id))
                    result = self.push_agree(another_user_id, user_id, apply_id, base_url, function, type)
                    OHHOLog.print_log(result)

        return result
