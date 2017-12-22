from DB.mysql.models.ohho.user.model_ohho_user_impression import OHHOUserImpression
from DB.mysql.models.ohho.user.model_ohho_user_accuracy_extension import OHHOUserAccuracyExtension
from DB.mysql.models.ohho.cellphone.model_ohho_country_code import OHHOCountryCode
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase
from Tools.ohho_datetime import OHHODatetime
from sqlalchemy import func
from sqlalchemy import desc, asc


class DBOHHOUserImpression(DBBase):
    def __init__(self, index=0):
        super(DBOHHOUserImpression, self).__init__(OHHOUserImpression, index)

    def get_user_impression_list_by_user_id(self, user_id):
        query = self.get_query()
        query = self.get_by_type(query, 0)
        query = Operation.filter(query, self.model.user_id, user_id)
        query = self.order_by_id_desc(query)
        return query

    def get_query_new(self, index=0):
        session = Operation.get_session(index)
        if session:
            return session.query(self.model.content_id, self.model.id,
                                 func.count(self.model.content_id).label("count_content"))
        return None

    def get_user_impression(self, user_id, type):
        query = self.get_query_new()
        query = Operation.filter(query, self.model.another_user_id, user_id).group_by(self.model.content_id)
        query = self.get_by_type(query, type)
        query = query.order_by(desc("count_content"), desc(self.model.changed_at)).limit(5)
        query = self.get_all(query)

        return query


if __name__ == "__main__":
    pass
