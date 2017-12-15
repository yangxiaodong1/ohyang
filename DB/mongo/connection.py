from mongoengine import connect
from settings import DBMongo


def connect2db():
    user = DBMongo["user"]
    password = DBMongo["password"]
    host = DBMongo["host"]
    db = DBMongo["db"]
    if user and password:
        connection = connect(user=user, password=password, host=host, db=db)
    else:
        connection = connect(host=host, db=db)
    return connection

print(connect2db())

