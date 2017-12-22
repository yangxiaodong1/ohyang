from DB.mysql.models.ohho.base.model_ohho_interest import OHHOInterest
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_log import OHHOLog


class DBOHHOInterest(DBBase):
    def __init__(self, index=0):
        super(DBOHHOInterest, self).__init__(OHHOInterest, index)

    def get_by_key(self, key):
        query = self.get_query()
        query = Operation.filter(query, self.model.key, key)
        query = self.order_by_id_desc(query)
        return self.first(query)

    def find_by_name(self, query, name):
        return Operation.ilike(query, self.model.name, name)

    def delete(self, instance):
        return super(DBOHHOInterest, self).delete(instance, True)

    def restore(self, instance):
        return super(DBOHHOInterest, self).restore(instance, True)

    def get_valid(self, query):
        return super(DBOHHOInterest, self).get_valid(query, True)

    def get_invalid(self, query):
        return super(DBOHHOInterest, self).get_invalid(query, True)

    def get_by_parent_id(self, parent_id):
        query = self.get_query()
        query = self.get_valid(query)
        query = self.order_by_id_desc(query)
        return Operation.filter(query, self.model.parent_id, parent_id)

    # def get_by_id(self, the_id):
    #     return self.get_by_id(the_id)

    def get_level_1(self):
        return self.get_by_parent_id(1)

    def get_level_information(self, parent_id):
        result = list()
        query = self.get_by_parent_id(parent_id)
        if self.is_empty(query):
            return result
        else:
            for q in query:
                # OHHOLog.print_log(q.id)
                temp = self.get_information(q)
                if temp:
                    result.append(temp)
        return result

    def get_level_2_information(self, parent_id):
        result = list()
        level_1 = self.get_by_parent_id(parent_id)
        for level in level_1:
            temp = self.get_information(level)
            if temp:
                temp_data = self.get_level_information(level.id)
                if temp_data:
                    temp["data"] = temp_data
                result.append(temp)
        return result

    def get_level_3_information(self, parent_id):
        result = list()
        level_1 = self.get_by_parent_id(parent_id)
        if self.is_empty(level_1):
            return result
        else:
            for level in level_1:
                temp = self.get_information(level)
                if temp:
                    temp_data = self.get_level_2_information(level.id)
                    if temp_data:
                        temp["data"] = temp_data
                    result.append(temp)
        return result

    def get_some_type(self, name):
        # name = "举报类型"
        query = self.get_query()
        query = self.find_by_name(query, name)
        query = self.order_by_id_asc(query)
        parent = self.first(query)
        if parent:
            return self.get_level_information(parent.id)
        else:
            return list()

    def get_report_type(self):
        name = "举报类型"
        return self.get_some_type(name)

    def get_feedback_type(self):
        name = "反馈类型"
        return self.get_some_type(name)

    def get_cancel_meet_feedback_type(self):
        name = "取消见面反馈类型"
        return self.get_some_type(name)

    def get_complete_meet_feedback_type(self):
        name = "确定见面反馈类型"
        return self.get_some_type(name)

    def get_degree(self):
        name = "学历"
        return self.get_some_type(name)

    def get_work_content(self):
        name = "工作内容"
        return self.get_some_type(name)

    def get_occupation(self):
        name = "行业"
        return self.get_some_type(name)

    def get_information(self, instance):
        result = dict()
        result["name"] = instance.name
        result["id"] = instance.id
        return result


if __name__ == "__main__":
    interest = DBOHHOInterest()
    degree = interest.get_degree()
    result = list()
    for d in degree:
        temp = interest.get_information(d)
        if temp:
            result.append(temp)
    print(result)
