from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection(object):
    @staticmethod
    def get_engine(connection, echo=False):
        return create_engine(connection, echo=echo, encoding="utf-8")

    @staticmethod
    def get_session(engine):
        db_session = sessionmaker(bind=engine)
        return db_session()


if __name__ == "__main__":
    from settings import DBMysql

    if DBMysql:
        the_settings = DBMysql[0]
        connection = "mysql+pymysql://" + the_settings["user"] + ":" + the_settings["password"] + \
                     "@" + the_settings["host"] + "/" + the_settings["db"]
        session = Connection.get_session(connection)
        # print(session.encoding)
