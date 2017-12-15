from ohho.common.logic.common.record.meet import Meet as RecordMeet
from ohho.common.logic.common.record.friend import Friend
from ohho.common.logic.common.im.netease.friend import Friend as IMFriend
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog


class LogicApplyFriend(object):
    def __init__(self):
        self.friend = Friend()
        self.im_friend = IMFriend()
        self.record_meet = RecordMeet()

    def apply_friend(self, user_id, friend_user_id, apply_id):
        """
        申请好友（只有见过面的人可以申请好友）
        只要不是好友/黑名单,就可以申请好友
        :param user_id: 用户ID
        :param friend_user_id: 另一用户ID
        :return:
        """
        if self.record_meet.is_met(apply_id):
            user_id = int(user_id)
            friend_user_id = int(friend_user_id)
            if self.friend.is_friend_or_black(user_id, friend_user_id):
                return Result.result_failed("you have been friends or blacks!")
            else:
                if self.friend.has_valid_apply(user_id, friend_user_id):
                    return Result.result_failed("you have a valid apply!")
                else:
                    friend = self.friend.get_friend_by_user_and_friend(friend_user_id, user_id)
                    if not friend:
                        success = self.friend.add_apply(user_id, friend_user_id)
                        if success:
                            self.im_friend.apply_friend(user_id, friend_user_id, "")
                            log_string = "%d apply %d to be friend" % (user_id, friend_user_id)
                            OHHOLog.print_log(log_string)
                            return Result.result_success()
                        else:
                            return Result.result_failed()
                    else:
                        self.friend.add_friend(user_id, friend_user_id, friend.apply_id)
                        return Result.result_success("add friend successfully!")
        else:
            return Result.result_failed("you are not met!")
