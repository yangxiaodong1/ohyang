from DB.mysql.models.ohho.user.model_ohho_user import OHHOUser
from DB.mysql.models.ohho.user.model_ohho_user_accuracy_extension import OHHOUserAccuracyExtension
from DB.mysql.models.ohho.cellphone.model_ohho_country_code import OHHOCountryCode
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_datetime import OHHODatetime


class DBOHHOUser(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUser, self).__init__(OHHOUser, index)

    def get_by_username(self, username):
        query = self.get_query()
        query = Operation.filter(query, self.model.username, username)
        return self.first(query)

    def get_by_cellphone_from_query(self, query, cellphone):
        return Operation.filter(query, self.model.cellphone, cellphone)

    def get_by_cellphone(self, cellphone):
        query = self.get_query()
        query = self.get_valid(query)
        query = Operation.filter(query, self.model.cellphone, cellphone)
        query = self.order_by_id_asc(query)
        return self.first(query)

    def exist_valid_cellphone(self, cellphone):
        query = self.get_query()
        query = self.get_valid(query)
        query = Operation.filter(query, self.model.cellphone, cellphone)
        if self.is_empty(query):
            return False
        else:
            return True

    def exist_valid_cellphone_country_code_id(self, country_code_id, cellphone):
        query = self.get_by_country_code_and_cellphone(country_code_id, cellphone)
        if query:
            return True
        else:
            return False

    def find_by_cellphone(self, query, cellphone):
        return Operation.ilike(query, self.model.cellphone, cellphone)

    def find_by_username(self, username):
        query = self.get_query()
        return Operation.ilike(query, self.model.username, username)

    def get_by_password(self, query, password):
        return Operation.filter(query, self.model.password, password)

    def get_valid(self, query):
        return super(DBOHHOUser, self).get_valid(query, True)

    def get_invalid(self, query):
        return super(DBOHHOUser, self).get_invalid(query, True)

    def get_by_country_code(self, query, country_code_id):
        return Operation.filter(query, self.model.country_code_id, country_code_id)

    def get_by_country_code_and_cellphone(self, country_code_id, cellphone):
        query = self.get_query()
        query = self.get_by_country_code(query, country_code_id)
        query = Operation.filter(query, self.model.cellphone, cellphone)
        query = self.order_by_id_asc(query)
        return self.first(query)

    def delete(self, instance):
        return super(DBOHHOUser, self).delete(instance, True)

    def restore(self, instance):
        return super(DBOHHOUser, self).restore(instance, True)


if __name__ == "__main__":
    instance = DBOHHOUser()
    user = instance.get_by_id(27)
    print(instance.get_information(user))
    print(user.user_accuracy_extensions)
