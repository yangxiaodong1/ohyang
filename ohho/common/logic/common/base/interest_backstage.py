from ohho.common.db.ohho.base.db_ohho_interest import DBOHHOInterest
# from DB.mysql.models.ohho.model_ohho_watchword import OHHOWatchword
from ohho.common.logic.common.base.base_class import BaseClass


class InterestBackstage(BaseClass):
    def __init__(self):
        super(InterestBackstage, self).__init__(DBOHHOInterest)

    #def get_by_state(self, query, state, has_state=False):
    def get_by_state(self,query, state, has_state):
        return self.instance.get_by_state(query, state, has_state)

    def get_by_parent_id(self, parent_id):
        query = self.instance.get_by_parent_id(parent_id)
        return query