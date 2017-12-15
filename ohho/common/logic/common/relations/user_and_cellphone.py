from ohho.common.db.ohho.relation.db_ohho_user_and_cellphone_relation import DBOHHOUserAndCellphoneRelation
from ohho.common.logic.common.relations.relation_class import RelationClass


class UserAndCellphoneRelation(RelationClass):
    def __init__(self):
        super(UserAndCellphoneRelation, self).__init__(DBOHHOUserAndCellphoneRelation)

    def find_by_cellphone(self, query, cellphone_id_list):
        return self.instance.find_by_cellphone(query, cellphone_id_list)