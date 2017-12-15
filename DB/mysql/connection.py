from DB.common.connection import Connection
from settings import DBMysql

connections = list()

for mysql_setting in DBMysql:
    temp = "mysql+pymysql://" + mysql_setting["user"] + ":" + mysql_setting["password"] + \
           "@" + mysql_setting["host"] + "/" + mysql_setting["db"] + "?charset=utf8"
    connections.append(temp)


# if connections:
#     connection = connections[0]
# else:
#     connection = None


# connection = "mysql+pymysql://" + DBMysql["user"] + ":" + DBMysql["password"] + \
#              "@" + DBMysql["host"] + "/" + DBMysql["db"] + "?charset=utf8"


def get_engines(echo=False):
    engines = list()
    if connections:
        for connection in connections:
            engines.append(Connection.get_engine(connection, echo))
    return engines


def get_sessions(echo=False):
    sessions = list()
    engines = get_engines(echo)
    if engines:
        for engine in engines:
            sessions.append(Connection.get_session(engine))
    return sessions


engines = get_engines()
if engines:
    engine = engines[0]
else:
    engine = None

sessions = get_sessions()
if sessions:
    session = sessions[0]
else:
    session = None

if __name__ == "__main__":
    sql = "insert into cellphone(manufacture) value('华为')"
    session.execute(sql)
    session.commit()
    # session.rollback()
    # session = get_session()
    # print(session.execute("show databases").fetchall())
