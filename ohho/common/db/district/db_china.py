from DB.mysql.models.district.model_china import China
from DB.common.operation import Operation
from ohho.common.db.db_base import DBBase


class DBChina(DBBase):
    def __init__(self):
        super(DBChina, self).__init__(China)


if __name__ == "__main__":
    china = DBChina()
    obj = china.get_by_id(1)
    print(obj.name)
