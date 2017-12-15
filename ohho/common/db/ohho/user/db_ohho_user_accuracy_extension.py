from DB.mysql.models.ohho.user.model_ohho_user_accuracy_extension import OHHOUserAccuracyExtension
from DB.mysql.models.ohho.user.model_ohho_user import OHHOUser
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_operation import OHHOOperation


class DBOHHOUserAccuracyExtension(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUserAccuracyExtension, self).__init__(OHHOUserAccuracyExtension, index)

    def get_by_user_list(self, user_id_list):
        query = self.get_query()
        return Operation.in_(query, self.model.user_id, user_id_list)

    def get_by_user(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        query = self.order_by_id_asc(query)
        return Operation.first(query)

    def get_by_user_id(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        query = self.order_by_id_asc(query)
        return query

    def get_by_user_id_only_one(self, user_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.user_id, user_id)
        query = self.order_by_id_asc(query)
        query = self.first(query)
        return query

    def get_by_sex(self, query, sex):
        return Operation.filter(query, self.model.sex, sex)

    def get_by_identity_card(self, query, identity_card):
        return Operation.filter(query, self.model.identity_card, identity_card)

    def get_by_real_name(self, query, real_name):
        return Operation.filter(query, self.model.real_name, real_name)

    def get_by_email(self, query, email):
        return Operation.filter(query, self.model.email, email)

    def get_by_nickname(self, query, nickname):
        return Operation.filter(query, self.model.nickname, nickname)

    def get_by_birthday(self, query, birthday):
        return Operation.filter(query, self.model.birthday, birthday)

    def find_by_birthday(self, query, small_date, big_date):
        query = Operation.less_than(query, self.model.birthday, big_date)
        query = Operation.great_than_equal(query, self.model.birthday, small_date)
        return query

    def get_by_small_height(self, query, height):
        return Operation.great_than_equal(query, self.model.height, height)

    def get_by_big_height(self, query, height):
        return Operation.less_than(query, self.model.height, height)

    def get_by_small_weight(self, query, weight):
        return Operation.great_than_equal(query, self.model.weight, weight)

    def get_by_big_weight(self, query, weight):
        return Operation.less_than(query, self.model.weight, weight)

    def get_by_marriage(self, query, marriage):
        return Operation.filter(query, self.model.marriage, marriage)

    def get_by_hometown(self, query, home_town_area):
        return Operation.filter(query, self.model.home_town, home_town_area)

    def get_by_current(self, query, current_area):
        return Operation.filter(query, self.model.current, current_area)

    def parse_interest(self, instance):
        result = dict()
        # if instance and instance.interest:
        #     result = OHHOOperation.json2dict(instance.interest)
        return result


if __name__ == "__main__":
    instance = DBOHHOUserAccuracyExtension()
    user = instance.get_by_user(27)
    print(instance.get_information(user))
    print(user.user.cellphone)
