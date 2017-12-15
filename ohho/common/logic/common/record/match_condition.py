from ohho.common.db.ohho.base.db_ohho_body_type import DBOHHOBodyType
from ohho.common.db.ohho.base.db_ohho_drink import DBOHHODrink
from ohho.common.db.ohho.base.db_ohho_industry import DBOHHOIndustry
from ohho.common.db.ohho.base.db_ohho_smoke import DBOHHOSmoke
from ohho.common.db.ohho.base.db_ohho_work_domain import DBOHHOWorkDomain

from Tools.ohho_log import OHHOLog
from ohho.common.db.ohho.base.db_ohho_profession import DBOHHOProfession
from ohho.common.db.ohho.record.db_ohho_record_match_condition import DBOHHORecordMatchCondition

from ohho.common.logic.ohho.detail_constant import *


class MatchCondition(object):
    def __init__(self):
        self.condition = DBOHHORecordMatchCondition()

    def add(self, data):
        hometown_list = list()
        current_list = list()
        data["hometown_list"] = hometown_list
        data["current_list"] = current_list
        condition = self.get(data)
        if not condition:
            success = self.condition.add(data)
            if success:
                OHHOLog.print_log(ADD_MATCH_CONDITION_SUCCESS)
                condition = self.get(data)
            else:
                OHHOLog.print_log(ADD_MATCH_CONDITION_FAILED)
        else:
            OHHOLog.print_log(MATCH_CONDITION_EXIST)

        return condition

    def get(self, data_dict):
        query = self.condition.get_query()
        OHHOLog.print_log(query.count())
        query = self.condition.filter_all(query, data_dict)
        OHHOLog.print_log(query.count())
        query = self.condition.order_by_id_asc(query)
        return self.condition.first(query)

    def get_by_id(self, match_condition_id):
        return self.condition.get_by_id(match_condition_id)

    def get_some(self, query, offset, limit):
        return self.condition.get_some(query, offset, limit)

    def update(self, instance, data):
        return self.condition.update(instance, data)

    def delete(self, instance):
        return self.condition.delete(instance)

    def find(self, sex, nickname):
        query = self.condition.get_query()
        if sex != "":
            query = self.condition.filter_by_sex(query, sex)
        if nickname != "":
            query = self.condition.find_by_nickname(query, nickname)
        return query

    def get_name_by_id(self, id, db_mode):
        if id is None:
            return ""
        else:
            instance = db_mode()
            the_object = instance.get_by_id(id)
            return the_object.name if the_object else ""

    def get_information(self, instance):
        information = self.condition.get_information(instance)
        information["drink"] = self.get_name_by_id(instance.drink_id, DBOHHODrink)
        information["smoke"] = self.get_name_by_id(instance.smoke_id, DBOHHOSmoke)
        information["profession"] = self.get_name_by_id(instance.profession_id, DBOHHOProfession)
        information["industry"] = self.get_name_by_id(instance.industry_id, DBOHHOIndustry)
        information["body_type"] = self.get_name_by_id(instance.body_type_id, DBOHHOBodyType)
        information["work_domain"] = self.get_name_by_id(instance.work_domain_id, DBOHHOWorkDomain)
        return information
