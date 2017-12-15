from ohho.common.db.ohho.base.db_ohho_drink import DBOHHODrink
from ohho.common.logic.common.base.base_class import BaseClass


class Drink(BaseClass):
    def __init__(self):
        super(Drink, self).__init__(DBOHHODrink)
