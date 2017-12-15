from ohho.common.db.ohho.base.db_ohho_smoke import DBOHHOSmoke
from ohho.common.logic.common.base.base_class import BaseClass

class Smoke(BaseClass):
    def __init__(self):
        super(Smoke, self).__init__(DBOHHOSmoke)

