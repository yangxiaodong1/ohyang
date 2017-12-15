from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.types import Integer, String, ForeignKey
from DB.mysql.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'ohho_user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))  # or Column(String(30))
    last_name = Column(String(50))
    username = Column(String(100))
    password = Column(String(100))

