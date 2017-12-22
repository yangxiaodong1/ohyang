from ohho.common.db.ohho.base.db_ohho_hint import DBOHHOHint
from ohho.common.logic.common.base.base_class import BaseClass


class Hint(BaseClass):
    def __init__(self):
        super(Hint, self).__init__(DBOHHOHint)

    def get_by_key(self, key):
        return self.instance.get_by_key(key)

    def get_by_parent_id(self, parent_id):
        return self.instance.get_by_parent_id(parent_id)

    def find_by_name(self, query, name):
        return self.instance.find_by_name(query, name)
