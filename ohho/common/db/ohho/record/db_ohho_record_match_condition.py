from DB.mysql.models.ohho.record.model_ohho_record_match_condition import OHHORecordMatchCondition
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase

DEFAULT = None
DEFAULT_LIST = list()


class DBOHHORecordMatchCondition(DBBase):
    def __init__(self, index=0):
        super(DBOHHORecordMatchCondition, self).__init__(OHHORecordMatchCondition, index)

    # search start
    def get_nearest_by_interest(self, interest):
        query = self.get_query()
        query = Operation.filter(query, self.model.interest, interest)
        query = self.order_by_id_desc(query)
        return Operation.first(query)

    def filter_by_sex(self, query, sex):
        return Operation.filter(query, self.model.sex, sex)

    def filter_by_email(self, query, email):
        return Operation.filter(query, self.model.email, email)

    def filter_by_nickname(self, query, nickname):
        return Operation.filter(query, self.model.nickname, nickname)

    def find_by_nickname(self, query, nickname):
        return Operation.ilike(query, self.model.nickname, nickname)

    def filter_by_birthday(self, query, birthday):
        return Operation.filter(query, self.model.birthday, birthday)

    def filter_by_big_height(self, query, big_height):
        return Operation.filter(query, self.model.big_height, big_height)

    def filter_by_small_height(self, query, small_height):
        return Operation.filter(query, self.model.small_height, small_height)

    def filter_by_big_weight(self, query, big_weight):
        return Operation.filter(query, self.model.big_weight, big_weight)

    def filter_by_small_weight(self, query, small_weight):
        return Operation.filter(query, self.model.small_weight, small_weight)

    def filter_by_marriage(self, query, marriage):
        return Operation.filter(query, self.model.marriage, marriage)

    def filter_by_hometown(self, query, hometown_list):
        return Operation.in_(query, self.model.hometown_area, hometown_list)

    def filter_by_current(self, query, current_list):
        return Operation.in_(query, self.model.current_area, current_list)

    def filter_by_industry(self, query, industry_id):
        return Operation.filter(query, self.model.industry_id, industry_id)

    def filter_by_profession(self, query, profession_id):
        return Operation.filter(query, self.model.profession_id, profession_id)

    def filter_by_drink(self, query, drink_id):
        return Operation.filter(query, self.model.drink_id, drink_id)

    def filter_by_smoke(self, query, smoke_id):
        return Operation.filter(query, self.model.smoke_id, smoke_id)

    def filter_by_body_type(self, query, body_type_id):
        return Operation.filter(query, self.model.body_type_id, body_type_id)

    def filter_by_work_domain(self, query, work_domain_id):
        return Operation.filter(query, self.model.work_domain_id, work_domain_id)

    def filter_all(self, query, data):
        sex = data.get("sex", DEFAULT)
        query = self.filter_by_sex(query, sex)

        email = data.get("email", DEFAULT)
        query = self.filter_by_email(query, email)

        nickname = data.get("nickname", DEFAULT)
        query = self.filter_by_nickname(query, nickname)

        birthday = data.get("birthday", DEFAULT)
        query = self.filter_by_birthday(query, birthday)

        big_height = data.get("big_height", DEFAULT)
        query = self.filter_by_big_height(query, big_height)

        small_height = data.get("small_height", DEFAULT)
        query = self.filter_by_small_height(query, small_height)

        big_weight = data.get("big_weight", DEFAULT)
        query = self.filter_by_big_weight(query, big_weight)

        small_weight = data.get("small_weight", DEFAULT)
        query = self.filter_by_small_weight(query, small_weight)

        marriage = data.get("marriage", DEFAULT)
        query = self.filter_by_marriage(query, marriage)

        hometown_list = data.get("hometown_list", DEFAULT_LIST)
        if hometown_list:
            query = self.filter_by_hometown(query, hometown_list)

        current_list = data.get("current_list", DEFAULT_LIST)
        if current_list:
            query = self.filter_by_current(query, current_list)

        industry_id = data.get("industry_id", DEFAULT)
        query = self.filter_by_industry(query, industry_id)

        smoke_id = data.get("smoke_id", DEFAULT)
        query = self.filter_by_smoke(query, smoke_id)

        drink_id = data.get("drink_id", DEFAULT)
        query = self.filter_by_drink(query, drink_id)

        profession_id = data.get("profession_id", DEFAULT)
        query = self.filter_by_profession(query, profession_id)

        body_type_id = data.get("body_type_id", DEFAULT)
        query = self.filter_by_body_type(query, body_type_id)

        work_domain_id = data.get("work_domain_id", DEFAULT)
        query = self.filter_by_work_domain(query, work_domain_id)

        return query

        # sex = data.get("sex", DEFAULT)
        # if sex is not None:
        #     query = self.filter_by_sex(query, sex)
        #
        # OHHOLog.print_log(query.count())
        #
        # email = data.get("email", DEFAULT)
        # if email is not None:
        #     query = self.filter_by_email(query, email)
        #
        # OHHOLog.print_log(query.count())
        #
        # nickname = data.get("nickname", DEFAULT)
        # if nickname is not None:
        #     query = self.filter_by_nickname(query, nickname)
        #
        # OHHOLog.print_log(query.count())
        #
        # birthday = data.get("birthday", DEFAULT)
        # if birthday is not None:
        #     query = self.filter_by_birthday(query, birthday)
        #
        # OHHOLog.print_log(query.count())
        #
        # big_height = data.get("big_height", DEFAULT)
        # if big_height is not None:
        #     query = self.filter_by_big_height(query, big_height)
        #
        # OHHOLog.print_log(query.count())
        #
        # small_height = data.get("small_height", DEFAULT)
        # if small_height is not None:
        #     query = self.filter_by_small_height(query, small_height)
        #
        # OHHOLog.print_log(query.count())
        #
        # big_weight = data.get("big_weight", DEFAULT)
        # if big_weight is not None:
        #     query = self.filter_by_big_weight(query, big_weight)
        #
        # OHHOLog.print_log(query.count())
        #
        # small_weight = data.get("small_weight", DEFAULT)
        # if small_weight is not None:
        #     query = self.filter_by_small_weight(query, small_weight)
        #
        # OHHOLog.print_log(query.count())
        #
        # marriage = data.get("marriage", DEFAULT)
        # if marriage is not None:
        #     query = self.filter_by_marriage(query, marriage)
        #
        # OHHOLog.print_log(query.count())
        #
        # hometown_list = data.get("hometown_list", DEFAULT_LIST)
        # if hometown_list:
        #     query = self.filter_by_hometown(query, hometown_list)
        #
        # OHHOLog.print_log(query.count())
        #
        # current_list = data.get("current_list", DEFAULT_LIST)
        # if current_list:
        #     query = self.filter_by_current(query, current_list)
        #
        # industry_id = data.get("industry_id", DEFAULT)
        # if industry_id is not None:
        #     query = self.filter_by_industry(query, industry_id)
        #
        # smoke_id = data.get("smoke_id", DEFAULT)
        # if smoke_id is not None:
        #     query = self.filter_by_smoke(query, smoke_id)
        #
        # drink_id = data.get("drink_id", DEFAULT)
        # if drink_id is not None:
        #     query = self.filter_by_drink(query, drink_id)
        #
        # profession_id = data.get("profession_id", DEFAULT)
        # if profession_id is not None:
        #     query = self.filter_by_profession(query, profession_id)
        #
        # body_type_id = data.get("body_type_id", DEFAULT)
        # if body_type_id is not None:
        #     query = self.filter_by_body_type(query, body_type_id)
        #
        # work_domain_id = data.get("work_domain_id", DEFAULT)
        # if work_domain_id is not None:
        #     query = self.filter_by_work_domain(query, work_domain_id)
        #
        # return query


if __name__ == "__main__":
    pass
