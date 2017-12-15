from ohho.common.db.ohho.db_cellphone import DBCellphone
from ohho.common.db.ohho.relation.db_ohho_user_and_cellphone_relation import DBOHHOUserAndCellphoneRelation
from ohho.common.logic.common.result import Result
from Tools.ohho_log import OHHOLog
from ohho.common.logic.ohho.detail_constant import CELLPHONE_EXIST
from ohho.common.logic.ohho.detail_constant import RESTORE_SUCCESS
from ohho.common.logic.ohho.detail_constant import RESTORE_FAILED


class Cellphone(object):
    def __init__(self, key=None):
        self.cellphone = DBCellphone(key)
        self.relation = DBOHHOUserAndCellphoneRelation()

    def set_key(self, key):
        self.cellphone.set_key(key)

    def get_key(self):
        return self.cellphone.get_key()

    def get(self):
        return self.cellphone.get_by_key()

    def get_by_id(self, cellphone_id):
        return self.cellphone.get_by_id(cellphone_id)

    def delete(self, cellphone):
        return self.cellphone.delete(cellphone)

    def update(self, cellphone, data_dict):
        if cellphone:
            return self.cellphone.update(cellphone, data_dict)
        else:
            return None

    def add_cellphone(self, cellphone_dict):
        key = cellphone_dict.get("key", None)
        if key is not None and key is not "":
            self.cellphone.set_key(key)
            cellphone = self.get()
            if cellphone:
                result = Result.result_exist(CELLPHONE_EXIST)
                result["cellphone_id"] = cellphone.id
            else:
                success = self.cellphone.add(cellphone_dict)
                if success:
                    cellphone = self.get()
                    result = Result.result_success()
                    result["cellphone_id"] = cellphone.id
                else:
                    result = Result.result_failed()
        else:
            result = Result.result_parameters_are_invalid()
        return result

    def delete_relations(self, user_id):
        relations = self.relation.get_by_user(user_id)
        valid_relations = self.relation.get_by_state(relations, True, has_state=True)
        for relation in valid_relations:
            self.relation.delete(relation)

    def bind_cellphone(self, cellphone_id, user_id):
        result = dict()
        result["success"] = False
        relation = self.relation.get_by_cellphone_and_user(cellphone_id, user_id)
        if relation and self.relation.is_valid(relation, has_state=True):
            result = Result.result_success(CELLPHONE_EXIST)
            # else:
            #     self.delete_relations(user_id)
            #     restore = self.relation.restore(relation)
            #     if restore:
            #         result = Result.result_success(RESTORE_SUCCESS)
            #     else:
            #         result = Result.result_failed(RESTORE_FAILED)
        else:
            self.delete_relations(user_id)
            data_dict = dict()
            data_dict["user_id"] = user_id
            data_dict["cellphone_id"] = cellphone_id
            temp = self.relation.add(data_dict)
            if temp:
                result = Result.result_success()
            else:
                result = Result.result_failed()
        return result

    def is_bound_by_user(self, cellphone_id, user_id):
        # OHHOLog.print_log(cellphone_id)
        # OHHOLog.print_log(user_id)
        relation = self.relation.get_by_cellphone_and_user(cellphone_id, user_id)
        if self.relation.is_valid(relation, has_state=True):
            return True
        else:
            return False

    def get_all_cellphone(self):
        return self.cellphone.get_query()

    def find_by_key(self, query, cellphone_key):
        return self.cellphone.find_by_key(query, cellphone_key)

    def find_by_manufacturer(self, query, manufacturer):
        return self.cellphone.find_by_manufacturer(query, manufacturer)

    def find_by_platform(self, query, platform_type):
        return self.cellphone.find_by_platform(query, platform_type)

    def find_by_mac_address(self, query, mac_address):
        return self.cellphone.find_by_mac_address(query, mac_address)

    def get_some_cellphones(self, query, offset, limit):
        count = query.count()
        query = self.cellphone.order_by_id_desc(query)

        if offset > 0:
            query = self.cellphone.offset(query, offset)
        if limit > 0:
            query = self.cellphone.limit(query, limit)

        return query, count
