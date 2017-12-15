from DB.mysql.connection import sessions
from sqlalchemy import func
from Tools.ohho_log import OHHOLog
from Tools.ohho_datetime import OHHODatetime
import datetime
import time

if sessions:
    session = sessions[0]


class Operation(object):
    @staticmethod
    def get_session(index=0):
        if sessions and len(sessions) > index:
            return sessions[index]
        return None

    @staticmethod
    def get_none():
        return None

    @staticmethod
    def get_query(model, index=0):
        session = Operation.get_session(index)
        if session:
            return session.query(model)
        return None

    @staticmethod
    def commit(index=0):
        session = Operation.get_session(index)
        if session:
            session.commit()

    @staticmethod
    def rollback(index=0):
        session = Operation.get_session(index)
        if session:
            session.rollback()
        return None

    @staticmethod
    def set_attribute(instance, key, value):
        return setattr(instance, key, value)

    @staticmethod
    def get_attribute(instance, key):
        try:
            return getattr(instance, key)
        except Exception as ex:
            print(ex)
            return ""

    @staticmethod
    def add_without_commit(model, obj_dict):
        try:
            instance = model()
            obj_dict["created_at"] = OHHODatetime.get_utc_now()
            obj_dict["changed_at"] = OHHODatetime.get_utc_now()
            if not obj_dict.get("timestamp", None):
                obj_dict["timestamp"] = OHHODatetime.get_current_timestamp()
            for key, value in obj_dict.items():
                Operation.set_attribute(instance, key, value)
            session.add(instance)
            return True
        except Exception as ex:
            OHHOLog.print_log(ex)
            return False

    @staticmethod
    def bulk_add(model, dict_list):
        try:
            session.execute(model.__table__.insert(), dict_list)
            session.commit()
            return True
        except Exception as ex:
            OHHOLog.print_log(ex)
            return False

    @staticmethod
    def add(model, obj_dict):
        try:
            success = Operation.add_without_commit(model, obj_dict)
            if success:
                Operation.commit()
                return True
            else:
                Operation.rollback()
                return False
        except Exception as ex:
            print(ex)
            return False

    @staticmethod
    def delete_without_commit(instances):
        try:
            session.delete(instances)
            return True
        except Exception as ex:
            OHHOLog.print_log(ex)
            return False

    @staticmethod
    def delete(instances):
        try:
            success = Operation.delete_without_commit(instances)
            if success:
                Operation.commit()
                return True
            else:
                Operation.rollback()
                return False
        except Exception as ex:
            print(ex)
            return False

    @staticmethod
    def delete_some_without_commit(query):
        try:
            for instance in query:
                Operation.delete_without_commit(instance)
            return True
        except Exception as ex:
            OHHOLog.print_log(ex)
            return False

    @staticmethod
    def delete_some(query):
        try:
            success = Operation.delete_some_without_commit(query)
            if success:
                Operation.commit()
                return True
            else:
                Operation.rollback()
                return False
        except Exception as ex:
            OHHOLog.print_log(ex)
            return False

    @staticmethod
    def update_without_commit(instance, obj_dict):
        try:
            obj_dict["changed_at"] = datetime.datetime.utcnow()
            obj_dict["timestamp"] = int(time.time() * 1000)
            for key, value in obj_dict.items():
                setattr(instance, key, value)
            session.merge(instance)
            return True
        except Exception as ex:
            OHHOLog.print_log(ex)
            return False

    @staticmethod
    def update(instance, obj_dict):
        try:
            success = Operation.update_without_commit(instance, obj_dict)
            if success:
                Operation.commit()
                return True
            else:
                Operation.rollback()
                return False
        except Exception as ex:
            OHHOLog.print_log(ex)
            return False

    @staticmethod
    def get_instance_info(instance, base_url=""):
        result = dict()
        if instance:
            for key, value in instance.__dict__.items():
                if key.startswith("_"):
                    continue

                if type(value) == datetime.datetime:
                    result[key] = OHHODatetime.clock2string(OHHODatetime.utc2beijing(value))
                elif type(value) == datetime.date:
                    result[key] = OHHODatetime.date2string(value)
                elif type(value) == int:
                    if not value:
                        result[key] = 0
                    else:
                        result[key] = int(value)
                elif (key.endswith("_id")) or (key in ('sex', 'height', 'weight', 'angle', 'location_type')):
                    if not value:
                        result[key] = 0
                    else:
                        result[key] = value
                elif key in ("icon", "source_icon", "thumbnail"):
                    if value and value.startswith("http"):
                        result[key] = value
                    elif value:
                        result[key] = base_url + value
                    else:
                        result[key] = ""
                elif key in ('longitude', 'latitude'):
                    if value is None:
                        result[key] = 0
                    else:
                        result[key] = float(value)
                elif key in ("interest",):
                    import json
                    if not value:
                        pass
                    else:
                        result[key] = json.loads(value)
                elif not value:
                    if type(value) == str:
                        result[key] = ""
                    else:
                        result[key] = 0
                else:
                    result[key] = value

        return result

    @staticmethod
    def get_like_string(key):
        return "%" + str(key) + "%"

    @staticmethod
    def filter(query, key, value):
        return query.filter(key == value)

    @staticmethod
    def is_not(query, key, value):
        return query.filter(key.isnot(value))

    @staticmethod
    def in_(query, key, value):
        return query.filter(key.in_(value))

    @staticmethod
    def great_than_equal(query, key, value):
        return query.filter(key >= value)

    @staticmethod
    def between(query, key, left, right):
        return query.filter(key.between(left, right))

    @staticmethod
    def less_than(query, key, value):
        return query.filter(key < value)

    @staticmethod
    def ilike(query, key, value):
        like_string = Operation.get_like_string(value)
        return query.filter(key.ilike(like_string))

    @staticmethod
    def first(query):
        if not query:
            return query
        return query.first()

    @staticmethod
    def offset(query, offset):
        if not query:
            return query
        return query.offset(offset)

    @staticmethod
    def limit(query, limit):
        if not query:
            return query
        return query.limit(limit)

    @staticmethod
    def order_by_id_desc(model, query):
        if not query:
            return query
        return query.order_by(model.id.desc())


    @staticmethod
    def order_by_index_asc(model, query):
        if not query:
            return query
        return query.order_by(model.index.asc())
    @staticmethod
    def order_by_id_asc(model, query):
        if not query:
            return query
        return query.order_by(model.id.asc())

    @staticmethod
    def get_some(query, offset, limit, model):
        if not query:
            return query, 0
        count = query.count()
        query = Operation.order_by_id_desc(model, query)

        if offset > 0:
            query = Operation.offset(query, offset)
        if limit > 0:
            query = Operation.limit(query, limit)
        return query, count

    # @staticmethod
    # def group_by(key, index=0):
    #     session = Operation.get_session(index)
    #     if session:
    #         return session.query(key, func.count(key)).group_by(key)

    @staticmethod
    def is_empty(query):
        if not query:
            return True
        count = query.count()
        if count > 0:
            return False
        return True


if __name__ == "__main__":
    session.rollback()
