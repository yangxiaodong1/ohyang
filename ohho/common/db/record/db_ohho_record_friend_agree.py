from DB.mysql.models.ohho.record.model_ohho_record_friend_agree import OHHORecordFriendAgree as model
from ohho.common.db.db_base import DBBase
from DB.common.operation import Operation


class DBOHHORecordFriendAgree(DBBase):
    def __init__(self):
        super(DBOHHORecordFriendAgree, self).__init__(model)

    def filter_by_apply(self, apply_id):
        query = self.get_query()
        return Operation.filter(query, self.model.apply_id, apply_id)

    def get_nearest_agree(self, apply_id):
        query = self.filter_by_apply(apply_id)
        query = self.order_by_id_desc(query)
        return self.first(query)

    def find_by_apply(self, apply_id_list):
        query = self.get_query()
        return Operation.in_(query, self.model.apply_id, apply_id_list)
