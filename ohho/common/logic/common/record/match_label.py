from ohho.common.db.ohho.db_ohho_body_type import DBOHHOBodyType
from ohho.common.db.ohho.db_ohho_drink import DBOHHODrink
from ohho.common.db.ohho.db_ohho_industry import DBOHHOIndustry
from ohho.common.db.ohho.db_ohho_smoke import DBOHHOSmoke
from ohho.common.db.ohho.db_ohho_work_domain import DBOHHOWorkDomain

from Tools.ohho_log import OHHOLog
from ohho.common.db.ohho.db_ohho_profession import DBOHHOProfession
from ohho.common.db.record.db_ohho_record_match_label import DBOHHORecordMatchLabel
from DB.common.operation import Operation

from ohho.common.logic.ohho.detail_constant import *


class MatchLabel(object):
    def __init__(self):
        self.label = DBOHHORecordMatchLabel()

    def get_query(self):
        return self.label.get_query()

    def order_by_id_desc(self, query):
        return self.label.order_by_id_desc(query)

    def first(self, query):
        return self.label.first(query)

    def get_some(self, query, offset, limit):
        return self.label.get_some(query, offset, limit)

    def add(self, data):
        return self.label.add(data)

    def get_by_id(self, label_id):
        return self.label.get_by_id(label_id)

    def get_by_name(self, query, name):
        return self.label.get_by_name(query, name)

    def is_empty(self, query):
        return self.label.is_empty(query)

    def get_by_parent_id(self, query, parent_id):
        return self.label.get_by_parent_id(query, parent_id)

    def update(self, instance, data):
        return self.label.update(instance, data)

    def delete(self, instance):
        return self.label.delete(instance, True)

    def get_information(self, instance):
        return self.label.get_information(instance)
