from DB.mysql.models.ohho.record.model_ohho_record_friend_apply import OHHORecordFriendApply as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation
from ohho.common.logic.common.record.constant import VALID_INTERVAL_MILLISECOND
from Tools.ohho_datetime import OHHODatetime
from Tools.ohho_log import OHHOLog


class DBOHHORecordFriendApply(DBBase):
    def __init__(self):
        super(DBOHHORecordFriendApply, self).__init__(model)

    def get_by_one_user(self, query, one_user_id):
        return Operation.filter(query, self.model.one_user_id, one_user_id)

    def get_by_another_user(self, query, another_user_id):
        return Operation.filter(query, self.model.another_user_id, another_user_id)

    def get_by_timestamp_great_than_equal(self, query, timestamp):
        return Operation.great_than_equal(query, self.model.timestamp, timestamp)

    def get_by_timestamp_less_than(self, query, timestamp):
        return Operation.less_than(query, self.model.timestamp, timestamp)

    def is_valid_instance(self, instance):
        if instance:
            timestamp = OHHODatetime.get_current_timestamp()
            if instance.timestamp + VALID_INTERVAL_MILLISECOND < timestamp:
                return False
            return True
        else:
            return False
