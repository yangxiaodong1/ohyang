from ohho.common.db.ohho.base.db_ohho_profession import DBOHHOProfession
from ohho.common.logic.common.base.base_class import BaseClass

class Profession(BaseClass):
    def __init__(self):
        super(Profession, self).__init__(DBOHHOProfession)
