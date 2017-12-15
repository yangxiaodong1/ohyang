from DB.mysql.models.ohho.feedback.model_ohho_complete_meet_feedback import OHHOCompleteMeetFeedback
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOCompleteMeetFeedback(DBBase):
    def __init__(self, index=0):
        super(DBOHHOCompleteMeetFeedback, self).__init__(OHHOCompleteMeetFeedback, index)

    def get_by_user(self, user_id):
        query = self.get_query()
        return Operation.filter(query, self.model.user_id, user_id)


if __name__ == "__main__":
    pass
