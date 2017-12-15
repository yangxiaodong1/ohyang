from ohho.common.db.ohho.base.db_ohho_drink import DBOHHODrink
from ohho.common.logic.common.result import Result


class LogicAddDrink(object):
    def __init__(self):
        self.drink = DBOHHODrink()

    def add(self, name):
        data = dict()
        data["name"] = name
        drink = self.drink
        success = drink.add(data)
        if success:
            result = Result.result_success()
        else:
            result = Result.result_failed()
        return result
