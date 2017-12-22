from ohho.common.logic.common.record.meet import Meet
from ohho.common.logic.common.user import User
from ohho.common.logic.common.constant import PUSH_STATE_TYPE_END_MEET
from ohho.common.db.ohho.map.db_ohho_map_information import DBOHHOMapInformation
from ohho.common.db.ohho.user.db_ohho_user_configuration import DBOHHOUserConfiguration
from ohho.common.logic.common.result import Result


class LogicRematch(object):
    def __init__(self):
        self.meet = Meet()
        self.user = User()
        self.map = DBOHHOMapInformation()
        self.configuration = DBOHHOUserConfiguration()

    def rematch(self, user_id, friend_user_id, apply_id, is_published):
        # 加到exclude表中, 取消见面
        # type 0:未被惩罚
        # type 1: 惩罚，删除这个人以前的惩罚，加到惩罚表中；关闭本人的配对开关
        self.meet.add_exclude(user_id, friend_user_id)
        user_map = self.map.get_by_user(user_id)
        friend_map = self.map.get_by_user(friend_user_id)
        user_address = user_map.address if user_map else ""
        friend_user_address = friend_map.address if friend_map else ""

        self.meet.add_meet_end(apply_id, user_id, user_address)
        self.meet.add_meet_end(apply_id, friend_user_id, friend_user_address)

        self.meet.delete_meeting(apply_id, user_id)
        self.meet.delete_meeting(apply_id, friend_user_id)
        if not self.meet.is_meet_end(apply_id, friend_user_id):
            data = dict()
            data["user_id"] = user_id
            data["apply_id"] = apply_id
            self.user.push_user_information(friend_user_id, PUSH_STATE_TYPE_END_MEET, data)

        if is_published:
            self.meet.delete_published_by_user(user_id)
            data = dict()
            data["user_id"] = user_id
            data["apply_id"] = apply_id
            self.meet.add_published(data)
            configuration = self.configuration.get_by_user(user_id)
            if configuration:
                self.configuration.close_match(configuration)
        return Result.result_success()
