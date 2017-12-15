from DB.mysql.models.ohho.report.model_ohho_report import OHHOReport
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBOHHOReport(DBBase):
    def __init__(self, index=0):
        super(DBOHHOReport, self).__init__(OHHOReport, index)

    def get_by_identity(self, identity_id):
        query = self.get_query()
        query = Operation.filter(query, self.model.identity_id, identity_id)
        return Operation.first(query)

    def get_by_user(self, query, user_id):
        return Operation.filter(query, self.model.user_id, user_id)

    def get_by_reported_user(self, query, reported_user_id):
        return Operation.filter(query, self.model.reported_user_id, reported_user_id)


if __name__ == "__main__":
    report = DBOHHOReport()
    query = report.get_query()
    query = report.order_by_id_desc(query)
    query = report.get_all(query)
    print(query)
    if query:
        print("YES")
    else:
        print("NO")
    pass
    # identity_id = 123456789
    # device = DBOHHOReport.get_by_identity(identity_id)
    # print(device.id)
