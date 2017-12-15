from ohho.common.db.ohho.relation.db_ohho_user_and_device_relation import DBOHHOUserAndDeviceRelation
from ohho.common.logic.common.relations.relation_class import RelationClass


class UserAndDeviceRelation(RelationClass):
    def __init__(self):
        super(UserAndDeviceRelation, self).__init__(DBOHHOUserAndDeviceRelation)

    def find_by_device(self, query, device_id_list):
        return self.instance.find_by_device(query, device_id_list)
