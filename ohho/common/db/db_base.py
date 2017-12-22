from DB.common.operation import Operation
from Tools.ohho_log import OHHOLog
from ohho.common.logic.common.constant import LESS_THAN_TWO_SECOND_SAMPLE
from ohho.common.logic.common.constant import LESS_THAN_ONE_SECOND_SAMPLE


class DBBase(object):
    def __init__(self, model, index=0):
        self.model = model
        self.index = index

    def get_none(self):
        return Operation.get_none()

    def get_query(self):
        return Operation.get_query(self.model, self.index)

    def get_all(self, query):
        return query.all()

    def get_by_id(self, the_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.id, the_id)
        return Operation.first(query)

    def order_by_id_desc(self, query):
        return Operation.order_by_id_desc(self.model, query)

    def order_by_index_asc(self, query):
        return Operation.order_by_index_asc(self.model, query)

    def order_by_id_asc(self, query):
        return Operation.order_by_id_asc(self.model, query)

    def first(self, query):
        return Operation.first(query)

    def commit(self):
        Operation.commit()

    def rollback(self):
        Operation.rollback()

    def add(self, data):
        try:
            return Operation.add(self.model, data)
        except Exception as ex:
            OHHOLog.print_log(ex)
            return None

    def bulk_add(self, dict_list):
        return Operation.bulk_add(self.model, dict_list)

    def add_without_commit(self, data):
        return Operation.add_without_commit(self.model, data)

    def update(self, instance, data):
        return Operation.update(instance, data)

    def update_without_commit(self, instance, data):
        return Operation.update_without_commit(instance, data)

    def offset(self, query, offset):
        return Operation.offset(query, offset)

    def limit(self, query, limit):
        return Operation.limit(query, limit)

    def delete(self, instance, has_state=False):
        if has_state:
            data = {"state": 0}
            return Operation.update(instance, data)
        else:
            return Operation.delete(instance)

    def delete_without_commit(self, instance, has_state=False):
        if has_state:
            data = {"state": 0}
            return Operation.update_without_commit(instance, data)
        else:
            return Operation.delete_without_commit(instance)

    def restore(self, instance, has_state=False):
        if has_state:
            data = {"state": 1}
            return Operation.update(instance, data)
        return False

    def restore_without_commit(self, instance, has_state=False):
        if has_state:
            data = {"state": 1}
            return Operation.update_without_commit(instance, data)
        return False

    def delete_some(self, query):
        return Operation.delete_some(query)

    def delete_some_without_commit(self, query):
        return Operation.delete_some_without_commit(query)

    def delete_all(self):
        query = self.get_query()
        query.delete()
        # 要使它生效需要执行commit
        # self.commit()

    def get_some(self, query, offset, limit):
        return Operation.get_some(query, offset, limit, self.model)

    def get_information(self, instance, base_url=""):
        data = Operation.get_instance_info(instance, base_url)
        return data

    def is_empty(self, query):
        count = query.count()
        # OHHOLog.print_log(count)
        if count > 0:
            return False
        return True

    def get_by_state(self, query, state, has_state=False):
        if has_state:
            return Operation.filter(query, self.model.state, state)
        else:
            if state:
                return query
            else:
                return None

    def get_valid(self, query, has_state=False):
        return self.get_by_state(query, True, has_state)

    def get_invalid(self, query, has_state=False):
        return self.get_by_state(query, False, has_state)

    def is_valid(self, instance, has_state=False):
        if instance:
            # OHHOLog.print_log("has instance")
            if has_state:
                # OHHOLog.print_log("state exist")
                return instance.state
            else:
                # OHHOLog.print_log("state not exist")
                return True
        else:
            # OHHOLog.print_log("state not exist")
            return False

    def get_count(self, query):
        if query:
            return query.count()
        else:
            return 0

    def get_great_than_equal_created_at(self, query, created_at):
        return Operation.great_than_equal(query, self.model.created_at, created_at)

    def get_less_than_timestamp(self, query, timestamp):
        return Operation.less_than(query, self.model.timestamp, timestamp)

    def get_great_than_equal_timestamp(self, query, timestamp):
        return Operation.great_than_equal(query, self.model.timestamp, timestamp)

    def between_timestamp_two_second(self, query, key, timestamp):
        right = timestamp
        left = (right - LESS_THAN_TWO_SECOND_SAMPLE)
        return Operation.between(query, key, left, right)

    def between_timestamp_one_second(self, query, key, timestamp):
        right = timestamp
        left = (right - LESS_THAN_ONE_SECOND_SAMPLE)
        return Operation.between(query, key, left, right)

    def get_less_than_created_at(self, query, created_at):
        if query:
            return Operation.less_than(query, self.model.created_at, created_at)
        else:
            return None

    def get_great_than_equal_changed_at(self, query, changed_at):
        return Operation.great_than_equal(query, self.model.changed_at, changed_at)

    def get_less_than_changed_at(self, query, changed_at):
        return Operation.less_than(query, self.model.changed_at, changed_at)

    def get_by_type(self, query, type):
        return Operation.filter(query, self.model.type, type)
