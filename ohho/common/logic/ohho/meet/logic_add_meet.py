from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.user import User
from ohho.common.logic.common.result import Result


class LogicAddMeet(object):
    def __init__(self):
        self.meet = Meet()
        self.user = User()

    def add_meet(self, user_id, friend_user_id, address):
        apply = None
        if self.meet.has_valid_apply(user_id, friend_user_id):
            apply = self.meet.get_apply_by_user_and_friend(user_id, friend_user_id)
        else:
            if self.meet.has_valid_apply(friend_user_id, user_id):
                apply = self.meet.get_apply_by_user_and_friend(friend_user_id, user_id)

        if apply:
            agree = self.meet.has_agree(apply.id)
            meet = self.meet.get_meet_by_apply_id(apply.id)
            if meet:
                return Result.result_success("has meet")
            elif agree:
                one_user_map = self.user.get_user_map_information(user_id)
                success = self.meet.add_meet(one_user_map, apply.id)
                if success:
                    return Result.result_success()
                else:
                    return Result.result_failed()
            else:
                return Result.result_failed("still not agree to meet!")
        else:
            return Result.result_failed("no valid apply!")
