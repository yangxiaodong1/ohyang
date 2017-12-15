from ohho.common.db.ohho.base.db_ohho_body_type import DBOHHOBodyType
from ohho.common.logic.common.base.base_class import BaseClass


class BodyType(BaseClass):
    def __init__(self):
        super(BodyType, self).__init__(DBOHHOBodyType)
