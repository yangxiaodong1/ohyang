from sqlalchemy.ext.declarative import declarative_base
from DB.mysql.connection import engines

BaseModel = declarative_base()


def init_db(index=0):
    if engines and len(engines) > index:
        BaseModel.metadata.create_all(engines[index])


def drop_db(index=0):
    if engines and len(engines) > index:
        BaseModel.metadata.drop_all(engines[index])
